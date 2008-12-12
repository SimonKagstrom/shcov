def read_file(name):
    f = open(name)
    out = f.read()
    f.close()
    return out
