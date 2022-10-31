import time
from rich.progress import track

for i in track(range(10), complete_style='green'):
    print("one loop has been finished")
    time.sleep(1)
