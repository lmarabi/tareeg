/**********************************************************************
 * $Id: Envelope.inl 1820 2006-09-06 16:54:23Z mloskot $
 *
 * GEOS - Geometry Engine Open Source
 * http://geos.refractions.net
 *
 * Copyright (C) 2005-2006 Refractions Research Inc.
 *
 * This is free software; you can redistribute and/or modify it under
 * the terms of the GNU Lesser General Public Licence as published
 * by the Free Software Foundation. 
 * See the COPYING file for more information.
 *
 **********************************************************************/

#ifndef GEOS_GEOM_ENVELOPE_INL
#define GEOS_GEOM_ENVELOPE_INL

#include <cassert>
#include <geos/geom/Coordinate.h>
#include <geos/geom/Envelope.h>

namespace geos {
namespace geom { // geos::geom

/*public*/
INLINE double
Envelope::getMaxY() const { return maxy; }

/*public*/
INLINE double
Envelope::getMaxX() const { return maxx; }

/*public*/
INLINE double
Envelope::getMinY() const { return miny; }

/*public*/
INLINE double
Envelope::getMinX() const { return minx; }

/*public*/
INLINE bool
Envelope::intersects(const Coordinate& other) const
{
	return (other.x <= maxx && other.x >= minx &&
		other.y <= maxy && other.y >= miny);
}

/*public*/
INLINE bool
Envelope::intersects(const Envelope& other) const
{
	return intersects(&other);
}

/*public*/
INLINE bool
Envelope::isNull(void) const
{
	return maxx < minx;
}

/*public*/
INLINE bool
Envelope::intersects(const Envelope* other) const
{
	// Optimized to reduce function calls
	if ( isNull() || other->isNull() ) return false;
	return !(other->minx > maxx ||
			 other->maxx < minx ||
			 other->miny > maxy ||
			 other->maxy < miny);
}

/*public*/
INLINE bool
Envelope::intersects(double x, double y) const
{
	return (x <= maxx && x >= minx && y <= maxy && y >= miny);
}

} // namespace geos::geom
} // namespace geos

#endif // GEOS_GEOM_ENVELOPE_INL

