#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""An extendable daemon implementation."""

import logging
from datetime import datetime
from threading import Lock, Thread
from time import sleep


class Daemon():
    """An extendable daemon implementation."""

    interval = 30.0
    stopped = False
    lock = Lock()
    daemon_locked = False
    main_thread = None

    def __init__(self, interval):
        """Construct a new daemon instance."""
        self.interval = float(interval)
        self.main_thread = Thread(target=self._main_loop)

    def start(self):
        """Start the daemon."""
        self.main_thread.start()

    def stop(self):
        """Stop the daemon."""
        self.stopped = True
        self.main_thread.join()

    def _main_loop(self):
        # single-run mode
        if self.interval <= 0:
            self._invoke_process()
            return
        # interval mode
        while not self.stopped:
            thr = Thread(target=self._invoke_process)
            thr.start()
            sleep(self.interval)

    def _invoke_process(self):
        if self.daemon_locked:
            logging.debug('Daemon already processing')
            return
        self._lock_daemon()
        self._run_daemon_process()
        self._unlock_daemon()

    def _run_daemon_process(self):
        """Override with your implementation."""
        pass

    def _lock_daemon(self):
        self.lock.acquire()
        self.daemon_locked = True
        self.lock.release()

    def _unlock_daemon(self):
        self.lock.acquire()
        self.daemon_locked = False
        self.lock.release()


if __name__ == '__main__':
    class MyDaemon(Daemon):  # noqa: D101

        def _invoke_process(self):
            print(datetime.now().timestamp())

    my_daemon = MyDaemon(1)
    my_daemon.start()
    sleep(5)
    my_daemon.stop()
