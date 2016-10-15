from spider.scheduler.services import SchedulerService


def callback(proj_id, taks_id, inter_links):
    # log proj and task
    SchedulerService.scheduling_tasks(proj_id, inter_links)
