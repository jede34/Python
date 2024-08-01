from collections import deque 

tasks = [
    {'type': 'fast', 'name': 'Wash dishes'},
    {'type': 'slow', 'name': 'Watch a film'},
    {'type': 'fast', 'name': 'Walk with a dog'},
    {'type': 'fast', 'name': 'Reed a book'}
]

task_queue = deque()

for task in tasks:
    if task['type'] == 'fast':
        task_queue.appendleft(task)
        print(f'Add fast task: {task['name']}')
    else:
        task_queue.append(task)
        print(f'Add slow task: {task['name']}')

while task_queue:
    task = task_queue.popleft()
    print(f'Task complete: {task['name']}')