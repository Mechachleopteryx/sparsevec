from sv_func import sparsevec, hash
from sv_index import index as _index

class SparseBigData:
    def __init__(self, filename, data_structure='sparsevec'):
        if data_structure == 'sparsevec':
            d, i = sparsevec(filename)
            self.data = {'data': d, 'index': i}
            self.sparsevec = d
            self.index = i
        elif data_structure == 'hash':
            self.hash = self.data = hash(filename)

    def __getitem__(self, i):
        return _index(i, self.data)

def test_SparseBigData():
    for representation in 'sparsevec', 'hash':
        d = SparseBigData('stream.dat', representation)
        assert d[6] == 3
        assert d[9] == 0



