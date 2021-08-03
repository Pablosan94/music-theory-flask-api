from notes import chord_formulas, preprocess

def major_chords(start, note_list):
    formula = chord_formulas['major-chords']
    result = []

    for i in range(len(formula)):
        result.append(note_list[(start + formula[i]) % len(note_list)])
        start += formula[i]

    return result

def minor_chords(start, note_list):
    formula = chord_formulas['minor-chords']
    result = []

    for i in range(len(formula)):
        result.append(note_list[(start + formula[i]) % len(note_list)])
        start += formula[i]

    return result

def augmented_chords(start, note_list):
    formula = chord_formulas['augmented-chords']
    result = []

    for i in range(len(formula)):
        result.append(note_list[(start + formula[i]) % len(note_list)])
        start += formula[i]

    return result

def diminished_chords(start, note_list):
    formula = chord_formulas['diminished-chords']
    result = []

    for i in range(len(formula)):
        result.append(note_list[(start + formula[i]) % len(note_list)])
        start += formula[i]

    return result

def suspended2_chords(start, note_list):
    formula = chord_formulas['suspended2-chords']
    result = []

    for i in range(len(formula)):
        result.append(note_list[(start + formula[i]) % len(note_list)])
        start += formula[i]

    return result

def suspended4_chords(start, note_list):
    formula = chord_formulas['suspended4-chords']
    result = []

    for i in range(len(formula)):
        result.append(note_list[(start + formula[i]) % len(note_list)])
        start += formula[i]

    return result

def major_seventh_chords(start, note_list):
    formula = chord_formulas['major-seventh-chords']
    result = []

    for i in range(len(formula)):
        result.append(note_list[(start + formula[i]) % len(note_list)])
        start += formula[i]

    return result

def minor_seventh_chords(start, note_list):
    formula = chord_formulas['minor-seventh-chords']
    result = []

    for i in range(len(formula)):
        result.append(note_list[(start + formula[i]) % len(note_list)])
        start += formula[i]

    return result

def dominant_seventh_chords(start, note_list):
    formula = chord_formulas['dominant-seventh-chords']
    result = []

    for i in range(len(formula)):
        result.append(note_list[(start + formula[i]) % len(note_list)])
        start += formula[i]

    return result

chords = {
    'major-chords': major_chords,
    'minor-chords': minor_chords,
    'augmented-chords': augmented_chords,
    'diminished-chords': diminished_chords,
    'suspended2-chords': suspended2_chords,
    'suspended4-chords': suspended4_chords,
    'major-seventh-chords': major_seventh_chords,
    'minor-seventh-chords': minor_seventh_chords,
    'dominant-seventh-chords': dominant_seventh_chords
}

def process(chord, root):
    start, note_list = preprocess(root)

    return chords.get(chord)(start, note_list)