######################################################################
##
## Copyright (C) 2008,  Simon Kagstrom
##
## Filename:      shcov_file.py
## Author:        Simon Kagstrom <simon.kagstrom@gmail.com>
## Description:   The shcov file class
##
## $Id:$
##
######################################################################
import pickle, md5, os

from shcov_utils import *

class File:
    def __init__(self, path):
	self.path = path
	self.basename = os.path.basename(path)
	self.lines = {}

	m = md5.new()
	m.update(read_file(path))

	self.digest = m.digest()

    def save(self, path):
	outfile = open(path, 'wb')

	pickle.dump(self, outfile)
	outfile.close()

    def add_to_line(self, line_nr):
	line_nr = int(line_nr)
	try:
	    self.lines[line_nr] = self.lines[line_nr] + 1
	except KeyError, e:
	    self.lines[line_nr] = 1


def load(path):
    file = pickle.load(open(path))
    source_file = read_file(file.path)

    m = md5.new()
    m.update(source_file)
    digest = m.digest()

    # File has changed
    if digest != file.digest:
	file = File(file.path)
    return file
