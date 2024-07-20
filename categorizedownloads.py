import time
import os
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler


class OnMyWatch:

    watchDirectory = "/home/teageto/Downloads"

    def __init__(self):
        self.observer = Observer()

    def run(self):
        event_handler = Handler()
        self.observer.schedule(
                event_handler, self.watchDirectory, recursive=True
        )
        self.observer.start()
        try:
            while True:
                time.sleep(60)
        except self.observer.stop():
            print("Observer stopped")

        self.observer.join()


class Handler(FileSystemEventHandler):

    @staticmethod
    def on_any_event(event):
        if event.event_type == 'created':
            print(f"{os.listdir(event)}")
            os.replace()
