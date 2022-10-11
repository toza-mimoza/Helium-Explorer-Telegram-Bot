from telegram import Update
from telegram.constants import ParseMode
from telegram.ext import ContextTypes
from bot.db.DBUtil import DBUtil
from bot.db.model.BotInstance import BotInstance
from bot.db.model.User import User
from bot.helium.RequestHandler import *
from bot.jobs.jobs_manager import register_helium_jobs_for_user, deregister_helium_jobs_for_user
from bot.setup_actions import setup_start
from bot.ui.menu.MenuManager import MenuManager
from util.constants import DbConstants, UiLabels
from bot.ui.template.menus import build_main_menu, build_sub_menu_overview, build_sub_menu_snooze, build_sub_menu_settings
from util import get_telegram_user_id, get_telegram_username

def _init_menu_manager_for_user(update: Update):
    telegram_user_id = update.message.from_user.id
    menu_manager = DBUtil.get_menu_manager_for_user(telegram_user_id)
    if not menu_manager:
        menu_manager = MenuManager(telegram_user_id)
        menu_manager.update()
    return menu_manager


async def ui_setup(update: Update, context: ContextTypes):
    '''
    Setup bot UI action. This action runs a conversation handler for setting up bot account.
    '''
    telegram_user_id = update.message.from_user.id
    telegram_user_name = update.message.from_user.username
    # logic for inserting new user to db
    DBUtil.insert_or_update_record(DbConstants.TREE_USERS, telegram_user_id, User(
        telegram_user_id, telegram_user_name))

    if not DBUtil.is_in_db(DbConstants.TREE_BOT_INSTANCE, telegram_user_id):
        # activate/insert bot instance for the user
        DBUtil.insert_or_update_record(DbConstants.TREE_BOT_INSTANCE, telegram_user_id, BotInstance(telegram_user_id))

    user = User(telegram_user_id, telegram_user_name)
    user.is_registered = False
    user.update()
    
    if not DBUtil.is_user_registered(telegram_user_id):
        log.info(f'User {telegram_user_id} has not registered account, beginning setup...')

        # trigger conversation handler

        await setup_start(update, context)


async def ui_start(update: Update, context: ContextTypes):
    '''
    Start bot UI action. This action apart from activating bot instance it registers jobs that run repeatedly for specific user.
    '''
    telegram_user_id = get_telegram_user_id(update)
    telegram_user_name = get_telegram_username(update)
    # telegram_user_name = update.message.from_user.username
    if not DBUtil.exists_user(telegram_user_id):
        user = User(telegram_user_id, telegram_user_name)
        user.update()
    if DBUtil.is_user_registered(telegram_user_id):
        bot_instance = BotInstance(telegram_user_id)
        bot_instance.active = True
        bot_instance.update()
    
    register_helium_jobs_for_user(telegram_user_id, context)

    menu_manager = _init_menu_manager_for_user(update)
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
    bot_instance: BotInstance | None = DBUtil.get_bot_for_user(telegram_user_id)
    if not bot_instance:
        await ui_start(update, context)
        return 
    bot_instance.active = False
    bot_instance.update()

    deregister_helium_jobs_for_user(telegram_user_id, context)
    
    menu_manager = _init_menu_manager_for_user(update)
    menu_manager.set_menu(build_main_menu(telegram_user_id))
    await context.bot.send_message(chat_id=update.message.chat_id,
                                   text=UiLabels.UI_MSG_MAIN,
                                   reply_markup=menu_manager.get_current_menu().get_menu())


async def ui_back(update: Update, context: ContextTypes):
    '''
    Back button bot UI action.
    '''
    telegram_user_id = update.message.from_user.id
    menu_manager = _init_menu_manager_for_user(update)
    # menu_manager.delete_oldest_periodically(5)
    # menu_manager.update_last_active(menu_manager.backward())
    await context.bot.send_message(chat_id=update.message.chat_id,
                                   text=UiLabels.UI_MSG_MAIN,
                                   reply_markup=menu_manager.backward().get_menu())


async def ui_overview(update: Update, context: ContextTypes):
    '''
    Overview menu bot UI action.
    '''
    telegram_user_id = update.message.from_user.id
    menu_manager = _init_menu_manager_for_user(update)
    menu_manager.set_menu(build_sub_menu_overview(telegram_user_id))
    await context.bot.send_message(chat_id=update.message.chat_id,
                                   text=UiLabels.UI_MSG_OVERVIEW,
                                   reply_markup=menu_manager.get_current_menu().get_menu())


async def ui_snooze(update: Update, context: ContextTypes):
    '''
    Snooze notifications menu UI action.
    '''
    telegram_user_id = update.message.from_user.id
    menu_manager = _init_menu_manager_for_user(update)
    menu_manager.set_menu(build_sub_menu_snooze(telegram_user_id))
    await context.bot.send_message(chat_id=update.message.chat_id,
                                   text=UiLabels.UI_MSG_SNOOZE,
                                   reply_markup=menu_manager.get_current_menu().get_menu())


async def ui_settings(update: Update, context: ContextTypes):
    '''
    Settings menu UI action.
    '''
    telegram_user_id = update.message.from_user.id
    menu_manager = _init_menu_manager_for_user(update)
    menu_manager.set_menu(build_sub_menu_settings(telegram_user_id))
    await context.bot.send_message(chat_id=update.message.chat_id,
                                   text=UiLabels.UI_MSG_SETTINGS,
                                   reply_markup=menu_manager.get_current_menu().get_menu())
