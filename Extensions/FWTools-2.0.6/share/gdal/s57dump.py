#!/usr/bin/env python
#******************************************************************************
#  $Id: s57tables.py,v 1.1 2001/12/17 22:33:06 warmerda Exp $
# 
#  Project:  S-57 OGR Translator
#  Purpose:  Script to translate s57 .csv files into C code "data" statements.
#  Author:   Frank Warmerdam, warmerdam@pobox.com
# 
#******************************************************************************
#  Copyright (c) 2001, Frank Warmerdam
# 
#  Permission is hereby granted, free of charge, to any person obtaining a
#  copy of this software and associated documentation files (the "Software"),
#  to deal in the Software without restriction, including without limitation
#  the rights to use, copy, modify, merge, publish, distribute, sublicense,
#  and/or sell copies of the Software, and to permit persons to whom the
#  Software is furnished to do so, subject to the following conditions:
# 
#  The above copyright notice and this permission notice shall be included
#  in all copies or substantial portions of the Software.
# 
#  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS
#  OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#  FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL
#  THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#  LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
#  FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
#  DEALINGS IN THE SOFTWARE.
#******************************************************************************
# 
# $Log: s57tables.py,v $
# Revision 1.1  2001/12/17 22:33:06  warmerda
# New
#

import sys
import os
import string

def my_split( line ):
    n_start = 0
    while line[n_start] != ',':
        n_start = n_start+1

    n_start = n_start+1
    if line[n_start] == '"':
        n_start = n_start + 1
        n_end = n_start
        while line[n_end+1] != '"':
            n_end = n_end+1
        c_start = n_end + 3
    else:
        n_end = n_start
        while line[n_end+1] != ',':
            n_end = n_end+1
        c_start = n_end + 2

    c_end = c_start
    while line[c_end+1] != ',':
        c_end = c_end + 1

    return (line[n_start:n_end+1], line[c_start:c_end+1])
        

# -----------------------------------------------------------------------------
# 

if __name__ != '__main__':
    print 'This module should only be used as a mainline.'
    sys.exit( 1 )

if len(sys.argv) < 2:
    directory = os.environ['S57_CSV']
else:
    directory = sys.argv[1]

classes = open( directory + '/s57objectclasses.csv' ).readlines()

for line in classes:
    (name, code) = my_split( line )
    print code, name

    

