from bacteria.actions import Actions

code = {
    25: Actions.heat_resistance,
    27: Actions.photosynthesis,
    49: Actions.cold_resistance
}


def proc(bact, dna: int):
    if dna in list(code.keys()):
        return code[dna](bact)
    return dna
