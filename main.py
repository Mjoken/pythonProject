import multiprocessing
import os
import time


class ClockProcess(multiprocessing.Process):
    def __init__(self, interval):
        multiprocessing.Process.__init__(self)
        self.interval = interval

    def run(self):
        while True:
            print("The time is %s" % time.ctime())
            time.sleep(self.interval)


if __name__ == '__main__':
    proc = ClockProcess(7)
    proc.start()
    while True:
        print("Enter command: ")
        inp = input()
        if "kill" in inp:
            proc.terminate()
            print("Terminated proc: ", proc)
        elif "break" in inp or "exit" in inp:
            break
print('Main process %d terminated' % os.getpid())

# END -----------------------------------------------------------
