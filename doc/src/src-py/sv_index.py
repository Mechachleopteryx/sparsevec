def index(i, data):
    # Assume data is hash
    if len(data) == 2:
        # Sparse vector representation
        try:
            data_index = data['index'].index(i)
            return data['data'][data_index]
        except ValueError:
            return 0
    else:
        # Hash representation
        return data.get(i, 0)

def test_index():
    from sv_func import sparsevec, hash, sparsevec_index, hash_index
    d, i = sparsevec('stream.dat')
    data_hash = hash('stream.dat')
    data = {'data': d, 'index': i}
    # Check one data item in the compressed structure and one zero
    assert sparsevec_index(3, d, i) == index(3, d)
    assert hash_index(3, data_hash) == index(3, data_hash)
    assert sparsevec_index(9, d, i) == index(9, d)
    assert hash_index(9, data_hash) == index(9, data_hash)
