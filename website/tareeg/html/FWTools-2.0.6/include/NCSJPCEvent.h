/********************************************************
** Copyright 2002 Earth Resource Mapping Ltd.
** This document contains proprietary source code of
** Earth Resource Mapping Ltd, and can only be used under
** one of the three licenses as described in the 
** license.txt file supplied with this distribution. 
** See separate license.txt file for license details 
** and conditions.
**
** This software is covered by US patent #6,442,298,
** #6,102,897 and #6,633,688.  Rights to use these patents 
** is included in the license agreements.
**
** FILE:     $Archive: /NCS/Source/include/NCSJPCEvent.h $
** CREATED:  05/12/2002 3:27:34 PM
** AUTHOR:   Simon Cope
** PURPOSE:  NCSJPCEvent class
** EDITS:    [xx] ddMmmyy NAME COMMENTS
 *******************************************************/

#ifndef NCSJPCEVENT_H
#define NCSJPCEVENT_H

#ifndef NCSJPCTYPES_H
#include "NCSJPCTypes.h"
#endif // NCSJPCTYPES_H

// Segment class
class NCSJPC_EXPORT_ALL CNCSJPCEvent {
public:
	CNCSJPCEvent(bool bManualReset = false, bool bInitialState = false, char *pLockName = NULL);
	virtual ~CNCSJPCEvent();
	bool Set();
	bool Reset();
	bool Wait(NCSTimeStampMs tsTimeout = -1);

private:
#ifdef WIN32
	HANDLE m_hEvent;
#else
	bool m_bManualReset;
	char *m_pLockName;
	CNCSMutex m_Mutex;
	bool m_bSignalled;
#endif
};

#endif // NCSJPCEVENT_H
