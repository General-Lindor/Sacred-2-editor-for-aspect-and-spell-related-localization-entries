########################################################################################################
## THIS SCRIPT GENERATES res.json OUT OF decoded.txt ###################################################
## decoded.txt IS THE HASH-VALUE-MAP THAT s2rw.exe CREATES IN .TXT UTF-16LE_BOM FILE FORMAT ############
########################################################################################################

#values: dict[str, dict[str, list[str] | dict[int, list[str]]]] = {
values = {
    "SERAPHIM" : {
        "SE_COMBAT" : {
            1404 : ["SE_CO_SEELENHAMMER",],
            1403 : ["SE_CO_SCHLAGHAGEL",],
            1405 : ["SE_CO_WIRBELSPRUNG",],
            1401 : ["SE_CO_BEFLUEGELN",],
            1402 : ["SE_CO_KAMPFHALTUNG",],
        },
        "SE_CELESTIALMAGIC" : {
            1397 : ["SE_CM_BLITZ",],
            1400 : ["SE_CM_LICHTSAEULE",],
            1396 : ["SE_CM_BEKEHRUNG",],
            1398 : ["SE_CM_HEILEN",],
            1399 : ["SE_CM_LICHTAURA",],
        },
        "SE_TECHNICS" : {
            1410 : ["SE_TE_SCHWERTFEUER",],
            1409 : ["SE_TE_SCHOCKWELLE",],
            1408 : ["SE_TE_NOTSCHILD",],
            1407 : ["SE_TE_ENERGIESCHILD",],
            1406 : ["SE_TE_BEEEFFGEE",],
        },
    },
    "DRYADE" : {
        "DR_HUNT" : {
            1478 : ["DR_HU_KONZENTRIERTERANGRIFF",],
            1477 : ["DR_HU_ANGRIFFSSERIE",],
            1480 : ["DR_HU_SPRINT",],
            1481 : ["DR_HU_WIRBELN",],
            1479 : ["DR_HU_PROJEKTILFOKUS",],
        },
        "DR_VOODOO" : {
            1488 : ["DR_VO_QUAELEN",],
            1483 : ["DR_VO_KRANKHEIT",],
            1490 : ["DR_VO_VERDERBENSFLUCH",],
            1489 : ["DR_VO_TOTEM",],
            1491 : ["DR_VO_ZOMBIE",],
        },
        "DR_NATUREMAGIC" : {
            1482 : ["DR_NM_BODENSPIESSE",],
            1487 : ["DR_NM_WUCHERWURZEL",],
            1484 : ["DR_NM_HANDAUFLEGEN",],
            1486 : ["DR_NM_WACHERVERSTAND",],
            1485 : ["DR_NM_RINDENHAUT",],
        },
    },
    "SCHATTENKRIEGER" : {
        "SK_HEAVYCOMBAT" : {
            508 : ["SK_HC_HARTERSCHLAG",],
            507 : ["SK_HC_BEFREIUNGSSCHLAG",],
            510 : ["SK_HC_RAMMSTOSS",],
            509 : ["SK_HC_KAMPFRUF",],
            511 : ["SK_HC_WILLENSSTAERKE",],
        },
        "SK_TACTICALCOMBAT" : {
            373 : ["SK_TC_ATTACKE",],
            613 : ["SK_TC_SPRUNG",],
            614 : ["SK_TC_STANDARTE",],
            612 : ["SK_TC_KAMPFRAUSCH",],
            503 : ["SK_TC_UMLENKUNG",],
        },
        "SK_ASTRALPLANE" : {
            499 : ["SK_AP_GEISTERHAND",],
            506 : ["SK_AP_UNTERSTUETZUNG",],
            502 : ["SK_AP_KAMPFBEFEHL",],
            501 : ["SK_AP_GEISTFORM", "SK_AP_GEISTFORM_BUFF",],
            504 : ["SK_AP_KOHORTE",],
        },
    },
    "INQUISITOR" : {
        "IN_INQUISITION" : {
            801 : ["IN_IN_HINRICHTUNG",],
            804 : ["IN_IN_VERSTUEMMELUNG",],
            800 : ["IN_IN_PRANGER",],
            803 : ["IN_IN_EIFER",],
            802 : ["IN_IN_KASTEIUNG",],
        },
        "IN_POWER" : {
            809 : ["IN_PO_FAECHERBLITZ",],
            805 : ["IN_PO_MACHTSOG",],
            808 : ["IN_PO_MACHTSTOSS",],
            807 : ["IN_PO_DOPPELGAENGER", "IN_PO_DOPPELGAENGER_BUFF",],
            806 : ["IN_PO_VERGELTUNG",],
        },
        "IN_UNDERWORLD" : {
            811 : ["IN_UW_SEELENRAUB",],
            812 : ["IN_UW_ENTSETZEN",],
            810 : ["IN_UW_VERSKLAVUNG",],
            813 : ["IN_UW_SCHAENDUNG",],
            814 : ["IN_UW_SEELENFAENGER",],
        },
    },
    "HOCHELFE" : {
        "HE_INFERNO" : {
            815 : ["HE_IN_FEUERBALL",],
            816 : ["HE_IN_FEUERSTURM",],
            817 : ["HE_IN_METEOR",],
            818 : ["HE_IN_FEUERDAEMON",],
            819 : ["HE_IN_FEUERHAUT",],
        },
        "HE_STORM" : {
            824 : ["HE_ST_FROSTSCHLAG",],
            823 : ["HE_ST_EISSPLITTER",],
            820 : ["HE_ST_SCHNEESTURM",],
            821 : ["HE_ST_NEBELFORM",],
            827 : ["HE_ST_KRISTALLHAUT",],
        },
        "HE_ARCANE" : {
            828 : ["HE_AR_ENERGIEBLITZ",],
            826 : ["HE_AR_MAGISCHERSCHLAG",],
            822 : ["HE_AR_TELEPORT",],
            829 : ["HE_AR_BANNKREIS",],
            825 : ["HE_AR_REGENERATIONSKRAFT",],
        },
    },
    "TEMPELWACHE" : {
        "TW_CLOSECOMBAT" : {
            1465 : ["TW_CC_SCHOEPFUNGSSCHLAG",],
            1463 : ["TW_CC_KAMPFARM",],
            1467 : ["TW_CC_TODESSPIESSE",],
            1464 : ["TW_CC_KAMPFAURA", "TW_CC_KAMPFAURA_BUFF",],
            1466 : ["TW_CC_TKAMPFSCHILD",],
        },
        "TW_TECHNOLOGY" : {
            1475 : ["TW_TE_PROJEKTIL",],
            1474 : ["TW_TE_FLAMMENWERFER",],
            1476 : ["TW_TE_TSCHOCK",],
            1473 : ["TW_TE_ARCHIMEDISSTRAHL",],
            1798 : ["TW_TE_LEVITIEREN",],
        },
        "TW_ENERGY" : {
            1471 : ["TW_EN_MUTIEREN",],
            1470 : ["TW_EN_GLUTHITZE",],
            1468 : ["TW_EN_EISESKAELTE",],
            1469 : ["TW_EN_ENERGIENETZ",],
            1472 : ["TW_EN_SCHOCKPULSE",],
        },
    },
    "DRACHENMAGIER" : {
        "DM_DRAGONMAGIC" : {
            3130 : ["DM_DM_BERSERKERFORM",],
            3129 : ["DM_DM_DRACHENFORM",],
            3132 : ["DM_DM_DRACHENSCHLAG",],
            3131 : ["DM_DM_EWIGESFEUER",],
            3133 : ["DM_DM_VERTRAUTER",],
        },
        "DM_COMMAND" : {
            3137 : ["DM_CO_ZERSTOERER",],
            3135 : ["DM_CO_WINDSTOSS",],
            3136 : ["DM_CO_MAGISCHERWALL",],
            3134 : ["DM_CO_WIRBELWIND",],
            3138 : ["DM_CO_BESCHUETZER",],
        },
        "DM_MENTALISM" : {
            3139 : ["DM_ME_GEDANKENSCHLAG",],
            3140 : ["DM_ME_ENERGIEBRAND",],
            3141 : ["DM_ME_MAHLSTROM",],
            3142 : ["DM_ME_KAMPFTRANCE",],
            3143 : ["DM_ME_SCHUTZRUNEN",],
        },
#        "OTHER" : [
#            "DM_FORM_TRAVEL_SPRUNG",
#            "DM_FORM_ANY_RECALL",
#            "DM_FORM_BRSRK_BLUTRAUSCH",
#            "DM_FORM_BRSRK_ZERFETZEN",
#            "DM_FORM_DRGN_TELEPORT",
#            "DM_FORM_DRGN_FEUERBALL",
#            "DM_FORM_DRGN_FEUERWAND",
#        ],
    },
#    "OTHER" : ["EA_OTHER", "EA_ALL_HORSE",],
}

#########################################################################################################################################
## EXTRACT ##############################################################################################################################
#########################################################################################################################################

import hashgen as h

hashes = {}
with open(file="decoded.txt", mode="r", encoding="utf-16") as f:
    for line in f:
        #print(line[0:10])
        #input()
        hashes[line[0:10]] = line[11:-1]

def manuallyResolve(key: str, valueList: list[str]) -> str:
    print("\nKEY: " + key)
    curr = 0
    for value in valueList:
        print(str(curr) + ": " + value)
        curr += 1
    try:
        idx = int(input("Choose an index: "))
        return valueList[idx]
    except Exception as e:
        pass
    while True:
        try:
            idx = int(input("Index out of range! Try again: "))
            return valueList[idx]
        except Exception as e:
            pass

def getValueOfCategory(key: str, hashList: list[str]) -> str:
    valueMap = {}
    for hash in hashList:
        value = hashes.get(hash)
        if value != None:
            valueMap[value] = True
    noDuplicateValuesList = list(valueMap.keys())
    if len(noDuplicateValuesList) == 0:
        return ""
    elif len(noDuplicateValuesList) == 1:
        return noDuplicateValuesList[0]
    else:
        return manuallyResolve(key, noDuplicateValuesList)

def insertIntoMap(categoryHashMap: dict, key: str, hashList: list[str]) -> dict:
    value = getValueOfCategory(key, hashList)
    hashValueItem = {"HASHES" : hashList, "VALUE" : value}
    categoryHashMap[key] = hashValueItem
    return categoryHashMap

#########################################################################################################################################
## SPELL ################################################################################################################################
#########################################################################################################################################

spellSyntaxes = {
    #"SPELLNAME" : ["UI_TT_#SPELL_NAME"],
    "PROPERTY1" : ["UI_TT_#SPELL_PROPERTIES_1"],
    "PROPERTY2" : ["UI_TT_#SPELL_PROPERTIES_2"],
    "PROPERTY3" : ["UI_TT_#SPELL_PROPERTIES_3"],
    "PROPERTY4" : ["UI_TT_#SPELL_PROPERTIES_4"],
    "MOD1A" : ["UI_TT_#SPELL_MOD_1A"],
    "MOD1B" : ["UI_TT_#SPELL_MOD_1B"],
    "MOD2A" : ["UI_TT_#SPELL_MOD_2A"],
    "MOD2B" : ["UI_TT_#SPELL_MOD_2B"],
    "MOD3A" : ["UI_TT_#SPELL_MOD_3A"],
    "MOD3B" : ["UI_TT_#SPELL_MOD_3B"],
}

def getSpellCategoryHashMap(BPID: int, spells: list[str]) -> dict[str, list[str]]:
    # SPELL NAME
    categoryHashMap = {}
    nameList = []
    nameList.append(h.hashgen("BLUEPRINT_" + str(BPID)))
    for spell in spells:
        nameList.append(h.hashgen("UI_TT_" + str(spell) + "_NAME"))
    categoryHashMap = insertIntoMap(categoryHashMap, "SPELLNAME", nameList)

    # SPELL PROPERTIES & MODS
    for syntaxItem in spellSyntaxes.items():
        syntaxCategory = syntaxItem[0]
        syntaxList = syntaxItem[1]
        hashList = []
        for spell in spells:
            for syntax in syntaxList:
                hashList.append(h.hashgen(syntax.replace("#SPELL", spell)))
        categoryHashMap = insertIntoMap(categoryHashMap, syntaxCategory, hashList)
    
    return categoryHashMap

#########################################################################################################################################
## ASPECT ###############################################################################################################################
#########################################################################################################################################

hasNoLoreAspects = ["SE_COMBAT", "DR_HUNT", "SK_HEAVYCOMBAT", "SK_TACTICALCOMBAT", "IN_INQUISITION", "TW_CLOSECOMBAT"]
loreSyntaxes = {
    "LORE_NAME" : ["UI_TT_SKILL_#ASPECT_LORE_NAME", "UI_TT_SKILL_#ASPECT_LORE_NAME_CONSOLE"],
    "LORE_DESCRIPTION" : ["UI_TT_SKILL_#ASPECT_LORE_ATMO"],
    "LORE_MASTERY_NAME" : ["UI_TT_SKILL_#ASPECT_LORE_MASTERY_NAME", "UI_TT_SKILL_#ASPECT_LORE_MASTERY_NAME_CONSOLE"],
    "LORE_MASTERY_ATMO_SHORT" : ["UI_TT_SKILL_#ASPECT_LORE_MASTERY_ATMO_SHORT"],
    "LORE_MASTERY_ATMO_LONG" : ["UI_TT_SKILL_#ASPECT_LORE_MASTERY_ATMO_LONG"],
    "LORE_PROPERTIES_1" : ["UI_TT_SKILL_#ASPECT_LORE_PROPERTIES_1"],
    "LORE_PROPERTIES_2" : ["UI_TT_SKILL_#ASPECT_LORE_PROPERTIES_2"],
    "LORE_PROPERTIES_3" : ["UI_TT_SKILL_#ASPECT_LORE_PROPERTIES_3"],
    "LORE_PROPERTIES_MASTERY" : ["UI_TT_SKILL_#ASPECT_LORE_PROPERTIES_MASTERY"],
}
focusSyntaxes = {
    "FOCUS_NAME" : ["UI_TT_SKILL_#ASPECT_FOCUS_NAME", "UI_TT_SKILL_#ASPECT_FOCUS_NAME_CONSOLE"],
    "FOCUS_DESCRIPTION" : ["UI_TT_SKILL_#ASPECT_FOCUS_ATMO"],
    "FOCUS_MASTERY_NAME" : ["UI_TT_SKILL_#ASPECT_FOCUS_MASTERY_NAME", "UI_TT_SKILL_#ASPECT_FOCUS_MASTERY_NAME_CONSOLE"],
    "FOCUS_MASTERY_ATMO_SHORT" : ["UI_TT_SKILL_#ASPECT_FOCUS_MASTERY_ATMO_SHORT"],
    "FOCUS_MASTERY_ATMO_LONG" : ["UI_TT_SKILL_#ASPECT_FOCUS_MASTERY_ATMO_LONG"],
    "FOCUS_PROPERTIES_1" : ["UI_TT_SKILL_#ASPECT_FOCUS_PROPERTIES_1"],
    "FOCUS_PROPERTIES_2" : ["UI_TT_SKILL_#ASPECT_FOCUS_PROPERTIES_2"],
    "FOCUS_PROPERTIES_3" : ["UI_TT_SKILL_#ASPECT_FOCUS_PROPERTIES_3"],
    "FOCUS_PROPERTIES_MASTERY" : ["UI_TT_SKILL_#ASPECT_FOCUS_PROPERTIES_MASTERY"],
}

def getAspectCategoryHashMap(aspect: str) -> dict[str, list[str]]:
    categoryHashMap = {}

    # ASPECT NAME
    aspectnamelist = []
    if aspect != "SK_HEAVYCOMBAT":
        aspectnamelist.append(h.hashgen("EA_" + aspect))
    else:
        aspectnamelist.append(h.hashgen("EA_SK_HARDCOMBAT"))
    categoryHashMap = insertIntoMap(categoryHashMap, "ASPECTNAME", aspectnamelist)

    # SKILL ASPECT LORE
    if (not (aspect in hasNoLoreAspects)):
        for syntaxItem in loreSyntaxes.items():
            syntaxCategory = syntaxItem[0]
            syntaxList = syntaxItem[1]
            hashList = []
            for syntax in syntaxList:
                hashList.append(h.hashgen(syntax.replace("#ASPECT", aspect)))
            categoryHashMap = insertIntoMap(categoryHashMap, syntaxCategory, hashList)

    # SKILL ASPECT FOCUS
    for syntaxItem in focusSyntaxes.items():
        syntaxCategory = syntaxItem[0]
        syntaxList = syntaxItem[1]
        hashList = []
        for syntax in syntaxList:
            hashList.append(h.hashgen(syntax.replace("#ASPECT", aspect)))
        categoryHashMap = insertIntoMap(categoryHashMap, syntaxCategory, hashList)
    
    return categoryHashMap

#########################################################################################################################################
# HERO ##################################################################################################################################
#########################################################################################################################################

def getHeroCategoryHashMap(hero: str) -> dict[str, list[str]]:
    categoryHashMap = {}
    if hero != "INQUISITOR":
        descList = []
        descList.append(h.hashgen("UI_TT_ATMO_" + hero + "_GOOD"))
        categoryHashMap = insertIntoMap(categoryHashMap, "DESC_GOOD", descList)
    if hero != "SERAPHIM":
        descList = []
        descList.append(h.hashgen("UI_TT_ATMO_" + hero + "_BAD"))
        categoryHashMap = insertIntoMap(categoryHashMap, "DESC_BAD", descList)
    
    return categoryHashMap

#########################################################################################################################################
## EXPORT ###############################################################################################################################
#########################################################################################################################################

import os
import re
import json

def getPath(filename):
    base = os.path.abspath(__file__)
    base = re.split("\\\\", base)
    base.pop(len(base) - 1)
    result = ""
    for partialString in base:
        if partialString != "":
            result += partialString + "/"
    result += filename
    return result

def load(filepath):
    with open(getPath(filepath), "r", encoding = "utf-8") as file:
        file = "\n".join(file)
        return json.loads(str(file))

def save(filepath, content):
    with open(getPath(filepath), "w", encoding = "utf-8") as file:
        json.dump(content, file, indent = 4)

def export():
    heroes = {}
    for valuesItem in values.items():
        hero = valuesItem[0]
        aspectsMap = valuesItem[1]

        propertiesHero = getHeroCategoryHashMap(hero)
        aspects = []

        for item in aspectsMap.items():
            itemAspect = item[0]
            itemSpellsMap = item[1]

            propertiesAspect = getAspectCategoryHashMap(itemAspect)
            spells = []

            for itemSpells in itemSpellsMap.items():
                blueprintID = itemSpells[0]
                spellsList = itemSpells[1]

                spellCategoryHashMap = getSpellCategoryHashMap(blueprintID, spellsList)
                spells.append(spellCategoryHashMap)
            
            propertiesAspect["SPELLS"] = spells
            aspects.append(propertiesAspect)
        propertiesHero["ASPECTS"] = aspects
        heroes[hero] = propertiesHero
    save("res.json", heroes)

export()