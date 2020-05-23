from trains import Task
import time

iterations = 100
for iteration in range(iterations):
    print('enqueue round {}'.format(iteration))

    for i in range(4):
        # Get a reference to the task to pipe to.
        next_task = Task.get_task('2c7c7a30254b4fff834790d4d3983a3e')
        # Clone the task to pipe to. This creates a task with status Draft whose parameters can be modified.
        cloned_task = Task.clone(source_task=next_task)
        Task.enqueue(cloned_task.id, queue_name='A1-Queue')

    for i in range(2):
        # Get a reference to the task to pipe to.
        next_task = Task.get_task('3dfd8c59a5ed4053ac64d5142cfbbb04')

        # Clone the task to pipe to. This creates a task with status Draft whose parameters can be modified.
        cloned_task = Task.clone(source_task=next_task)
        Task.enqueue(cloned_task.id, queue_name='A1-Queue')

    for i in range(1):
        # Get a reference to the task to pipe to.
        next_task = Task.get_task('1bbd4693fd62452c95dbb3241294577f')

        # Clone the task to pipe to. This creates a task with status Draft whose parameters can be modified.
        cloned_task = Task.clone(source_task=next_task)
        Task.enqueue(cloned_task.id, queue_name='C3-Queue')

    time.sleep(2)