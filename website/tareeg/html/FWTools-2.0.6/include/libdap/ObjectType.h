
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
 
#ifndef _object_type_h
#define _object_type_h

/** When a version 2.x or greater DAP data server sends an object, it uses
    the Content-Description header of the response to indicate the type of
    object contained in the response. During the parse of the header a member
    of Connect is set to one of these values so that other mfuncs can tell
    the type of object without parsing the stream themselves.

    <pre>
     enum ObjectType {
       unknown_type,
       dods_das,
       dods_dds,
       dods_data,
       dods_error,
       web_error
     };
     </pre>

    @brief The type of object in the stream coming from the data
    server.  */

enum ObjectType {
    unknown_type,
    dods_das,
    dods_dds,
    dods_data,
    dods_error,
    web_error
};

#endif
