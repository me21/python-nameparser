# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import re

# emoji regex from https://stackoverflow.com/questions/26568722/remove-unicode-emoji-using-re-in-python
try:
    # Wide UCS-4 build
    re_emoji = re.compile('['
        '\U0001F300-\U0001F64F'
        '\U0001F680-\U0001F6FF'
        '\u2600-\u26FF\u2700-\u27BF]+',
        re.UNICODE)
except re.error:
    # Narrow UCS-2 build
    re_emoji = re.compile('('
        '\ud83c[\udf00-\udfff]|'
        '\ud83d[\udc00-\ude4f\ude80-\udeff]|'
        '[\u2600-\u26FF\u2700-\u27BF])+',
        re.UNICODE)

REGEXES = set([
    ("spaces", re.compile(r"\s+", re.U)),
    ("word", re.compile(r"(\w|\.)+", re.U)),
    ("mac", re.compile(r'^(ma?c)(\w{2,})', re.I | re.U)),
    ("initial", re.compile(r'^(\w\.|[A-Z])?$', re.U)),
    ("quoted_word", re.compile(r'(?<!\w)\'([^\s]*?)\'(?!\w)', re.U)),
    ("double_quotes", re.compile(r'\"(.*?)\"', re.U)),
    ("parenthesis", re.compile(r'\((.*?)\)', re.U)),
    ("roman_numeral", re.compile(r'^(X|IX|IV|V?I{0,3})$', re.I | re.U)),
    ("no_vowels",re.compile(r'^[^aeyiuo]+$', re.I | re.U)),
    ("period_not_at_end",re.compile(r'.*\..+$', re.I | re.U)),
    ("emoji",re_emoji),
    ("phd", re.compile(r'\s(ph\.?\s+d\.?)', re.I | re.U)),
    ("russian_last_name_endings", re.compile(r'^.+(ov|ova|ev|eva|yov|yova|in|yn|ina|sky|skaya|ich|ych|uk|yuk|yk|ko|ak|ukh|ykh|ikh|chuk|yy|yi|oy|oi|iy|ii)$', re.I | re.U)),
    ("russian_last_name_endings_cyrillic", re.compile(r'^.+(ов|ова|ев|ева|ёв|ёва|ин|ын|ина|ский|ская|цкая|цкий|ич|ыч|ук|юк|ык|ко|ак|ух|ых|их|чук|ый|ой|ий)$', re.I | re.U)),
    ("russian_patronymic_endings", re.compile(r'^(.+(ovich|ovna|evich|evna|ichna))|(ilyich|kuzmich|lukich|fomich)$', re.I | re.U)),
    ("russian_patronymic_endings_cyrillic", re.compile(r'^(.+(ович|овна|евич|евна|ична))|(ильич|кузьмич|лукич|фомич)$', re.I | re.U)),
    ("turkic_patronymic_suffixes", re.compile(r'^(oglu|ogly|qizi|kizi|kyzy|gyzy|uly|uulu)$', re.I | re.U)),
    ("turkic_patronymic_suffixes_cyrillic", re.compile(r'^(оглу|оглы|кызы|гызы|улы|уулу)$', re.I | re.U)),
])
"""
All regular expressions used by the parser are precompiled and stored in the config.
"""
