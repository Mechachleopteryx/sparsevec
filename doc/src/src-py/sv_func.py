def sparsevec(filename, outname=None):
    datafile = open(filename, 'r')
    data = []
    index = []
    counter = 0
    for line in datafile:
        for word in line.split():    # split line into words
            number = float(word)
            if abs(number) > 1E-15:  # use tolerance to compare to 0
                data.append(number)
                index.append(counter)
                counter += 1

    if outname is not None:
        outfile = open(filename[:-3] + 'spv', 'w')
        outfile.write(repr(data) + '\n')
        outfile.write(repr(index) + '\n')
        outfile.close()
    return data, index

def hash(filename, outname=None):
    datafile = open(filename, 'r')
    data_hash = {}
    counter = 0
    for line in datafile:
        for word in line.split():    # split line into words
            number = float(word)
            if abs(number) > 1E-15:  # use tolerance to compare to 0
                data_hash[counter] = number
                counter += 1

    if outname is not None:
        outfile = open(filename[:-3] + 'spv', 'w')
        outfile.write(repr(data_hash) + '\n')
        outfile.close()
    return data_hash

def sparsevec_index(i, data, index):
    try:
        data_index = index.index(i)
        return dta[data_index]
    except ValueError:
        return 0

def hash_index(i, data_hash):
    return data_hash.get(i, 0)

def test_sparsevec():
    # Test for data in stream.dat
    data_ref = [1.1,  3,  5.1,  -2,  4,  2,  1]
    index_ref = [1, 2, 6, 7, 10, 12, 15]
    sparsevec('stream.dat', 'stream.svv')
    f = open('stream.svv', 'r')
    data = eval(f.readline())
    index = eval(f.readline())
    f.close()
    assert data == data_ref
    assert index = index_ref
    # Test indexing too
    assert sparsevec_index(6, data, index) == 3
    assert sparsevec_index(9, data, index) == 0

def test_hash():
    # Test for data in stream.dat
    data_hash_ref = {1: 1.1, 2: 3, 6: 5.1, 7: -2, 10: 4, 12: 2, 15: 1}
    hash('stream.dat', 'stream.svh')
    f = open('stream.svh', 'r')
    data_hash = eval(f.readline())
    f.close()
    assert data_hash == data_hash_ref
    # Test indexing too
    assert hash_index(6, data_hash) == 3
    assert hash_index(9, data_hash) == 0

# "Main program" in function
def main():
    data, index = sparsevec('stream.dat', 'stream.svv')
    data_hash = hash('stream.dat', 'stream.svh')

if __name__ == '__main__':
    main()



data = datafile.read()  # string of numbers
numbers = data.split()  # split wrt whitespace; result: list of strings
numbers = [float(n) for n in numbers]  # convert strings to floats
