from .formatter_helper import _bit
from telegram.constants import ParseMode

class EventConstants():
    TRIGGER_NOTIFICATION = 'TriggerNotification'
    UPDATE_HOTSPOT = 'UpdateHotspotEvent'

class DbConstants():
    DB_APP_NAME = 'helium.telegram.bot'
    TREE_USERS = 'users'
    TREE_HOTSPOTS = 'hotspots'
    TREE_ACTIVITIES = 'activities'
    TREE_OWNERS = 'owners'
    TREE_EVENTS_LOG = 'events_log'
    TREE_CONFIGURATION = 'configuration'
    TREE_BOT_INSTANCE = 'bot'
    TREE_MENU_NODES = 'menu_nodes'
    TREE_MENU_MANAGERS = 'menu_managers'
    
class UiLabels():
    UI_LABEL_MAIN_MENU = 'Main Menu'
    UI_LABEL_MENU_BACK = 'Back 🔙'
    UI_LABEL_MENU_START = 'Start Bot 🚀'
    UI_LABEL_MENU_STOP = 'Stop Bot 🤚'
    UI_LABEL_MENU_SETTINGS = 'Settings ⚙'
    UI_LABEL_MENU_SNOOZE = 'Snooze ⏰'
    UI_LABEL_MENU_OVERVIEW= 'Overview 📃'
    UI_LABEL_STUB = 'STUB LABEL'

class MsgLabelsMD():
    '''! Formatted message labels'''
    TOKEN_SUPPLY = _bit('Token supply')
    ELECTION_TIMES = _bit('Election times')
    CHALLENGE_COUNTS = _bit('Challenge counts')
    COUNTS = _bit('Counts')
    BLOCK_TIMES = _bit('Block times')
    TRANSACTIONS = _bit('Transactions')
    VALIDATORS = _bit('Validators')
    OUIS = _bit('OUIS')
    CITIES = _bit('Cities')
    COUNTRIES = _bit('Countries')
    BLOCKS = _bit('Blocks')
    CHALLENGES = _bit('Challenges')
    CONSENSUS_GROUPS = _bit('Consensus groups')
    HOTSPOTS = _bit('Hotspots')
    HOTSPOTS_ONLINE = _bit('Hotspots online')
    HOTSPOTS_DATA_ONLY = _bit('Hotspots data only')
    
    LAST_HOUR = _bit('Last hour')
    LAST_DAY = _bit('Last day')
    LAST_WEEK = _bit('Last week')
    LAST_MONTH = _bit('Last month')

    ACTIVE = _bit('Active')
    STDDEV = _bit('Std dev')
    AVG = _bit('Average')
    
    COINGECKO_PRICE_GBP = _bit('Coingecko price GBP')
    COINGECKO_PRICE_USD = _bit('Coingecko price USD')
    COINGECKO_PRICE_EUR = _bit('Coingecko price EUR')

class MsgLabelsHTML():
    '''! Formatted message labels'''
    TOKEN_SUPPLY = _bit('Token supply', ParseMode.HTML)
    ELECTION_TIMES = _bit('Election times', ParseMode.HTML)
    CHALLENGE_COUNTS = _bit('Challenge counts', ParseMode.HTML)
    COUNTS = _bit('Counts', ParseMode.HTML)
    BLOCK_TIMES = _bit('Block times', ParseMode.HTML)
    TRANSACTIONS = _bit('Transactions', ParseMode.HTML)
    VALIDATORS = _bit('Validators', ParseMode.HTML)
    OUIS = _bit('OUIS', ParseMode.HTML)
    CITIES = _bit('Cities', ParseMode.HTML)
    COUNTRIES = _bit('Countries', ParseMode.HTML)
    BLOCKS = _bit('Blocks', ParseMode.HTML)
    CHALLENGES = _bit('Challenges', ParseMode.HTML)
    CONSENSUS_GROUPS = _bit('Consensus groups', ParseMode.HTML)
    HOTSPOTS = _bit('Hotspots', ParseMode.HTML)
    HOTSPOTS_ONLINE = _bit('Hotspots online', ParseMode.HTML)
    HOTSPOTS_DATA_ONLY = _bit('Hotspots data only', ParseMode.HTML)
    
    LAST_HOUR = _bit('Last hour', ParseMode.HTML)
    LAST_DAY = _bit('Last day', ParseMode.HTML)
    LAST_WEEK = _bit('Last week', ParseMode.HTML)
    LAST_MONTH = _bit('Last month', ParseMode.HTML)

    ACTIVE = _bit('Active', ParseMode.HTML)
    STDDEV = _bit('Std dev', ParseMode.HTML)
    AVG = _bit('Average', ParseMode.HTML)
    
    COINGECKO_PRICE_GBP = _bit('Coingecko price GBP', ParseMode.HTML)
    COINGECKO_PRICE_USD = _bit('Coingecko price USD', ParseMode.HTML)
    COINGECKO_PRICE_EUR = _bit('Coingecko price EUR', ParseMode.HTML)