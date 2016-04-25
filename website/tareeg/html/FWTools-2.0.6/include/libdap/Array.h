
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
 
// (c) COPYRIGHT URI/MIT 1994-1999
// Please read the full copyright statement in the file COPYRIGHT_URI.
//
// Authors:
//      jhrg,jimg       James Gallagher <jgallagher@gso.uri.edu>

// Class for array variables. The dimensions of the array are stored in the
// list SHAPE. 
//
// jhrg 9/6/94

#ifndef _array_h
#define _array_h 1


#include <string>

#include <vector>

#ifndef _dods_limits_h
#include "dods-limits.h"
#endif

#ifndef _vector_h
#include "Vector.h"
#endif

const int DODS_MAX_ARRAY = DODS_INT_MAX;

/** This class is used to hold arrays of data. The elements of the array can
    be simple or compound data types. There is no limit on the number of
    dimensions an array can have, or on the size of each dimension.

    If desired, the user can give each dimension of an array a name. You can,
    for example, have a 360x180 array of temperatures, covering the whole
    globe with one-degree squares. In this case, you could name the first
    dimension \e Longitude and the second dimension \e Latitude. This can
    help prevent a great deal of confusion.

    The Array is used as part of the Grid class, where the dimension names
    are crucial to its structure. The dimension names correspond to \e Map
    vectors, holding the actual values for that column of the array.

    Each array dimension carries with it its own projection information. The
    projection inforamtion takes the form of three integers: the start, stop,
    and stride values. This is clearest with an example. Consider a
    one-dimensional array 10 elements long. If the start value of the
    dimension constraint is 3, then the constrained array appears to be seven
    elements long. If the stop value is changed to 7, then the array appears
    to be five elements long. If the stride is changed to two, the array will
    appear to be 3 elements long. Array constraints are written as:
    <b>[start:stride:stop]</b>.

    \verbatim
    A = [1 2 3 4 5 6 7 8 9 10]

    A[3::] = [4 5 6 7 8 9 10]

    A[3::7] = [4 5 6 7 8]

    A[3:2:7] = [4 6 8]

    A[0:3:9] = [1 4 7 10]
    \endverbatim

    @note Arrays use zero-based indexing.

    @brief A multidimensional array of identical data types.
    @see Grid
    @see Vector
    @see dimension */

class Array: public Vector {
public:
    /** Information about a dimension. Each Array has one or more dimensions.
	For each of an Array's dimensions, a cooresponding instance of this
	struct holds the natural size, name, constraint information and
	constrained size.

        @note Instead of using this struct's fileds directly, use Array's
        dimension accessor methods.

        @note This sturct is public because its type is used in public
        typedefs. */
    struct dimension {
    	int size;		///< The unconstrained dimension size.
    	string name;    ///< The name of this dimension.
    	int start;		///< The constriant start index
    	int stop;		///< The constraint end index
    	int stride;		///< The constraint stride
    	int c_size;		///< Size of dimension once constrained
    	bool selected;	///< \c True if a constraint has been applied to this dimension.
    };

private:
    std::vector<dimension> _shape;	// list of dimensions (i.e., the shape)
    unsigned int print_array(FILE *out, unsigned int index, 
			     unsigned int dims, unsigned int shape[]);

    friend class ArrayTest;
    		     
protected:
    void _duplicate(const Array &a);
    void print_xml_core(FILE *out, string space, bool constrained, string tag);

public:
    /** A constant iterator used to access the various dimensions of an
	Array. 

        @see dim_begin()
	@see dim_end() */
    typedef std::vector<dimension>::const_iterator Dim_citer ;
    /** An iterator used to access the various dimensions of an
	Array. Most of the methods that access various properties of a
	dimension use an instance of Dim_iter.

        @see dim_begin()
	@see dim_end() */
    typedef std::vector<dimension>::iterator Dim_iter ;

    Array(const string &n = "", BaseType *v = 0);
    Array(const Array &rhs);
    virtual ~Array();

    Array &operator=(const Array &rhs);
    virtual BaseType *ptr_duplicate();

    void add_var(BaseType *v, Part p = nil);
    
    void update_length(int size);

    void append_dim(int size, string name = "");

    void add_constraint(Dim_iter i, int start, int stride, int stop);
    void reset_constraint();

    void clear_constraint();

    Dim_iter dim_begin() ;
    Dim_iter dim_end() ;

    int dimension_size(Dim_iter i, bool constrained = false);
    int dimension_start(Dim_iter i, bool constrained = false);
    int dimension_stop(Dim_iter i, bool constrained = false);
    int dimension_stride(Dim_iter i, bool constrained = false);
    string dimension_name(Dim_iter i);

    unsigned int dimensions(bool constrained = false);

    virtual void print_decl(FILE *out, string space = "    ",
			    bool print_semi = true,
			    bool constraint_info = false,
			    bool constrained = false);

    virtual void print_xml(FILE *out, string space = "    ",
			   bool constrained = false);

    virtual void print_as_map_xml(FILE *out, string space = "    ",
				  bool constrained = false);

    virtual void print_val(FILE *out, string space = "", 
			   bool print_decl_p = true);

    virtual bool check_semantics(string &msg, bool all = false);
};

#endif // _array_h
