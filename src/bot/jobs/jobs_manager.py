from telegram.ext import ContextTypes, JobQueue
from telegram.ext import Application
from bot.db import DBUtil

from bot.jobs.jobs import delete_stale_menu_nodes_for_user, update_hotspots, fetch_activities, cleanup_inactive_user

def remove_job_if_exists(name: str, context: ContextTypes) -> bool:
    '''! Remove job with given name. Returns whether job was removed.'''
    current_jobs = context.job_queue.get_jobs_by_name(name)
    if not current_jobs:
        return False
    for job in current_jobs:
        job.schedule_removal()
    return True


def register_jobs(application: Application):
    job_queue = application.job_queue
    users = DBUtil.get_users()
    data = None

    # jobs independent if bot instance is active for user or not
    # register jobs for all users
    for user in users:
            
        data = {
            'telegram_user_id': user.telegram_user_id
        }
        # job_queue.run_repeating(delete_stale_menu_nodes_for_user, interval=5, first=1, data=data)
        job_queue.run_repeating(cleanup_inactive_user, interval=60*60*24*7, first=1, data=data)
        
    job_queue.start()

def register_helium_jobs_for_user(telegram_user_id: str, context: ContextTypes):
    """! Register jobs that dependend on bot_instance.active field. """ 
    
    job_name_update_hotspots = update_hotspots.__name__+'_'+str(telegram_user_id)
    job_name_fetch_activities = fetch_activities.__name__+'_'+str(telegram_user_id)

    
    data = {
        'telegram_user_id': telegram_user_id
    }
    context.job_queue.run_repeating(name=job_name_update_hotspots, callback=update_hotspots, interval=5, first=1, data=data)
    context.job_queue.run_repeating(name=job_name_fetch_activities, callback=fetch_activities, interval=60, first=1, data=data)

def deregister_helium_jobs_for_user(telegram_user_id: str, context: ContextTypes):
    """! Remove Helium jobs which depend on the user, while Telegram user independent jobs are left."""
    job_name_update_hotspots = update_hotspots.__name__+'_'+str(telegram_user_id)
    job_name_fetch_activities = fetch_activities.__name__+'_'+str(telegram_user_id)

    remove_job_if_exists(job_name_update_hotspots, context)
    remove_job_if_exists(job_name_fetch_activities, context)
