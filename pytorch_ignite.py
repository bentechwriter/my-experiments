from trains import Task
from ignite.engine import Events
import time
import random

task = Task.init(project_name='object detection', task_name='object detection')
logger = task.get_logger()

iterations = 10000
for iteration in range(iterations):
    if iteration % 10 == 0:
        print('{} / {}'.format(iteration, iterations))
    logger.report_scalar('title','series',iteration=iteration,value=iteration)
    time.sleep(0.05)