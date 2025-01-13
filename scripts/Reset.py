from scripts import __basepath__
from scripts.Utils import BoundDict
import shutil


def reset(lang: str, d: BoundDict):
    pathResBase = __basepath__ + "RES_BASE/"
    pathResMod = __basepath__ + "RES_MODIFIED/"

    pathResBaseLang = pathResBase + lang + "/res.json"
    pathResModLang = pathResMod + lang + "/res.json"

    shutil.copy(pathResBaseLang, pathResModLang)
    d.load()