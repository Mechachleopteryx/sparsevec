from sv_func import sparsevec, hash
from sv_index import index as _index

data = {}  # hash for the data structure as used by _index function

def load(filename, data_structure='sparsevec'):
    global data
    if data_structure == 'sparsevec':
        d, i = sparsevec(filename)
        data = {'data': d, 'index': i}
    elif data_structure == 'hash':
        data = hash(filename)

def index(i):
    return _index(i, data)

def test_index():
    for representation in 'sparsevec', 'hash':
        load('stream.dat', representation)
        assert index(6) == 3
        assert index(9) == 0

def main():
    # Example from the exercise
    load('stream.dat')
    print index(10), index(11)
    load('stream.dat', 'hash')
    print index(10), index(11)

if __name__ == '__main__':
    main()
