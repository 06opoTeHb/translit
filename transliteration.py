"""
Transliteration module

The module provides function to convert strings given from cyrillic
(e.g. Russian) to latin (English) and back.
The 'GOST' standard refers to Russian GOST 7.79-2000 (System B) which
is equivalent to ISO 9-95.
The 'RADIO' standard refers to Morse code table, so there are few
cyrillic letters that don't have relevant latin letter (e.g. "Ч", "Ш",
"Э", "Ю", "Я").
The 'ICAO' standard based on ICAO Doc 9303 and supposed to be used
only in one direction, from cyrillic to latin.
NOTE: Only 'GOST' standard supports capability to convert in both
directions without misrepresentation.
"""

import lingua as lng


def transliterate(line: str, reverse=False, standard='GOST', language='ru'):
    if reverse:
        _inverse(line, standard, language)
    else:
        _direct(line, standard, language)


def _direct(line: str, standard='GOST', language='ru'):
    new_line = []
    for word in line.split(' '):
        wrd = []
        for ltr in word:
            if ltr.upper() in lng.STANDARDS[language][standard]:
                wrd.append(lng.STANDARDS[language][standard][ltr.upper()])
            else:
                wrd.append(ltr)
        wrd = ''.join(wrd)
        if word.isupper():
            new_line.append(wrd.upper())
        elif word.islower():
            new_line.append(wrd.lower())
        elif word.istitle():
            new_line.append(wrd.capitalize())
        else:
            new_line.append(wrd)
    new_line = ' '.join(new_line)
    return new_line


def _inverse(line: str, standard='GOST', language='ru'):
    new_line = []
    for word in line.split(' '):
        wrd = []
        word_ = word
        if standard == 'GOST':
            word_ = word_.upper().replace('SHH', 'Щ')
            word_ = word_.upper().replace('YA', 'Я')
            word_ = word_.upper().replace('YO', 'Ё')
            word_ = word_.upper().replace('YU', 'Ю')
            word_ = word_.upper().replace('YA', 'Я')
            word_ = word_.upper().replace('E`', 'Э')
            word_ = word_.upper().replace('``', 'Ъ')
            word_ = word_.upper().replace('`', 'Ь')
        elif standard == 'ICAO':
            word_ = word_.upper().replace('SHCH', 'Щ')
            word_ = word_.upper().replace('KH', 'Х')
            word_ = word_.upper().replace('TS', 'Ц')
            word_ = word_.upper().replace('IE', 'Ъ')
            word_ = word_.upper().replace('IU', 'Ю')
            word_ = word_.upper().replace('IA', 'Я')
        if standard == 'GOST' or standard == 'ICAO':
            word_ = word_.upper().replace('SH', 'Ш')
            word_ = word_.upper().replace('ZH', 'Ж')
            word_ = word_.upper().replace('CH', 'Ч')
        for ltr in word_:
            if ltr.upper() in lng.STANDARDS_INV[language][standard]:
                wrd.append(lng.STANDARDS_INV[language][standard][ltr.upper()])
            else:
                wrd.append(ltr)
        wrd = ''.join(wrd)
        if word.isupper():
            new_line.append(wrd.upper())
        elif word.islower():
            new_line.append(wrd.lower())
        elif word.istitle():
            new_line.append(wrd.capitalize())
        else:
            new_line.append(wrd)
    new_line = ' '.join(new_line)
    return new_line


def languages(reverse=False):
    if reverse:
        return repr(*lng.STANDARDS_INV.keys())
    else:
        return repr(*lng.STANDARDS.keys())
