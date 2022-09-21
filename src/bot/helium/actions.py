from telegram import Update
from telegram.constants import ParseMode
from telegram.ext import ContextTypes
from bot.helium.RequestHandler import *
from bot.db.DBManager import DBManager
from bot.db.model import Activity, User, Owner, Hotspot
from util.constants import DbConstants

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
# Messages to users
#
#######################################################
async def echo(update: Update, context: ContextTypes):
    '''! Text that is not a command will be echoed back to the user.
    '''
    await context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text)

async def send_blockchain_stats(update: Update, context: ContextTypes):
    '''! Get Helium Blockchain stats
    '''
    telegram_user_id = update.message.from_user.id
    mode = ParseMode.HTML
    response = BCStatsFormatter.get_message(await RequestHandler.get_bc_stats(), parse_mode=mode)
    await update.message.reply_text(text=response, parse_mode=mode)

async def send_token_supply(update: Update, context: ContextTypes):
    '''! Get and send current token supply
    '''
    mode = ParseMode.HTML
    response = TokenSupplyFormatter.get_message(await RequestHandler.get_token_supply(), parse_mode=mode)
    await update.message.reply_text(text=response, parse_mode=mode)

async def send_hotspot_data(update: Update, context: ContextTypes):
    '''! Get and send hotspot data
    '''
    mode = ParseMode.HTML
    response = HotspotDataFormatter.get_message(await RequestHandler.get_hotspot_data(), parse_mode=mode)
    await update.message.reply_text(text=response, parse_mode=mode)

async def send_all_hotspot_activity(update: Update, context: ContextTypes):
    '''! Get and send hotspot all time activity 
    '''
    mode = ParseMode.HTML
    response = HotspotActivityFormatter.get_message(await RequestHandler.get_hotspot_activity(), parse_mode=mode)
    await update.message.reply_text(text=response, parse_mode=mode)

async def send_recent_hotspot_activity(update: Update, context: ContextTypes):
    '''! Get and send recent 24h hotspot activity
    '''
    mode = ParseMode.HTML
    response = HotspotActivityFormatter.get_message(await RequestHandler.get_hotspot_activity(), parse_mode=mode)
    await update.message.reply_text(text=response, parse_mode=mode)

async def send_roles_for_account(update: Update, context: ContextTypes):
    '''! Get and send current token supply
    '''
    mode = ParseMode.MARKDOWN
    response = await RequestHandler.get_roles_for_account('13QsWHxWfk5H55jghPrnT1uLtYAn4qrWxNvDSHqD7d9icmLEEtN')
    
    await update.message.reply_text(text=response, parse_mode=None)


#######################################################
#
# Internally used functions for updating data
#
#######################################################
async def update_roles_for_account_data(update: Update, context: ContextTypes):
    '''! Updates activities: any kind of transactions for Helium accounts / hotspot owners.'''
    telegram_user_id = update.message.from_user.id
    telegram_user_username = update.message.from_user.username

    user = DBManager.get_record(DbConstants.TREE_USERS, telegram_user_id)
    if not user:
        user = User(telegram_id=telegram_user_id, telegram_username=telegram_user_username)
        DBManager.insert_record(DbConstants.TREE_USERS, telegram_user_id, user)
        # return false because the user is new
        return False
    owner = DBManager.get_owner_by_telegram_id(telegram_user_id)
    if not owner:
        return False

    # for each hotspot from the owner 
    response = await RequestHandler.get_hotspot_data()
    data = response['data']


async def update_hotspot_data(update: Update, context: ContextTypes):
#   - gets from Telegram user id an owner
#   - if the owner has hotspots then proceed
#       - else abort
#   - for each hotspot 
#       - update activity data if changed (insert new activities)

    telegram_user_id = update.message.from_user.id
    telegram_user_username = update.message.from_user.username

    user = DBManager.get_record(DbConstants.TREE_USERS, telegram_user_id)
    if not user:
        user = User(telegram_id=telegram_user_id, telegram_username=telegram_user_username)
        DBManager.insert_record(DbConstants.TREE_USERS, telegram_user_id, user)
        # return false because the user is new
        return False
    owner = DBManager.get_owner_by_telegram_id(telegram_user_id)
    if not owner:
        return False

    # for each hotspot from the owner 
    response = await RequestHandler.get_hotspot_data()
    data = response['data']

# get_hotspots_from_owner_address
#   - fetches hotspots from same owner
#   - stores them in db
