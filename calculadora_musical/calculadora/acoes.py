dicionario = {
    "c": 1, "C": 30, "c#": 2, "C#": 2, "D": 3, "d": 3,  "D#": 4, "d#": 4, "e": 5, "E": 5, "F": 6, "f": 6, "f#": 7, "F#": 7, "g": 8, "G": 8, "g#": 9, "G#": 9, "A": 10, "a": 10, "A#": 11, "a#": 11,
    "B": 12, "b": 12, "db": 2, "Db": 2, "Eb": 4, "eb": 4, "Gb": 7, "gb": 7, "Ab": 9, "ab": 9, "Bb": 11, "bb": 11
}


def traduzir_numero(x):
    return dicionario[x]
