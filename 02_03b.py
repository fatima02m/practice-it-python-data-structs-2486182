from collections import deque

# can use a 'class' for tasks to add task description
# class can be used for a "variable" that has some properties you want to use
# or stuff you want to do

# creating a class for task so you can give each task a description and a priority


class Task(object):
    def __init__(self, taskDesc, hasPriority=False):
        self.taskDesc = taskDesc
        self.hasPriority = hasPriority

    def __str__(self):
        return "Task:{0}, Priority:{1}".format(self.taskDesc, self.hasPriority)


task_queue = deque()
# creating a add task method


def add_task(task):
    if task.hasPriority:
        task_queue.appendleft(task)
    else:
        task_queue.append(task)


def task_todo():
    return task_queue.popleft()


def print_tasks():
    for t in task_queue:
        print(t.taskDesc)


def main():
    add_task(Task("Make List"))
    add_task(Task("Make Breakfast"))
    add_task(Task("Respond to email", True))
    print_tasks()
    print(task_todo())
    return


if __name__ == "__main__":
    main()
