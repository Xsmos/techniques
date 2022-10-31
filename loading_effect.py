import time

print(format(" Loading effect ", "#^50"))

print("loading", end = '')

for i in range(20):
    print(".", end = '', flush = True)
    time.sleep(0.1)

print()
from progress.bar import FillingSquaresBar
bar = FillingSquaresBar("This loading process is working")
for i in bar.iter(range(100)):
    time.sleep(0.01)

from rich.progress import track

for step in track(range(30)):
    time.sleep(0.1)    