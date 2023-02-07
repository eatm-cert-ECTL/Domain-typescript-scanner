import queue
import threading
import time
from typing import Any

from PyQt5.QtCore import QObject, pyqtSignal


class Job_Queue(QObject):
    advancement = pyqtSignal(int)

    def __init__(self, function, elements:list[Any], nb_threads:int=200) -> None:
        """Model of a Job Queue, creates a pool of threads that apply independently a function to a set of elements

        Args:
            QObject (:class:`QObject`): a QObject
        """
        super().__init__()
        self.function = function
        self.elements = elements
        self.nb_threads = nb_threads

    def run_job_queue(self) -> None:
        """Starts the creation of the thread pool and the execution of all the jobs
        """
        threads = []

        self.jobs = queue.Queue()

        for elem in self.elements:
            self.jobs.put(elem)

        number = len(self.elements)
        
        for _ in range(min(self.nb_threads,number)):
            worker = Job_Thread(self.jobs, self.function)
            worker.setDaemon(True)
            worker.start()
            threads.append(worker)

        while self.jobs.unfinished_tasks > 0:
            self.advancement.emit(100 * (number - self.jobs.unfinished_tasks) / number)
            time.sleep(1.0)
            
        for worker in threads:
            worker.join()


class Job_Thread(threading.Thread):
    def __init__(self, queue:Job_Queue, function) -> None:
        """ Initialize a Job Thread, which applies a function on an element of the queue

        Args:
            queue (:class:`queue`): a queue with the jobs to do
            function (function): the function to apply on the elements of the queue
        """
        threading.Thread.__init__(self)
        self.jobs = queue
        self.function = function
        self.kill_received = False
        
    def run(self) -> None:
        while not self.kill_received:
            try:
                element = self.jobs.get(block=False)
            except queue.Empty:
                self.kill_received = True
                return
            
            self.function(element)

            self.jobs.task_done()