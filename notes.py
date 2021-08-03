notesFlats = ['C', 'Db', 'D', 'Eb', 'E', 'F', 'Gb', 'G', 'Ab', 'A', 'Bb', 'B']
notesSharps = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']

steps = {
    'ST': 1,
    'T': 2,
    'T+ST': 3,
    '2T': 4,
    '2T+ST': 5
}

scale_formulas = {
    'major-scale': [0, steps['T'], steps['T'], steps['ST'], steps['T'], steps['T'], steps['T'], steps['ST']],
    'minor-natural-scale': [0, steps['T'], steps['ST'], steps['T'], steps['T'], steps['ST'], steps['T'], steps['T']],
    'minor-harmonic-scale': [0, steps['T'], steps['ST'], steps['T'], steps['T'], steps['ST'], steps['T+ST'], steps['ST']],
    'minor-melodic-scale': [0, steps['T'], steps['ST'], steps['T'], steps['T'], steps['T'], steps['T'], steps['ST'], -steps['T'], -steps['T'], -steps['ST'], -steps['T'], -steps['T'], -steps['ST'], -steps['T']],
    'minor-pentatonic-scale': [0, steps['T+ST'], steps['T'], steps['T'], steps['T+ST'], steps['T']]
}

chord_formulas = {
    'major-chords': [0, steps['2T'], steps['T+ST']],
    'minor-chords': [0, steps['T+ST'], steps['2T']],
    'augmented-chords': [0, steps['2T'], steps['2T']],
    'diminished-chords': [0, steps['T+ST'], steps['T+ST']],
    'suspended2-chords': [0, steps['T'], steps['2T+ST']],
    'suspended4-chords': [0, steps['2T+ST'], steps['T']],
    'major-seventh-chords': [0, steps['2T'], steps['T+ST'], steps['2T']],
    'minor-seventh-chords': [0, steps['T+ST'], steps['2T'], steps['T+ST']],
    'dominant-seventh-chords': [0, steps['2T'], steps['T+ST'], steps['T+ST']]
}

def preprocess(root):
    note_list = notesSharps
    accidental = ''
    if len(root) > 1:
        accidental = root[1]
        if accidental == '#':
            note_list = notesSharps
        elif accidental == 'b':
            note_list = notesFlats

    return note_list.index(root), note_list

