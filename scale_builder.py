from notes import scale_formulas, preprocess

def major_scale(start, note_list):
    formula = scale_formulas['major-scale']
    result = []

    for i in range(len(formula)):
        result.append(note_list[(start + formula[i]) % len(note_list)])
        start += formula[i]

    return result

def minor_natural_scale(start, note_list):
    formula = scale_formulas['minor-natural-scale']
    result = []

    for i in range(len(formula)):
        result.append(note_list[(start + formula[i]) % len(note_list)])
        start += formula[i]

    return result

def minor_harmonic_scale(start, note_list):
    formula = scale_formulas['minor-harmonic-scale']
    result = []

    for i in range(len(formula)):
        result.append(note_list[(start + formula[i]) % len(note_list)])
        start += formula[i]

    return result

def minor_melodic_scale(start, note_list):
    formula = scale_formulas['minor-melodic-scale']
    result = []

    for i in range(len(formula)):
        result.append(note_list[(start + formula[i]) % len(note_list)])
        start += formula[i]

    return result

def minor_pentatonic_scale(start, note_list):
    formula = scale_formulas['minor-pentatonic-scale']
    result = []

    for i in range(len(formula)):
        result.append(note_list[(start + formula[i]) % len(note_list)])
        start += formula[i]

    return result

scales = {
    'major-scale': major_scale,
    'minor-natural-scale': minor_natural_scale,
    'minor-harmonic-scale': minor_harmonic_scale,
    'minor-melodic-scale': minor_melodic_scale,
    'minor-pentatonic-scale': minor_pentatonic_scale
}

def process(scale, root):
    start, note_list = preprocess(root)

    return scales.get(scale)(start, note_list)





