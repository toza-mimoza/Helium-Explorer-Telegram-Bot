from telegram import Update


def get_telegram_user_id(update: Update):
    return update.message.from_user.id

def get_telegram_username(update: Update):
    return update.message.from_user.username