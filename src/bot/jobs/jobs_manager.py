from telegram.ext import ContextTypes

def remove_job_if_exists(name: str, context: ContextTypes.DEFAULT_TYPE) -> bool:
    '''! Remove job with given name. Returns whether job was removed.'''
    current_jobs = context.job_queue.get_jobs_by_name(name)
    if not current_jobs:
        return False
    for job in current_jobs:
        job.schedule_removal()
    return True