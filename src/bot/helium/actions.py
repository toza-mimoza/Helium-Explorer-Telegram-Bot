from datetime import datetime
from telegram import Update
from telegram.constants import ParseMode
from telegram.ext import ContextTypes
from bot.helium.RequestHandler import *
from bot.db.DBUtil import DBUtil
from bot.db.model import Activity, User, Owner, Hotspot
from bot.message_actions import send_html_message, send_mdv2_message, send_message
from util.constants import DbConstants
from util import hr_hotspot_name
from util.formatter_helper import _b, _bit, escape
from util.time_helper import get_days_ago_time_str, get_iso_utc_time

import logging
log = logging.getLogger(__name__)

##
# @file actions.py
#
# @brief Messages as response to commands from Telegram users. 
# This file also contains internal actions from the bot for fetching latest hotspot data.
#
# @section description_main Description
# Main driving Python file for the Telegram Bot.
# 
# @section notes_actions_helium Notes
# - Methods used for updating hotspot are prefixed with an underscore.
#
# @section author_init_bot Author(s)
# - Created by Svetozar Stojanovic on 09/07/2022.
# - Modified by Svetozar Stojanovic on 09/15/2022.
#
# Copyright (c) 2022 Svetozar Stojanovic.  All rights reserved.


#######################################################
#
# Helper functions for this file.
#
#######################################################


async def _check_preconditions_owner(account_address, mode: ParseMode, update: Update=None, context: ContextTypes=None, silent=False):
    """! This function checks if the Telegram user is an owner and based on that it either informs the user and returns False since the check is failed or True if passed."""

    if not account_address:
        # this means Telegram user is not registered owner for this bot
        if not silent or not update:
            msg = "You haven't added any hotspots or you are not a registered hotspot owner. Send '/start' and follow the instructions there."    
            await update.message.reply_text(text=msg, parse_mode=mode)
        return False

    # get hotspot(s)
    hotspots = DBUtil.get_hotspots_by_owner(account_address)

    if not hotspots:
        if not silent and update:
            msg = "You haven't added any hotspots or you are not an owner. Send '/start' and follow the instructions there."    
            await update.message.reply_text(text=msg, parse_mode=mode)
        return False
        
    if len(hotspots) > 1:
        if not context.args:
            if not silent and update:
                msg = "You haven't entered a hotspot address as argument."    
                await update.message.reply_text(text=msg, parse_mode=mode)
            return False

        hotspot_address = context.args[0]
        
        found = False
        for hotspot in hotspots:
            if hotspot.hotspot_address == hotspot_address:
                found = True

        if not found:
            if not silent and update:
                msg = "You have entered an incorrect hotspot address format."    
                await update.message.reply_text(text=msg, parse_mode=mode)
        return False
    return True
    
def _get_telegram_user_id(update):
    telegram_user_id = str(update.message.from_user.id)
    return telegram_user_id

def _get_telegram_username(update):
    telegram_user_id = update.message.from_user.username
    return telegram_user_id


#######################################################
#
# Helium messages to users.
#
#######################################################

async def send_blockchain_stats(update: Update, context: ContextTypes):
    '''! Get Helium Blockchain stats
    '''
    telegram_user_id = update.message.from_user.id
    mode = ParseMode.HTML
    response = BCStatsFormatter.get_message(await RequestHandler.get_bc_stats(), parse_mode=mode)
   
    await send_html_message(response, update, context)

async def send_token_supply(update: Update, context: ContextTypes):
    '''! Get and send current token supply
    '''
    mode = ParseMode.HTML
    response = TokenSupplyFormatter.get_message(await RequestHandler.get_token_supply(), parse_mode=mode)
    
    await send_html_message(response, update, context)

async def send_hotspot_data(update: Update, context: ContextTypes):
    '''! Get and send hotspot data
    '''
    mode = ParseMode.HTML
    response = HotspotDataFormatter.get_message(await RequestHandler.get_hotspot_data(), parse_mode=mode)
    
    await send_html_message(response, update, context)

async def send_all_hotspot_activity(update: Update, context: ContextTypes):
    '''! Get and send hotspot all time activity 
    '''
    mode = ParseMode.HTML
    response = HotspotActivityFormatter.get_message(await RequestHandler.get_hotspot_activity(), parse_mode=mode)
    
    await send_html_message(response, update, context)

async def send_recent_hotspot_activity(update: Update, context: ContextTypes):
    '''! Get and send recent 24h hotspot activity
    '''
    mode = ParseMode.HTML
    response = HotspotActivityFormatter.get_message(await RequestHandler.get_hotspot_roles(), parse_mode=mode)
    
    msg = response
    await send_html_message(msg, update, context)

async def send_roles_for_account(update: Update, context: ContextTypes):
    '''! Send 10 recent roles for Helium account address. 
    '''
    mode = ParseMode.MARKDOWN
    telegram_user_id = _get_telegram_user_id(update)
    account_address = DBUtil.get_account_address_from_telegram_user_id(telegram_user_id)
    
    passed_checks = await _check_preconditions_owner(account_address, mode, update, context)
    if not passed_checks:
        return
    
    responses = await RequestHandler.get_account_roles(account_address)
    
    msg = ''
    await send_message(msg, update, context)

async def send_hotspot_activity(update: Update, context: ContextTypes):
    """! Send ten recent hotspot activities/roles to the user."""
    telegram_user_id = _get_telegram_user_id(update)
    mode = ParseMode.MARKDOWN
    # account address is owner unique id / Helium account address
    account_address = DBUtil.get_account_address_from_telegram_user_id(telegram_user_id)
    
    passed_checks = await _check_preconditions_owner(account_address, mode, update, context)
    if not passed_checks:
        return
    
    hotspots = DBUtil.get_hotspots_by_owner(account_address)

    if len(hotspots) > 1:
        # process command argument "/hs_activity [hotspot_address]"
        hotspot_address = context.args[0]
    elif len(hotspots) == 1:
        # if only one hotspot skip arguments from command  
        hotspot_address = hotspots[0].hotspot_address
        
    responses = await RequestHandler.get_hotspot_roles(hotspot_address)
    
    msg = _b('Last 10 hotspot activities: ') + '\n'
    for response in responses:
        for activity in response:
            act = Activity(hash_value=activity['hash'], account_address=account_address, hotspot_address=hotspot_address, activity_type=activity['type'], time=activity['time'], role=activity['role'], height=activity['height'])
            act.update()
            msg += HotspotActivityFormatter.get_message(activity, parse_mode=ParseMode.MARKDOWN) + '\n'
    await send_mdv2_message(msg, update, context)

async def send_hotspot_rewards(update: Update, context: ContextTypes):
    """! Send ten recent days of hotspot rewards to the user."""
    mode = ParseMode.MARKDOWN
    ten_days_ago = get_days_ago_time_str(10)
    response = await RequestHandler.get_hotspot_rewards('1125H4Afvw7TtscVw8xq8ZQ3XFDSFezfurqfy4VYetaw6GpdgbpH', min_time=ten_days_ago, max_time=get_iso_utc_time())

    msg = response
    await send_message(msg, update, context)
    
#######################################################
#
# Internally used functions for updating data
#
#######################################################
async def update_roles_for_account_data(update: Update, context: ContextTypes):
    '''! Updates activities: any kind of transactions for Helium accounts / hotspot owners.'''
    mode = ParseMode.MARKDOWN
    telegram_user_id = _get_telegram_user_id(update)
    account_address = DBUtil.get_account_address_from_telegram_user_id(telegram_user_id)
    passed_checks = await _check_preconditions_owner(account_address, mode, update, context, silent=True)
    if not passed_checks:
        return
    responses = await RequestHandler.get_account_roles(account_address, limit=10)

async def update_hotspot_data(hotspot_address: str, telegram_user_id: int, context: ContextTypes):
    mode = ParseMode.MARKDOWN
    account_address = DBUtil.get_account_address_from_telegram_user_id(telegram_user_id)
    
    if not account_address:
        raise Exception('Account address not found or owner does not exist')
        
    passed_checks = await _check_preconditions_owner(account_address, mode=mode, update=None, context=context)
    if not passed_checks:
        return
    response = await RequestHandler.get_hotspot_data(hotspot_address)

    if not 'error' in response:
        updated_hotspot = Hotspot(hotspot_address, animal_name=response['name'], account_address=response['owner'], status_online=response['status']['online'])
        updated_hotspot.update()

async def insert_hotspots_for_owner(account_address: str, telegram_user_id: int, update: Update, context: ContextTypes):

    response = await RequestHandler.get_hotspots_for_account(account_address)

    msg = '''Following hotspots are registered for monitoring:

    '''

    if response:
        for hotspot in response:
            hs = Hotspot(hotspot['address'], hotspot['name'], hotspot['owner'], hotspot['status']['online'])
            hs.update()
            log.info(f"Inserted/updated hotspot {hotspot['name']} into DB.")
            
            msg = msg + _bit(hr_hotspot_name(hotspot['name'])) + '\n'

        await send_mdv2_message(msg, update, context)
        