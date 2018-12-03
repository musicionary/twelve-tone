class Matrix:
    def __init__(self):
        self._tones = [
            'Ab', 'A', 'A#',
            'Bb', 'B',
            'Cb', 'C', 'C#',
            'Db', 'D', 'D#',
            'Eb', 'E',
            'Fb', 'F', 'F#',
            'Gb', 'G', 'G#',
        ]

        self._enharmonics = {
            'Ab': ['G#'],
            'A': ['G##', 'Bbb'],
            'A#': ['Bb', 'Cbb'],
            'Bb': ['A#', 'Cbb'],
            'B': ['A##', 'Cb'],
            'B#': ['C', 'Dbb'],
            'Cb': ['A##', 'B'],
            'C': ['B#', 'Dbb'],
            'C#': ['B##', 'Db'],
            'Db': ['B##', 'C#'],
            'D': ['C##', 'Ebb'],
            'D#': ['Eb', 'Fbb'],
            'Eb': ['D#', 'Fbb'],
            'E': ['D##', 'Fb'],
            'E#': ['Fb', 'Gbb'],
            'Fb': ['D##', 'E'],
            'F': ['E#', 'Gbb'],
            'F#': ['E##', 'Gb'],
            'Gb': ['E##', 'F#'],
            'G': ['F##', 'Abb'],
            'G#': ['Ab']
        }
