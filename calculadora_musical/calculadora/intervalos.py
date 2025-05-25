

dicionario = {
    "c": 1, "C": 1, "c#": 2, "C#": 2, "D": 3, "d": 3,  "D#": 4, "d#": 4, "e": 5, "E": 5, "F": 6, "f": 6, "f#": 7, "F#": 7, "g": 8, "G": 8, "g#": 9, "G#": 9, "A": 10, "a": 10, "A#": 11, "a#": 11,
    "B": 12, "b": 12, "db": 2, "Db": 2, "Eb": 4, "eb": 4, "Gb": 7, "gb": 7, "Ab": 9, "ab": 9, "Bb": 11, "bb": 11
}

dicionario2 = {
    1: "C", 2: "C#", 3: "D", 4: "D#", 5: "E", 6: "F", 7: "F#", 8: "G", 9: "G#", 10: "A", 11: "A#", 12: "B"
}


def traduzir_numero(x):
    nota1 = dicionario[x]
    return nota1


def tonica(x):
    nota1 = dicionario[x]
    return dicionario2[nota1]


def segundamenor(x):
    nota1 = dicionario[x]
    nota2 = nota1+1
    if nota2 > 12:
        nota3 = nota2-12
        return dicionario2[nota3]
    return dicionario2[nota2]


def segundamaior(x):
    nota1 = dicionario[x]
    nota2 = nota1+2
    if nota2 > 12:
        nota3 = nota2-12
        return dicionario2[nota3]
    return dicionario2[nota2]


def tercamenor(x):
    nota1 = dicionario[x]
    nota2 = nota1+3
    if nota2 > 12:
        nota3 = nota2-12
        return dicionario2[nota3]
    return dicionario2[nota2]


def tercamaior(x):
    nota1 = dicionario[x]
    nota2 = nota1+4
    if nota2 > 12:
        nota3 = nota2-12
        return dicionario2[nota3]
    return dicionario2[nota2]


def quartajusta(x):
    nota1 = dicionario[x]
    nota2 = nota1+5
    if nota2 > 12:
        nota3 = nota2-12
        return dicionario2[nota3]
    return dicionario2[nota2]


def quintadiminuta(x):
    nota1 = dicionario[x]
    nota2 = nota1+6
    if nota2 > 12:
        nota3 = nota2-12
        return dicionario2[nota3]
    return dicionario2[nota2]


def quintajusta(x):
    nota1 = dicionario[x]
    nota2 = nota1+7
    if nota2 > 12:
        nota3 = nota2-12
        return dicionario2[nota3]
    return dicionario2[nota2]


def sextamenor(x):
    nota1 = dicionario[x]
    nota2 = nota1+8
    if nota2 > 12:
        nota3 = nota2-12
        return dicionario2[nota3]
    return dicionario2[nota2]


def sextamaior(x):
    nota1 = dicionario[x]
    nota2 = nota1+9
    if nota2 > 12:
        nota3 = nota2-12
        return dicionario2[nota3]
    return dicionario2[nota2]


def setimamenor(x):
    nota1 = dicionario[x]
    nota2 = nota1+10
    if nota2 > 12:
        nota3 = nota2-12
        return dicionario2[nota3]
    return dicionario2[nota2]


def setimamaior(x):
    nota1 = dicionario[x]
    nota2 = nota1+11
    if nota2 > 12:
        nota3 = nota2-12
        return dicionario2[nota3]
    return dicionario2[nota2]
