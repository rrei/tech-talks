from life.ui import TextUI

# Symbols used to represent alive/dead cells in the terminal.
# NOTE: make them 2 characters wide to approximate square shape.
ALIVE = "\u2593" * 2
DEAD = "\u2591" * 2


# Lines displayed at the bottom of the screen to let the user know the controls.
CONTROLS = (
    "(p)ause (s)lower (f)aster (t)ick (r)eset (q)uit",
    "(c)enter [arrow keys to scroll]",
)


class LifeTextUI(TextUI):
    def __init__(self, life, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.initial_life = life
        self.life = life
        self.x, self.y = 0, 0

    def draw(self):
        """Draw a new frame onto the `self.screen`. The basic tools to do so are:

            self.screen.clear()
            self.screen.addstr(text)
            self.screen.refresh()
        """
        ...

    def input(self, key):
        """Handle user input. The values of interest for `key` are listed below:

            "KEY_DOWN"
            "KEY_UP"
            "KEY_RIGHT"
            "KEY_LEFT"
            "c"
            "p"
            "s"
            "f"
            "t"
            "r"
            "q"
        """
        ...
