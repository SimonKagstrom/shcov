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

from utils import *

class File:
    def __init__(self, path, source_path = None):
	self.path = path
        if source_path == None:
            self.source_path = path
        else:
            self.source_path = source_path
	self.basename = os.path.basename(path)
	self.lines = {}

	m = md5.new()
	m.update(read_file(self.source_path))

	self.digest = m.digest()

    def set_source_path(self, path):
        self.source_path = path

    def get_source_path(self):
        return self.source_path

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


def load(path, script_base = ''):
    file = pickle.load(open(path))
    source_file = read_file(script_base + file.path)

    m = md5.new()
    m.update(source_file)
    digest = m.digest()

    # File has changed
    if digest != file.digest:
	file = File(file.path, source_path = script_base + file.path)

    file.set_source_path(script_base + file.path)
    return file
