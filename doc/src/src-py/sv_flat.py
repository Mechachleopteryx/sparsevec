datafile = open('stream.dat', 'r')
data = []
index = []
data_hash = {}
counter = 0
for line in datafile:
    for word in line.split():    # split line into words
        number = float(word)
        if abs(number) > 1E-15:  # use tolerance to compare to 0
            data.append(number)
            index.append(counter)
            data_hash[counter] = number
            counter += 1

# Dump data structures to files with extensions
# .svv (sparse vector, vector representation) and
# .svh (sparse vector, hash representation)
# Use repr(object) to turn object to a string that
# can later be read into a string s and coverted back
# to the object via eval(s).

outfile = open('stream.svv', 'w')
outfile.write(repr(data) + '\n')
outfile.write(repr(index) + '\n')
outfile.close()

outfile = open('stream.svh', 'w')
outfile.write(repr(data_hash) + '\n')
outfile.close()

# Test of program
reference = {'data_hash':
             {1: 1.1, 2: 3, 6: 5.1, 7: -2, 10: 4, 12: 2, 15: 1},
             'data':
             [1.1,  3,  5.1,  -2,  4,  2,  1],
             'index':
             [1, 2, 6, 7, 10, 12, 15]}
assert index == reference['index']
assert data == reference['data']
assert data_hash == reference['data_hash']
