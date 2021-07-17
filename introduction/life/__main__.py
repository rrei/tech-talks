import sys

from . import loaders, ui

if len(sys.argv) > 2:
    print("python -m life [<RLE_FILE>]")
    sys.exit(1)

if len(sys.argv) == 2:
    life = loaders.rle.load(sys.argv[1])
else:
    life = loaders.random.load(-25, +25, -25, +25)
ui.LifeTextUI(life).start(paused=True)
sys.exit(0)
