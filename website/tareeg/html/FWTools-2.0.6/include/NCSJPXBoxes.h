/********************************************************
** Copyright 2005 Earth Resource Mapping Ltd.
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
** FILE:     $Archive: /NCS/Source/include/NCSJP2File.h $
** CREATED:  03/03/2005
** AUTHOR:   Frank Warmerdam
** PURPOSE:  JPX related box definitions for inclusion in NCSJP2File.h
** EDITS:    [xx] ddMmmyy NAME COMMENTS
 *******************************************************/

#define ECW_FW

/**
 * CNCSJPXAssocBox class - JPX Association box, superbox for associating
 *  subboxes. May be several present.
 * 
 * @author       Frank Warmerdam
 */	

class NCSJPC_EXPORT_ALL CNCSJPXAssocBox: public CNCSJP2SuperBox {
public:

    /** Box Type */
    static UINT32	sm_nTBox;

    /** Default contructor, initialises members */
    CNCSJPXAssocBox();

    /** Virtual destructor */
    virtual ~CNCSJPXAssocBox();
};

/**
 * CNCSJPXLabelBox class - Label box for identifying an 
 * AssocBox.
 * 
 * @author       Frank Warmerdam
 */	

class NCSJPC_EXPORT_ALL CNCSJPXLabelBox: public CNCSJP2Box {
public:
			
    /** Box type */
    static UINT32	sm_nTBox;

    /** Label text */
    char                *m_pLabel;

    /** Default constructor, initialises members */
    CNCSJPXLabelBox();

    /** Virtual destructor */
    virtual ~CNCSJPXLabelBox();

    /**
     * Set label contents. 
     *
     * @param    Label label text. 
     * @return CNCSError NCS_SUCCESS, or an error code.
     */
    CNCSError         SetLabel( const char * Label);

    /** 
     * Parse the label box.
     * @param		JP2File		JP2 file being parsed
     * @param		Stream		IOStream to use to parse file.
     * @return      CNCSError	NCS_SUCCESS, or Error code on failure.
     */
    virtual CNCSError Parse(class CNCSJP2File &JP2File, CNCSJPCIOStream &Stream);

    /**
     * UnParse the Data Entry label box to the JP2 file.
     * @param		JP2File		JP2 file being parsed
     * @param		Stream		IOStream to use to parse file.
     * @return      CNCSError	NCS_SUCCESS, or Error code on failure.
     */
    virtual CNCSError UnParse(class CNCSJP2File &JP2File, CNCSJPCIOStream &Stream);

    virtual void UpdateXLBox(void);
};
