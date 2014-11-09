
// -*- mode: c++; c-basic-offset:4 -*-

// This file is part of libdap, A C++ implementation of the OPeNDAP Data
// Access Protocol.

// Copyright (c) 2002,2003 OPeNDAP, Inc.
// Author: James Gallagher <jgallagher@opendap.org>
//
// This library is free software; you can redistribute it and/or
// modify it under the terms of the GNU Lesser General Public
// License as published by the Free Software Foundation; either
// version 2.1 of the License, or (at your option) any later version.
// 
// This library is distributed in the hope that it will be useful,
// but WITHOUT ANY WARRANTY; without even the implied warranty of
// MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
// Lesser General Public License for more details.
// 
// You should have received a copy of the GNU Lesser General Public
// License along with this library; if not, write to the Free Software
// Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA
//
// You can contact OPeNDAP, Inc. at PO Box 112, Saunderstown, RI. 02874-0112.
 
// (c) COPYRIGHT URI/MIT 1995-1999
// Please read the full copyright statement in the file COPYRIGHT_URI.
//
// Authors:
//      jhrg,jimg       James Gallagher <jgallagher@gso.uri.edu>

// This is the interface definition file for the abstract class
// Vector. Vector is the parent class for List and Array.

#ifndef _vector_h
#define _vector_h 1


#ifdef WIN32
#include <rpc.h>
#include <winsock2.h>
#else
#include <rpc/types.h>
#include <netinet/in.h>
#include <rpc/xdr.h>
#endif

#ifndef _basetype_h
#include "BaseType.h"
#endif

#ifndef _dds_h
#include "DDS.h"
#endif

/** Holds a one-dimensional array of DAP2 data types.  This class
    takes two forms, depending on whether the elements of the vector
    are themselves simple or compound objects. This class contains
    common functionality for the List and Array classes, and should
    rarely be used directly.

    When each element of the class is a simple data type, the Vector
    is implemented as a simple array of C types, rather than as an
    array of BaseType data types.  A single private ``template''
    BaseType instance (<tt>_var</tt>) is used to hold information in common
    to all the members of the array.  The template is also used as a
    container to pass values back and forth to an application
    program, as in <tt>var()</tt>.

    If the elements of the vector are themselves compound data
    types, the array is stored as a vector of BaseType pointers (see
    the libdap class <b>BaseTypePtrVec</b>). The template is still used to
    hold information in common to all the members of the array, but
    is not used to pass information to and from the application
    program. 

    @brief Holds a one-dimensional collection of DAP2 data types.  
    @see BaseType 
    @see Array
*/
class Vector: public BaseType {
private:
    int _length;		// number of elements in the vector
    BaseType *_var;		// base type of the Vector

    // _buf was a pointer to void; delete[] complained. 6/4/2001 jhrg
    char *_buf;			// array which holds cardinal data
    vector<string> d_str;        // special storage for strings. jhrg 2/11/05
    vector<BaseType *> _vec;	// array for other data

protected:
    // This function copies the private members of Vector.
    void _duplicate(const Vector &v);

public:
    Vector(const string &n = "", BaseType *v = 0, const Type &t = dods_null_c);
    Vector(const Vector &rhs);

    virtual ~Vector();

    Vector &operator=(const Vector &rhs);
    virtual BaseType *ptr_duplicate() = 0; 

    virtual int element_count(bool leaves);

    virtual void set_send_p(bool state); 

    virtual void set_read_p(bool state);

    virtual unsigned int width();

    virtual int length();

    virtual void set_length(int l);

    virtual bool serialize(const string &dataset, DDS &dds, XDR *sink,
			   bool ce_eval = true);
    virtual bool deserialize(XDR *source, DDS *dds, bool reuse = false);

    virtual unsigned int val2buf(void *val, bool reuse = false);

    virtual unsigned int buf2val(void **val);

    void set_vec(unsigned int i, BaseType *val);

    void vec_resize(int l);

    virtual BaseType *var(const string &name = "", bool exact_match = true,
              btp_stack *s = 0);

    virtual BaseType *var(const string &name, btp_stack &s);

    virtual BaseType *var(unsigned int i);

    virtual void add_var(BaseType *v, Part p = nil);

    virtual bool check_semantics(string &msg, bool all = false);
};

#endif /* _vector_h */
