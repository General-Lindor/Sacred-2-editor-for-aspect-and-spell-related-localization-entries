import os
import re
import sys

def definePath(fullPath: str | list[str]):
    slash = re.escape("/")
    backslash = re.escape("\\")

    path = ""
    base = ""
    if isinstance(fullPath, list):
        base = os.path.commonpath(fullPath)
    else:
        base = fullPath
    base = os.path.abspath(base)
    base = re.sub(pattern = backslash, repl = slash, string = base)
    base = base.encode("utf-8").decode("unicode_escape")
    base = re.split(slash, base)
    base.pop(len(base) - 1)
    for partialString in base:
        if partialString != "":
            path += partialString + "/"
    return path

__basepath__ = definePath(sys.argv)
__modulepath__ = definePath(__file__)