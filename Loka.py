import _collections_abc as c

spells: dict[str, dict[str, list[str] | dict[int, list[str]]]] = {
    "SE" : {
        "CO" : {
            1402 : ["SE_CO_KAMPFHALTUNG",],
            1401 : ["SE_CO_BEFLUEGELN",],
            1404 : ["SE_CO_SEELENHAMMER",],
            1403 : ["SE_CO_SCHLAGHAGEL",],
            1405 : ["SE_CO_WIRBELSPRUNG",],
        },
        "CM" : {
            1399 : ["SE_CM_LICHTAURA",],
            1398 : ["SE_CM_HEILEN",],
            1396 : ["SE_CM_BEKEHRUNG",],
            1400 : ["SE_CM_LICHTSAEULE",],
            1397 : ["SE_CM_BLITZ",],
        },
        "TE" : {
            1406 : ["SE_TE_BEEEFFGEE",],
            1407 : ["SE_TE_ENERGIESCHILD",],
            1408 : ["SE_TE_NOTSCHILD",],
            1409 : ["SE_TE_SCHOCKWELLE",],
            1410 : ["SE_TE_SCHWERTFEUER",],
        },
    },
    "DR" : {
        "HU" : {
            1479 : ["DR_HU_PROJEKTILFOKUS",],
            1481 : ["DR_HU_WIRBELN",],
            1480 : ["DR_HU_SPRINT",],
            1477 : ["DR_HU_ANGRIFFSSERIE",],
            1478 : ["DR_HU_KONZENTRIERTERANGRIFF",],
        },
        "VO" : {
            1491 : ["DR_VO_ZOMBIE",],
            1489 : ["DR_VO_TOTEM",],
            1490 : ["DR_VO_VERDERBENSFLUCH",],
            1483 : ["DR_VO_KRANKHEIT",],
            1488 : ["DR_VO_QUAELEN",],
        },
        "NM" : {
            1485 : ["DR_NM_RINDENHAUT",],
            1482 : ["DR_NM_BODENSPIESSE",],
            1486 : ["DR_NM_WACHERVERSTAND",],
            1484 : ["DR_NM_HANDAUFLEGEN",],
            1487 : ["DR_NM_WUCHERWURZEL",],
        },
    },
    "SW" : {
        "HC" : {
            507 : ["SK_HC_BEFREIUNGSSCHLAG",],
            508 : ["SK_HC_HARTERSCHLAG",],
            509 : ["SK_HC_KAMPFRUF",],
            510 : ["SK_HC_RAMMSTOSS",],
            511 : ["SK_HC_WILLENSSTAERKE",],
        },
        "TC" : {
            373 : ["SK_TC_ATTACKE",],
            612 : ["SK_TC_KAMPFRAUSCH",],
            613 : ["SK_TC_SPRUNG",],
            614 : ["SK_TC_STANDARTE",],
            503 : ["SK_TC_UMLENKUNG",],
        },
        "AP" : {
            499 : ["SK_AP_GEISTERHAND",],
            501 : ["SK_AP_GEISTFORM", "SK_AP_GEISTFORM_BUFF",],
            502 : ["SK_AP_KAMPFBEFEHL",],
            504 : ["SK_AP_KOHORTE",],
            506 : ["SK_AP_UNTERSTUETZUNG",],
        },
    },
    "IN" : {
        "IN" : {
            803 : ["IN_IN_EIFER",],
            801 : ["IN_IN_HINRICHTUNG",],
            802 : ["IN_IN_KASTEIUNG",],
            800 : ["IN_IN_PRANGER",],
            804 : ["IN_IN_VERSTUEMMELUNG",],
        },
        "PO" : {
            809 : ["IN_PO_FAECHERBLITZ",],
            805 : ["IN_PO_MACHTSOG",],
            808 : ["IN_PO_MACHTSTOSS",],
            806 : ["IN_PO_VERGELTUNG",],
            807 : ["IN_PO_DOPPELGAENGER", "IN_PO_DOPPELGAENGER_BUFF",],
        },
        "UW" : {
            814 : ["IN_UW_SEELENFAENGER",],
            812 : ["IN_UW_ENTSETZEN",],
            813 : ["IN_UW_SCHAENDUNG",],
            810 : ["IN_UW_VERSKLAVUNG",],
            811 : ["IN_UW_SEELENRAUB",],
        },
    },
    "HE" : {
        "IN" : {
            819 : ["HE_IN_FEUERHAUT",],
            818 : ["HE_IN_FEUERDAEMON",],
            817 : ["HE_IN_METEOR",],
            816 : ["HE_IN_FEUERSTURM",],
            815 : ["HE_IN_FEUERBALL",],
        },
        "ST" : {
            827 : ["HE_ST_KRISTALLHAUT",],
            821 : ["HE_ST_NEBELFORM",],
            820 : ["HE_ST_SCHNEESTURM",],
            824 : ["HE_ST_FROSTSCHLAG",],
            823 : ["HE_ST_EISSPLITTER",],
        },
        "AR" : {
            829 : ["HE_AR_BANNKREIS",],
            825 : ["HE_AR_REGENERATIONSKRAFT",],
            822 : ["HE_AR_TELEPORT",],
            828 : ["HE_AR_ENERGIEBLITZ",],
            826 : ["HE_AR_MAGISCHERSCHLAG",],
        },
    },
    "TG" : {
        "CC" : {
            1466 : ["TW_CC_TKAMPFSCHILD",],
            1464 : ["TW_CC_KAMPFAURA", "TW_CC_KAMPFAURA_BUFF",],
            1467 : ["TW_CC_TODESSPIESSE",],
            1463 : ["TW_CC_KAMPFARM",],
            1465 : ["TW_CC_SCHOEPFUNGSSCHLAG",],
        },
        "TE" : {
            1798 : ["TW_TE_LEVITIEREN",],
            1473 : ["TW_TE_ARCHIMEDISSTRAHL",],
            1476 : ["TW_TE_TSCHOCK",],
            1474 : ["TW_TE_FLAMMENWERFER",],
            1475 : ["TW_TE_PROJEKTIL",],
        },
        "EN" : {
            1472 : ["TW_EN_SCHOCKPULSE",],
            1469 : ["TW_EN_ENERGIENETZ",],
            1468 : ["TW_EN_EISESKAELTE",],
            1470 : ["TW_EN_GLUTHITZE",],
            1471 : ["TW_EN_MUTIEREN",],
        },
    },
    "DM" : {
        "DM" : {
            3133 : ["DM_DM_VERTRAUTER",],
            3132 : ["DM_DM_DRACHENSCHLAG",],
            3131 : ["DM_DM_EWIGESFEUER",],
            3130 : ["DM_DM_BERSERKERFORM",],
            3129 : ["DM_DM_DRACHENFORM",],
        },
        "CO" : {
            3138 : ["DM_CO_BESCHUETZER",],
            3137 : ["DM_CO_ZERSTOERER",],
            3136 : ["DM_CO_MAGISCHERWALL",],
            3134 : ["DM_CO_WIRBELWIND",],
            3135 : ["DM_CO_WINDSTOSS",],
        },
        "ME" : {
            3143 : ["DM_ME_SCHUTZRUNEN",],
            3142 : ["DM_ME_KAMPFTRANCE",],
            3141 : ["DM_ME_MAHLSTROM",],
            3140 : ["DM_ME_ENERGIEBRAND",],
            3139 : ["DM_ME_GEDANKENSCHLAG",],
        },
        "FORM" : [
            "DM_FORM_TRAVEL_SPRUNG",
            "DM_FORM_ANY_RECALL",
            "DM_FORM_BRSRK_BLUTRAUSCH",
            "DM_FORM_BRSRK_ZERFETZEN",
            "DM_FORM_DRGN_TELEPORT",
            "DM_FORM_DRGN_FEUERBALL",
            "DM_FORM_DRGN_FEUERWAND",
        ],
    },
}

hashes = {}
f = open(file="decoded.txt", mode="r", encoding="utf-16")
for line in f:
    #print(line[0:10])
    #input()
    hashes[line[0:10]] = line[11:-1]
f.close()

import hashgen as h
def checkLokaID(LokaID: str):
    s = hashes.get(h.hashgen(LokaID))
    if (s == None):
        print(LokaID)
    else:
        #print(LokaID, s)
        pass

def checkSpellName(spellName: str) -> None:
    checkLokaID("UI_TT_" + spellName + "_NAME")
    checkLokaID("UI_TT_" + spellName + "_PROPERTIES_1")
    checkLokaID("UI_TT_" + spellName + "_PROPERTIES_2")
    checkLokaID("UI_TT_" + spellName + "_PROPERTIES_3")
    checkLokaID("UI_TT_" + spellName + "_PROPERTIES_4")
    checkLokaID("UI_TT_" + spellName + "_MOD_1A")
    checkLokaID("UI_TT_" + spellName + "_MOD_1B")
    checkLokaID("UI_TT_" + spellName + "_MOD_2A")
    checkLokaID("UI_TT_" + spellName + "_MOD_2B")
    checkLokaID("UI_TT_" + spellName + "_MOD_3A")
    checkLokaID("UI_TT_" + spellName + "_MOD_3B")

def checkRuneID(runeID: int) -> None:
    checkLokaID("BLUEPRINT_" + str(runeID))

for hero in spells.values():
    for aspect in hero.values():
        if type(aspect) == list:
            for spell in aspect:
                checkSpellName(spell)
        elif type(aspect) == dict:
            for spellItem in aspect.items():
                checkRuneID(spellItem[0])
                for spell in spellItem[1]:
                    checkSpellName(spell)

print(h.hashgen("UI_TT_HE_IN_FEUERBALL_PROPERTIES_4"))