from trains import Task, Logger
import time
import random


task = Task.init(project_name='segmentation', task_name='segmentation')
logger = task.get_logger()

iterations = random.randint(100,500)
for iteration in range(iterations):
    logger.report_scalar('title','series',iteration=iteration,value=iteration)
    time.sleep(0.05)

