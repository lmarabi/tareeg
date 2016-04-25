
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

#ifndef response_h
#define response_h

#include <stdio.h>

#ifndef _debug_h
#include "debug.h"
#endif

using namespace std;

/** Encapsulate a response. Instead of directly returning the FILE pointer
    from which a response is read, return an instance of this object. For a
    simple system where all that needs to be done to free the stream and its
    associated resources, this is overkill. However, some streams may require
    complex operations to free their resources once the client is done with
    the stream. Those classes should return a subclass of Response
    which has those operations built into the destructor. 
    
    @todo If the code that parses the MIME headers was moved from Connect and
    HTTPConnect to this class and its children, it would be easier to build
    a FileConnect class (or maybe the specifics of the connection type could
    be held in the Response object and HTTPConnect and the to be written 
    FileConnect would not be needed). */
class Response {
private:
    /// The data stream
    FILE *d_stream;
    /// Response object type
    ObjectType d_type;
    /// Server version
    string d_version;
    /// The DAP server's protocol
    string d_protocol;
    /// The HTTP response code
    int d_status;

protected:
    /** @name Suppressed default methods */
    //@{
    Response() {}
    Response(const Response &) {}
    Response &operator=(const Response &) {
	throw InternalErr(__FILE__, __LINE__, "Unimplemented assignment");
    }
    //@}

public:
    /** Initialize with a stream. Create an instance initialized to a stream.
	by default get_type() and get_version() return default values of
	unknown_type and "dods/0.0", respectively. Specializations (see
	HTTPResponse and HTTPConnect) may fill these fields in with other
	values. */
    Response(FILE *s) : d_stream(s), d_type(unknown_type), 
			d_version("dods/0.0"), d_protocol("2.0"), 
                        d_status(0) { }

    /** Close the stream. */
    virtual ~Response() { 
        if (d_stream)
	    fclose(d_stream); 
    }

    /** @name Accessors */
    //@{
    virtual int get_status() const { return d_status; }
    virtual FILE *get_stream() const { return d_stream; }
    virtual ObjectType get_type() const { return d_type; }
    virtual string get_version() const { return d_version; }
    virtual string get_protocol() const { return d_protocol; }
    //@}

    /** @name Mutators */
    //@{
    virtual void set_status(int s) { d_status = s; }
    virtual void set_stream(FILE *s) { d_stream = s; }
    virtual void set_type(ObjectType o) { d_type = o; }
    virtual void set_version(const string &v) { d_version = v; }
    virtual void set_protocol(const string &p) { d_protocol = p; }
    //@}
};

#endif // response_h
