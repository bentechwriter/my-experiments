from trains import Task
import time
import random

task = Task.init(project_name='object detection', task_name='object detection')
logger = task.get_logger()

iterations = random.randint(100,500)
for iteration in range(iterations):
    logger.report_scalar('title','series',iteration=iteration,value=iteration)
    time.sleep(0.05)