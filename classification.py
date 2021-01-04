from trains import Task
import time
import random

task = task = Task.init(project_name='classification', task_name='classification')

logger = task.get_logger()

iterations = 5000
for iteration in range(iterations):
    if iteration % 10 == 0:
        print('{} / {}'.format(iteration, iterations))
    if iteration % 100 == 0:
        print('{} / {}'.format(iteration, iterations))
    logger.report_scalar('title','series',iteration=iteration,value=iteration)
    time.sleep(0.05)