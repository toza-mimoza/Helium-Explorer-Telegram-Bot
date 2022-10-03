from telegram import Update
from telegram.constants import ParseMode
from telegram.ext import ContextTypes
from bot.db.DBUtil import DBUtil
from bot.db.model.BotInstance import BotInstance
from bot.db.model.User import User
from bot.helium.RequestHandler import *
from bot.jobs.jobs_manager import register_helium_jobs_for_user, deregister_helium_jobs_for_user
from bot.ui.menu.MenuManager import MenuManager
from util.constants import DbConstants, UiLabels
from bot.ui.template.menus import build_main_menu, build_sub_menu_overview, build_sub_menu_snooze, build_sub_menu_settings
from bot.jobs import delete_stale_menu_nodes_for_user, update_hotspots, fetch_activities, cleanup_inactive_user


def init_menu_manager_for_user(update: Update):
    telegram_user_id = update.message.from_user.id
    menu_manager = DBUtil.get_menu_manager_for_user(telegram_user_id)
    if not menu_manager:
        menu_manager = MenuManager(telegram_user_id)
    DBUtil.insert_or_update_record(
        DbConstants.TREE_MENU_MANAGERS, telegram_user_id, menu_manager)

    return menu_manager


async def ui_start(update: Update, context: ContextTypes):
    '''
    Start bot UI action. This action apart from activating bot instance it registers jobs that run repeatedly for specific user.
    '''
    telegram_user_id = update.message.from_user.id
    telegram_user_name = update.message.from_user.username
    # logic for inserting new user to db
    DBUtil.insert_or_update_record(DbConstants.TREE_USERS, telegram_user_id, User(
        telegram_user_id, telegram_user_name))

    if not DBUtil.is_in_db(DbConstants.TREE_BOT_INSTANCE, telegram_user_id):
        DBUtil.insert_or_update_record(DbConstants.TREE_BOT_INSTANCE, telegram_user_id, BotInstance(telegram_user_id))
    
    DBUtil.activate_bot_for_user(telegram_user_id)

    register_helium_jobs_for_user(telegram_user_id, context)

    menu_manager = init_menu_manager_for_user(update)
    menu_manager.set_menu(build_main_menu(telegram_user_id))
    await context.bot.send_message(chat_id=update.message.chat_id,
                                   text=UiLabels.UI_MSG_MAIN,
                                   reply_markup=menu_manager.get_current_menu().get_menu())


async def ui_stop(update: Update, context: ContextTypes):
    '''
    Stop button bot UI action. This action deactivates the bot instance for the user, which prevents sending notifications.
    The user record (User model; Telegram user abstraction) is deactivated. 
    Jobs specific for the user are removed from the job queue.
    '''
    telegram_user_id = get_telegram_user_id(update)
    # logic for deactivating bot instance for telegram user
    bot_instance = DBUtil.get_bot_for_user(telegram_user_id)
    bot_instance.active = False
    bot_instance.update()

    deregister_helium_jobs_for_user(telegram_user_id, context)
    
    menu_manager = init_menu_manager_for_user(update)
    menu_manager.set_menu(build_main_menu(telegram_user_id))
    await context.bot.send_message(chat_id=update.message.chat_id,
                                   text=UiLabels.UI_MSG_MAIN,
                                   reply_markup=menu_manager.get_current_menu().get_menu())


async def ui_back(update: Update, context: ContextTypes):
    '''
    Back button bot UI action.
    '''
    telegram_user_id = update.message.from_user.id
    menu_manager = init_menu_manager_for_user(update)
    menu_manager.delete_oldest_periodically(5)
    menu_manager.update_last_active(menu_manager.backward())
    await context.bot.send_message(chat_id=update.message.chat_id,
                                   text=UiLabels.UI_MSG_MAIN,
                                   reply_markup=menu_manager.backward().get_menu())


async def ui_overview(update: Update, context: ContextTypes):
    '''
    Overview menu bot UI action.
    '''
    telegram_user_id = update.message.from_user.id
    menu_manager = init_menu_manager_for_user(update)
    menu_manager.set_menu(build_sub_menu_overview(telegram_user_id))
    await context.bot.send_message(chat_id=update.message.chat_id,
                                   text=UiLabels.UI_MSG_OVERVIEW,
                                   reply_markup=menu_manager.get_current_menu().get_menu())


async def ui_snooze(update: Update, context: ContextTypes):
    '''
    Snooze notifications menu UI action.
    '''
    telegram_user_id = update.message.from_user.id
    menu_manager = init_menu_manager_for_user(update)
    menu_manager.set_menu(build_sub_menu_snooze(telegram_user_id))
    await context.bot.send_message(chat_id=update.message.chat_id,
                                   text=UiLabels.UI_MSG_SNOOZE,
                                   reply_markup=menu_manager.get_current_menu().get_menu())


async def ui_settings(update: Update, context: ContextTypes):
    '''
    Settings menu UI action.
    '''
    telegram_user_id = update.message.from_user.id
    menu_manager = init_menu_manager_for_user(update)
    menu_manager.set_menu(build_sub_menu_settings(telegram_user_id))
    await context.bot.send_message(chat_id=update.message.chat_id,
                                   text=UiLabels.UI_MSG_SETTINGS,
                                   reply_markup=menu_manager.get_current_menu().get_menu())

def get_telegram_user_id(update):
    return update.message.from_user.id
