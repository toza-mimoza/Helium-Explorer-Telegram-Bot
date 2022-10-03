from telegram.ext import ContextTypes

from bot.db.DBUtil import DBUtil

import logging

from bot.helium.actions import update_hotspot_data
log = logging.getLogger(__name__)

async def cleanup_inactive_user(context: ContextTypes.DEFAULT_TYPE):
    job = context.job
    telegram_user_id = job.data['telegram_user_id']
    # TO-DO
    log.info(f'Executed job cleanup_inactive_user for user {telegram_user_id}')
    pass
async def update_hotspots(context: ContextTypes.DEFAULT_TYPE):
    job = context.job
    telegram_user_id = job.data['telegram_user_id']
    account_address = DBUtil.get_account_address_from_telegram_user_id(telegram_user_id)
    hotspots = DBUtil.get_hotspots_by_owner(account_address)

    if not hotspots:
        log.warn(f'There are no hotspots assigned to this user with telegram_user_id {telegram_user_id}! Aborting update of hotspot(s)!')
        return

    for hotspot in hotspots:
        await update_hotspot_data(hotspot.hotspot_address, context)

    # TO-DO
    log.info(f'Executed job update_hotspots for user {telegram_user_id}')
    pass
async def fetch_activities(context: ContextTypes.DEFAULT_TYPE):
    job = context.job
    telegram_user_id = job.data['telegram_user_id']
    # TO-DO
    log.info(f'Executed job fetch_activities for user {telegram_user_id}')
    pass

async def delete_stale_menu_nodes_for_user(context: ContextTypes.DEFAULT_TYPE):
    job = context.job
    telegram_user_id = job.data['telegram_user_id']
    menu_manager = DBUtil.get_menu_manager_for_user(telegram_user_id)
    menu_manager.delete_oldest_periodically()
    log.info(f'Executed job delete_stale_menu_nodes_for_user for user {telegram_user_id}')
    pass
