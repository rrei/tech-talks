"""This module implements a basic parser for Run Length Encoded (RLE) patterns. The
format is described in https://conwaylife.com/wiki/Run_Length_Encoded. A collection
of RLE files can be downloaded from https://www.conwaylife.com/patterns/all.zip.

Usage:
    import life

    state = life.loader.rle("/path/to/pattern.rle")
"""
import pathlib
import re

from ..game import Life

ITEM_REGEX = re.compile(r"\s*(?P<count>\d*)(?P<tag>[bo$])\s*(?P<eof>!?)\s*")


class Loader:
    def __init__(self):
        self.life = Life()
        self.x, self.y = 0, 0
        self.finished = False

    def set_alive(self, count):
        self.life.update((self.x + i, self.y) for i in range(count))
        self.x += count

    def set_dead(self, count):
        self.x += count

    def end_line(self, count):
        self.x = 0
        self.y += count


def load(file_path):
    """Create a new `Life` object from the RLE file located at `file_path`."""
    loader = Loader()
    for line in pathlib.Path(file_path).read_text().splitlines():
        _parse_line(line.strip(), loader)
        if loader.finished:
            break
    return loader.life


def _parse_line(line, loader):
    if line.startswith("#") or "=" in line:
        return
    line_pos = 0
    while line_pos < len(line) and not loader.finished:
        line_pos = _parse_item(line, line_pos, loader)


def _parse_item(line, line_pos, loader):
    match = ITEM_REGEX.match(line, pos=line_pos)
    count = int(match["count"]) if match["count"] else 1
    tag = match["tag"]
    if tag == "b":
        loader.set_dead(count)
    elif tag == "o":
        loader.set_alive(count)
    else:
        loader.end_line(count)
    loader.finished = bool(match["eof"] != "")
    return match.end()
