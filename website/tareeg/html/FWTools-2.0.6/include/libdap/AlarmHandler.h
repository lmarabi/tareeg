
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
 
#ifndef alarm_handler_h
#define alarm_handler_h

#include <stdio.h>

#include <string>

#include "EventHandler.h"

/** Handle the time out alarm. When an OPeNDAP server runs until the time out
    alarm is triggered, this class provides the concrete implementation of
    EventHandler::handle_signal(). 
    
    @see EventHandler
    @see SignalHandler
    @author James Gallagher <jgallagher@opendap.org> */
class AlarmHandler : public EventHandler {
private:
    FILE *d_stream;		// Sink for the Error object.
    string d_version;

    // Ensure that d_stream gets initialized...
    AlarmHandler() {}

public:
    /** Store information to be used by the handler.
	@param s Write to this stream. */
    AlarmHandler(FILE *s) : d_stream(s) {}
    
    virtual ~AlarmHandler() {
	fclose(d_stream);
    }

    /** Handle an alarm signal. When one of our servers gets an alarm, that
	means it has hit its time out. We need to dump two CRLF pairs down
	the stream and then send an Error object explaining that a timeout
	has been reached. 

	Because this is a signal handler, it should call only reentrant
	system services, functions, et cetera. Generally that eliminates
	stdio functions but I'm using them anyway. This handler never returns
	to the code that was running when the alarm signal was raised.

	@param signum We know it is SIGALRM; here as a check 
	@return Never returns; calls exit after sending the Error object. */
    virtual void handle_signal(int signum) {
	if (signum != SIGALRM)
	    fprintf(stderr, "SIGALRM handler caught another signal!\n");
#if 0
	// Use this code, or a variant, once we have reliable error delivery.
	fprintf(d_stream, "\n\n\n\n");
	Error e("The server has timed out. This happens when a request\n\
takes longer to process than the server's preset time-out value.\n\
Try making a request for a smaller amount of data. You can also contact\n\
the server's administrator and request that the time-out value be increased.");
	e.print(d_stream);
#endif
	exit(1);
    }

};

#endif
