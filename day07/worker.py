class WorkingWorker(object):

    BASE_TASK_TIME = 61

    def __init__(self, task):
        self.task = task
        self.time_remaining = self._work_time(task)


    def _work_time(self, task):
        return ord(task.upper()) - ord('A') + WorkingWorker.BASE_TASK_TIME
