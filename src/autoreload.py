import subprocess
import time
import re
import sys
import os

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

current_processes = []


def start_processes():
    global current_processes
    for proc in current_processes:
        proc.terminate()
    current_processes = [
        subprocess.Popen([sys.executable, 'test.py']),
        subprocess.Popen([sys.executable, 'main.py']),
    ]


class PythonHandler(FileSystemEventHandler):
    def on_any_event(self, event):
        extension = event.src_path.split('.')[-1]
        if extension == 'py':
            start_processes()


if __name__ == "__main__":
    start_processes()
    observer = Observer()
    observer.schedule(PythonHandler(), '.', recursive=True)
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()