spells: dict[str, dict[str, list[str]]] = {
    "SE" : {
        "CO" : [
            "SE_CO_KAMPFHALTUNG",
            "SE_CO_BEFLUEGELN",
            "SE_CO_SEELENHAMMER",
            "SE_CO_SCHLAGHAGEL",
            "SE_CO_WIRBELSPRUNG",
        ],
        "CM" : [
            "SE_CM_LICHTAURA",
            "SE_CM_HEILEN",
            "SE_CM_BEKEHRUNG",
            "SE_CM_LICHTSAEULE",
            "SE_CM_BLITZ",
        ],
        "TE" : [
            "SE_TE_BEEEFFGEE",
            "SE_TE_ENERGIESCHILD",
            "SE_TE_NOTSCHILD",
            "SE_TE_SCHOCKWELLE",
            "SE_TE_SCHWERTFEUER",
        ]
    },
    "DR" : {
        "HU" : [
            "DR_HU_PROJEKTILFOKUS",
            "DR_HU_WIRBELN",
            "DR_HU_SPRINT",
            "DR_HU_ANGRIFFSSERIE",
            "DR_HU_KONZENTRIERTERANGRIFF",
        ],
        "VO" : [
            "DR_VO_ZOMBIE",
            "DR_VO_TOTEM",
            "DR_VO_VERDERBENSFLUCH",
            "DR_VO_KRANKHEIT",
            "DR_VO_QUAELEN",
        ],
        "NM" : [
            "DR_NM_RINDENHAUT",
            "DR_NM_BODENSPIESSE",
            "DR_NM_WACHERVERSTAND",
            "DR_NM_HANDAUFLEGEN",
            "DR_NM_WUCHERWURZEL",
        ],
    },
    "SW" : {
        "HC" : [
            "SK_HC_BEFREIUNGSSCHLAG",
            "SK_HC_HARTERSCHLAG",
            "SK_HC_KAMPFRUF",
            "SK_HC_RAMMSTOSS",
            "SK_HC_WILLENSSTAERKE",
        ],
        "TC" : [
            "SK_TC_ATTACKE",
            "SK_TC_KAMPFRAUSCH",
            "SK_TC_SPRUNG",
            "SK_TC_STANDARTE",
            "SK_TC_UMLENKUNG",
        ],
        "AP" : [
            "SK_AP_GEISTERHAND",
            "SK_AP_GEISTFORM",
            "SK_AP_GEISTFORM_BUFF",
            "SK_AP_KAMPFBEFEHL",
            "SK_AP_KOHORTE",
            "SK_AP_UNTERSTUETZUNG",
        ],
    },
    "IN" : {
        "IN" : [
            "IN_IN_EIFER",
            "IN_IN_HINRICHTUNG",
            "IN_IN_KASTEIUNG",
            "IN_IN_PRANGER",
            "IN_IN_VERSTUEMMELUNG",
        ],
        "PO" : [
            "IN_PO_FAECHERBLITZ",
            "IN_PO_MACHTSOG",
            "IN_PO_MACHTSTOSS",
            "IN_PO_VERGELTUNG",
            "IN_PO_DOPPELGAENGER_BUFF",
            "IN_PO_DOPPELGAENGER",
        ],
        "UW" : [
            "IN_UW_SEELENFAENGER",
            "IN_UW_ENTSETZEN",
            "IN_UW_SCHAENDUNG",
            "IN_UW_VERSKLAVUNG",
            "IN_UW_SEELENRAUB",
        ],
    },
    "HE" : {
        "IN" : [
            "HE_IN_FEUERHAUT",
            "HE_IN_FEUERDAEMON",
            "HE_IN_METEOR",
            "HE_IN_FEUERSTURM",
            "HE_IN_FEUERBALL",
        ],
        "ST" : [
            "HE_ST_KRISTALLHAUT",
            "HE_ST_NEBELFORM",
            "HE_ST_SCHNEESTURM",
            "HE_ST_FROSTSCHLAG",
            "HE_ST_EISSPLITTER",
        ],
        "AR" : [
            "HE_AR_BANNKREIS",
            "HE_AR_REGENERATIONSKRAFT",
            "HE_AR_TELEPORT",
            "HE_AR_ENERGIEBLITZ",
            "HE_AR_MAGISCHERSCHLAG",
        ],
    },
    "TG" : {
        "CC" : [
            "TW_CC_TKAMPFSCHILD",
            "TW_CC_KAMPFAURA_BUFF",
            "TW_CC_KAMPFAURA",
            "TW_CC_TODESSPIESSE",
            "TW_CC_KAMPFARM",
            "TW_CC_SCHOEPFUNGSSCHLAG",
        ],
        "TE" : [
            "TW_TE_LEVITIEREN",
            "TW_TE_ARCHIMEDISSTRAHL",
            "TW_TE_TSCHOCK",
            "TW_TE_FLAMMENWERFER",
            "TW_TE_PROJEKTIL",
        ],
        "EN" : [
            "TW_EN_SCHOCKPULSE",
            "TW_EN_ENERGIENETZ",
            "TW_EN_EISESKAELTE",
            "TW_EN_GLUTHITZE",
            "TW_EN_MUTIEREN",
        ],
    },
    "DM" : {
        "DM" : [
            "DM_DM_VERTRAUTER",
            "DM_DM_DRACHENSCHLAG",
            "DM_DM_EWIGESFEUER",
            "DM_DM_BERSERKERFORM",
            "DM_DM_DRACHENFORM",
        ],
        "CO" : [
            "DM_CO_BESCHUETZER",
            "DM_CO_ZERSTOERER",
            "DM_CO_MAGISCHERWALL",
            "DM_CO_WIRBELWIND",
            "DM_CO_WINDSTOSS",
        ],
        "ME" : [
            "DM_ME_SCHUTZRUNEN",
            "DM_ME_KAMPFTRANCE",
            "DM_ME_MAHLSTROM",
            "DM_ME_ENERGIEBRAND",
            "DM_ME_GEDANKENSCHLAG",
        ],
        "FORM" : [
            "DM_FORM_TRAVEL_SPRUNG",
            "DM_FORM_ANY_RECALL",
            "DM_FORM_BRSRK_BLUTRAUSCH",
            "DM_FORM_BRSRK_ZERFETZEN",
            "DM_FORM_DRGN_TELEPORT",
            "DM_FORM_DRGN_FEUERBALL",
            "DM_FORM_DRGN_FEUERWAND",
        ]
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
for hero in spells.values():
  for aspect in hero.values():
    for spell in aspect:
      hash = h.hashgen("UI_TT_" + spell + "_NAME")
      v = hashes.get(hash)
      if v == None:
        print(spell)
    else:
      print(v)