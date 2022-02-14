import threading
import time
from random import randrange

THREAD = 0
RUN_TIME = 1
MIN_RUN_TIME = 10
MAX_RUN_TIME = 20


class Thread_Handler:
    """
    This class manage threads functionality
    """

    def __init__(self):
        self.active_threads = dict()

    def _thread_function(self, rand_time):
        """
        This function is the thread running function.
        :param rand_time:thread run time
        """
        time.sleep(rand_time)

    def create_Thread(self):
        """
        This function create thread that run for a random amount of time between 10-20 seconds
        """
        rand_time = randrange(MIN_RUN_TIME, MAX_RUN_TIME)
        thread = threading.Thread(target=self._thread_function, args=(rand_time,))
        thread.start()
        thread_id = thread.ident
        self.active_threads[thread_id] = [thread, rand_time]
        return thread_id

    def delete_thread(self, thread_id):
        """
        This function kill a specific thread with the provided id.
        :param thread_id: thread identifier
        """
        thread_id = int(thread_id)
        if thread_id not in self.active_threads:
            return
        self.active_threads[thread_id][THREAD].stop = True
        del self.active_threads[thread_id]

    def get_run_time(self, thread_id):
        """
        This function return the running time of the given thread
        :param thread_id: thread identifier
        :return: run time in seconds
        """
        return self.active_threads[thread_id][RUN_TIME]

    def get_active_threads(self):
        """
        This function return the alive threads and for each, his run time.
        :return: mapping between threads id and run time
        """
        out = dict()
        for thread_id in self.active_threads:
            if self.active_threads[thread_id][THREAD].is_alive():
                out[thread_id] = self.active_threads[thread_id][RUN_TIME]
        return out
