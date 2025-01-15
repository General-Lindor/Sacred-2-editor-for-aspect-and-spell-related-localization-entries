# Sacred 2 Aspects & Spells ressources Editor

## Description

This is a Sacred 2 Modding tool for allowing to quickly edit all the hash-value-entries in a decoded global.res file that are in some way related to aspects / spells.

global.res is part of the localization for i18n and defines all the text strings that are displayed somewhere ingame. It's heavily encrypted, using Huffman-Coding and Hash-Functions, but there exists a tool made by Pesmontis to edit it, S2rw.exe.

This tool aims to be a quality-of-life complementary to the usage of S2rw.exe.

## Requirements

- Desktop OS (Unix Based (e.g. Linux), Windows or macOS)
- Python 3.x Interpreter
- If you want to use the results you need S2rw.exe

## Usage

#### Editing

You don't edit the entries for each hash directly, instead hashes that should have the same value (like e.g. spell name and rune name) are grouped together into categories.
The Editing is straightforward.
The BASE (default) values come from PFP.

#### Saving

Any valid changes you make get instantly saved in your RAM.
These changes are preserved on changing the selected parameter like language, hero, aspect or spell.
They are however not preserved in-between sessions. For that you need to manually click the save button.

#### Exporting

This tool exports ALL possible hashes that are in some way related to aspects / spells, even those without an entry.
If you delete an entry, the hash-value-pair is still exported (with an empty value).
This way you can keep track of the values that you deleted.

It does NOT export a full decoded.txt, it ONLY exports hash-value-pairs that are in some way related to aspects / spells.

The format is the same as S2rw.exe exports to, UTF-16LE-BOM with the syntax HASH - TAB - VALUE for each entry.

So in general, you need to manually insert the exported ressources into your global.res files using S2rw.exe or you can use my [other global.res tool](https://github.com/General-Lindor/global.res) for that.

## Support

Currently only de_DE and en_EN languages are supported.
However you can easily extend the support itself by using the 'scripts/\_\_GEN\_\_/Loka.py' tool to convert a decoded global.res named decoded.txt into a valid res.json file.
You can then move the res.json into a folder inside ressources/BASE/yourlanguage and copy it into MODIFIED as well.
