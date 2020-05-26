from trains import Task, Logger
import time
import random


task = Task.init(project_name='segmentation', task_name='segmentation')
logger = task.get_logger()

iterations = 5000
for iteration in range(iterations):
    if iteration % 100 == 0:
        print('{} / {}'.format(iteration, iterations))
    logger.report_scalar('title','series',iteration=iteration,value=iteration)
    time.sleep(0.05)

