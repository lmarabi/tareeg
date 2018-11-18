
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
 
#ifndef _httpconnect_h
#define _httpconnect_h


#include <stdio.h>

#include <string>

#include <curl/curl.h>
#include <curl/types.h>
#include <curl/easy.h>

#ifndef _rc_reader_h_
#include "RCReader.h"
#endif

#ifndef _object_type_h
#include "ObjectType.h"
#endif

#ifndef _http_cache_h
#include "HTTPCache.h"
#endif

#ifndef http_response_h
#include "HTTPResponse.h"
#endif

#ifndef _util_h
#include "util.h"
#endif

using std::string;
#if defined(_MSC_VER) && (_MSC_VER == 1200)  //  VC++ 6.0 only
using std::vector<string>;
#else
using std::vector;
#endif

// This is defined in Connect.cc. ObjectType should be its own class.
// 6/17/2002 jhrg
extern ObjectType get_type(const string &value);

/** Use the CURL library to dereference a HTTP URL. Scan the response for
    headers used by the DAP 2.0 and extract their values. The body of the
    response is made available by a FILE pointer.

    @todo Change the way this class returns information so that the headers
    and the stream (aka FILE pointer) are returned using an object. Design
    this object so that its destructor closes the stream (this will prevent
    resource leaks). It will also obviate the need for the (now broken)
    is_response_present() predicate.

    @author jhrg */

class HTTPConnect {
private:
    CURL *d_curl;
    RCReader *d_rcr;
    HTTPCache *d_http_cache;

    char d_error_buffer[CURL_ERROR_SIZE]; // A human-readable message.

    bool d_accept_deflate;

    string d_username;		// extracted from URL
    string d_password;		// extracted from URL
    string d_upstring;		// used to pass info into curl

    vector<string> d_request_headers; // Request headers

    void www_lib_init() throw(Error, InternalErr);
    long read_url(const string &url, FILE *stream, vector<string> *resp_hdrs,
		  const vector<string> *headers = 0) throw(Error);
    // string get_temp_file(FILE *&stream) throw(InternalErr);
    HTTPResponse *plain_fetch_url(const string &url) 
	throw(Error, InternalErr);
    HTTPResponse *caching_fetch_url(const string &url) 
	throw(Error, InternalErr);

    bool url_uses_proxy_for(const string &url) throw();
    bool url_uses_no_proxy_for(const string &url) throw();

    void extract_auth_info(string &url);

    // bool cond_fetch_url(const string &url, const vector<string> &headers);

    friend size_t save_raw_http_header(void *ptr, size_t size, size_t nmemb, 
				       void *http_connect);
    friend class HTTPConnectTest;
    friend class ParseHeader;

protected:
    /** @name Suppress default methods
	These methods are not supported and are implmented here as protected
	methods to suppress the C++-supplied default versions (which will
	break this object). */
    //@{
    HTTPConnect() { }
    HTTPConnect(const HTTPConnect &) { }
    HTTPConnect &operator=(const HTTPConnect &) { 
	throw InternalErr(__FILE__, __LINE__, "Unimplemented assignment");
    }
    //@}

public:
    HTTPConnect(RCReader *rcr) throw(Error, InternalErr);

    virtual ~HTTPConnect();

    void set_credentials(const string &u, const string &p) throw(InternalErr);
    void set_accept_deflate(bool defalte);

    /** Set the state of the HTTP cache. By default, the HTTP cache is
	enabled of disabled using the value of the \c USE_CACHE property in
	the \c .dodsrc file. Use this method to set the state from within a
	program. 
	@param enabled True to use the cache, False to disable. */
    void set_cache_enabled(bool enabled) { 
	if (d_http_cache)
	    d_http_cache->set_cache_enabled(enabled);
    }

    /** Return the current state of the HTTP cache. */
    bool is_cache_enabled() { 
	return (d_http_cache) ? d_http_cache->is_cache_enabled() : false; 
    }

    HTTPResponse *fetch_url(const string &url) throw(Error, InternalErr);
};

#endif // _httpconnect_h
