# This file was created automatically by SWIG.
# Don't modify this file, modify the SWIG interface instead.

import _mapscript

class intarray(object):
    def __repr__(self):
        return "<C intarray instance at %s>" % (self.this,)
    def __init__(self, *args):
        newobj = _mapscript.new_intarray(*args)
        self.this = newobj.this
        self.thisown = 1
        del newobj.thisown
    def __del__(self, destroy=_mapscript.delete_intarray):
        try:
            if self.thisown: destroy(self)
        except: pass
    def __getitem__(*args): return _mapscript.intarray___getitem__(*args)
    def __setitem__(*args): return _mapscript.intarray___setitem__(*args)
    def cast(*args): return _mapscript.intarray_cast(*args)
    frompointer = staticmethod(_mapscript.intarray_frompointer)

class intarrayPtr(intarray):
    def __init__(self, this):
        self.this = this
        if not hasattr(self,"thisown"): self.thisown = 0
        self.__class__ = intarray
_mapscript.intarray_swigregister(intarrayPtr)

intarray_frompointer = _mapscript.intarray_frompointer

MapServerError = _mapscript.MapServerError
MapServerChildError = _mapscript.MapServerChildError

MS_VERSION = _mapscript.MS_VERSION
MS_TRUE = _mapscript.MS_TRUE
MS_FALSE = _mapscript.MS_FALSE
MS_ON = _mapscript.MS_ON
MS_OFF = _mapscript.MS_OFF
MS_DEFAULT = _mapscript.MS_DEFAULT
MS_EMBED = _mapscript.MS_EMBED
MS_DELETE = _mapscript.MS_DELETE
MS_YES = _mapscript.MS_YES
MS_NO = _mapscript.MS_NO
MS_SINGLE = _mapscript.MS_SINGLE
MS_MULTIPLE = _mapscript.MS_MULTIPLE
MS_GD_ALPHA = _mapscript.MS_GD_ALPHA
MS_LAYER_ALLOCSIZE = _mapscript.MS_LAYER_ALLOCSIZE
MS_CLASS_ALLOCSIZE = _mapscript.MS_CLASS_ALLOCSIZE
MS_STYLE_ALLOCSIZE = _mapscript.MS_STYLE_ALLOCSIZE
MS_MAX_LABEL_PRIORITY = _mapscript.MS_MAX_LABEL_PRIORITY
MS_DEFAULT_LABEL_PRIORITY = _mapscript.MS_DEFAULT_LABEL_PRIORITY
MS_FILE_MAP = _mapscript.MS_FILE_MAP
MS_FILE_SYMBOL = _mapscript.MS_FILE_SYMBOL
MS_INCHES = _mapscript.MS_INCHES
MS_FEET = _mapscript.MS_FEET
MS_MILES = _mapscript.MS_MILES
MS_METERS = _mapscript.MS_METERS
MS_KILOMETERS = _mapscript.MS_KILOMETERS
MS_DD = _mapscript.MS_DD
MS_PIXELS = _mapscript.MS_PIXELS
MS_PERCENTAGES = _mapscript.MS_PERCENTAGES
MS_SHAPE_POINT = _mapscript.MS_SHAPE_POINT
MS_SHAPE_LINE = _mapscript.MS_SHAPE_LINE
MS_SHAPE_POLYGON = _mapscript.MS_SHAPE_POLYGON
MS_SHAPE_NULL = _mapscript.MS_SHAPE_NULL
MS_LAYER_POINT = _mapscript.MS_LAYER_POINT
MS_LAYER_LINE = _mapscript.MS_LAYER_LINE
MS_LAYER_POLYGON = _mapscript.MS_LAYER_POLYGON
MS_LAYER_RASTER = _mapscript.MS_LAYER_RASTER
MS_LAYER_ANNOTATION = _mapscript.MS_LAYER_ANNOTATION
MS_LAYER_QUERY = _mapscript.MS_LAYER_QUERY
MS_LAYER_CIRCLE = _mapscript.MS_LAYER_CIRCLE
MS_LAYER_TILEINDEX = _mapscript.MS_LAYER_TILEINDEX
MS_LAYER_CHART = _mapscript.MS_LAYER_CHART
MS_TRUETYPE = _mapscript.MS_TRUETYPE
MS_BITMAP = _mapscript.MS_BITMAP
MS_POSITIONS_LENGTH = _mapscript.MS_POSITIONS_LENGTH
MS_UL = _mapscript.MS_UL
MS_LR = _mapscript.MS_LR
MS_UR = _mapscript.MS_UR
MS_LL = _mapscript.MS_LL
MS_CR = _mapscript.MS_CR
MS_CL = _mapscript.MS_CL
MS_UC = _mapscript.MS_UC
MS_LC = _mapscript.MS_LC
MS_CC = _mapscript.MS_CC
MS_AUTO = _mapscript.MS_AUTO
MS_XY = _mapscript.MS_XY
MS_FOLLOW = _mapscript.MS_FOLLOW
MS_TINY = _mapscript.MS_TINY
MS_SMALL = _mapscript.MS_SMALL
MS_MEDIUM = _mapscript.MS_MEDIUM
MS_LARGE = _mapscript.MS_LARGE
MS_GIANT = _mapscript.MS_GIANT
MS_NORMAL = _mapscript.MS_NORMAL
MS_HILITE = _mapscript.MS_HILITE
MS_SELECTED = _mapscript.MS_SELECTED
MS_INLINE = _mapscript.MS_INLINE
MS_SHAPEFILE = _mapscript.MS_SHAPEFILE
MS_TILED_SHAPEFILE = _mapscript.MS_TILED_SHAPEFILE
MS_SDE = _mapscript.MS_SDE
MS_OGR = _mapscript.MS_OGR
MS_UNUSED_1 = _mapscript.MS_UNUSED_1
MS_POSTGIS = _mapscript.MS_POSTGIS
MS_WMS = _mapscript.MS_WMS
MS_ORACLESPATIAL = _mapscript.MS_ORACLESPATIAL
MS_WFS = _mapscript.MS_WFS
MS_GRATICULE = _mapscript.MS_GRATICULE
MS_MYGIS = _mapscript.MS_MYGIS
MS_RASTER = _mapscript.MS_RASTER
MS_PLUGIN = _mapscript.MS_PLUGIN
MS_DB_XBASE = _mapscript.MS_DB_XBASE
MS_DB_CSV = _mapscript.MS_DB_CSV
MS_DB_MYSQL = _mapscript.MS_DB_MYSQL
MS_DB_ORACLE = _mapscript.MS_DB_ORACLE
MS_DB_POSTGRES = _mapscript.MS_DB_POSTGRES
MS_JOIN_ONE_TO_ONE = _mapscript.MS_JOIN_ONE_TO_ONE
MS_JOIN_ONE_TO_MANY = _mapscript.MS_JOIN_ONE_TO_MANY
MS_ALIGN_LEFT = _mapscript.MS_ALIGN_LEFT
MS_ALIGN_CENTER = _mapscript.MS_ALIGN_CENTER
MS_ALIGN_RIGHT = _mapscript.MS_ALIGN_RIGHT
MS_CJC_NONE = _mapscript.MS_CJC_NONE
MS_CJC_BEVEL = _mapscript.MS_CJC_BEVEL
MS_CJC_BUTT = _mapscript.MS_CJC_BUTT
MS_CJC_MITER = _mapscript.MS_CJC_MITER
MS_CJC_ROUND = _mapscript.MS_CJC_ROUND
MS_CJC_SQUARE = _mapscript.MS_CJC_SQUARE
MS_CJC_TRIANGLE = _mapscript.MS_CJC_TRIANGLE
MS_SUCCESS = _mapscript.MS_SUCCESS
MS_FAILURE = _mapscript.MS_FAILURE
MS_DONE = _mapscript.MS_DONE
MS_IMAGEMODE_PC256 = _mapscript.MS_IMAGEMODE_PC256
MS_IMAGEMODE_RGB = _mapscript.MS_IMAGEMODE_RGB
MS_IMAGEMODE_RGBA = _mapscript.MS_IMAGEMODE_RGBA
MS_IMAGEMODE_INT16 = _mapscript.MS_IMAGEMODE_INT16
MS_IMAGEMODE_FLOAT32 = _mapscript.MS_IMAGEMODE_FLOAT32
MS_IMAGEMODE_BYTE = _mapscript.MS_IMAGEMODE_BYTE
MS_IMAGEMODE_NULL = _mapscript.MS_IMAGEMODE_NULL
MS_GEOS_EQUALS = _mapscript.MS_GEOS_EQUALS
MS_GEOS_DISJOINT = _mapscript.MS_GEOS_DISJOINT
MS_GEOS_TOUCHES = _mapscript.MS_GEOS_TOUCHES
MS_GEOS_OVERLAPS = _mapscript.MS_GEOS_OVERLAPS
MS_GEOS_CROSSES = _mapscript.MS_GEOS_CROSSES
MS_GEOS_INTERSECTS = _mapscript.MS_GEOS_INTERSECTS
MS_GEOS_WITHIN = _mapscript.MS_GEOS_WITHIN
MS_GEOS_CONTAINS = _mapscript.MS_GEOS_CONTAINS
MS_GEOS_BEYOND = _mapscript.MS_GEOS_BEYOND
class fontSetObj(object):
    def __repr__(self):
        return "<C fontSetObj instance at %s>" % (self.this,)
    filename = property(_mapscript.fontSetObj_filename_get)
    numfonts = property(_mapscript.fontSetObj_numfonts_get)
    fonts = property(_mapscript.fontSetObj_fonts_get)
    def __init__(self, *args):
        newobj = _mapscript.new_fontSetObj(*args)
        self.this = newobj.this
        self.thisown = 1
        del newobj.thisown
    def __del__(self, destroy=_mapscript.delete_fontSetObj):
        try:
            if self.thisown: destroy(self)
        except: pass

class fontSetObjPtr(fontSetObj):
    def __init__(self, this):
        self.this = this
        if not hasattr(self,"thisown"): self.thisown = 0
        self.__class__ = fontSetObj
_mapscript.fontSetObj_swigregister(fontSetObjPtr)

class outputFormatObj(object):
    def __repr__(self):
        return "<C outputFormatObj instance at %s>" % (self.this,)
    name = property(_mapscript.outputFormatObj_name_get, _mapscript.outputFormatObj_name_set)
    mimetype = property(_mapscript.outputFormatObj_mimetype_get, _mapscript.outputFormatObj_mimetype_set)
    driver = property(_mapscript.outputFormatObj_driver_get, _mapscript.outputFormatObj_driver_set)
    extension = property(_mapscript.outputFormatObj_extension_get, _mapscript.outputFormatObj_extension_set)
    renderer = property(_mapscript.outputFormatObj_renderer_get, _mapscript.outputFormatObj_renderer_set)
    imagemode = property(_mapscript.outputFormatObj_imagemode_get, _mapscript.outputFormatObj_imagemode_set)
    transparent = property(_mapscript.outputFormatObj_transparent_get, _mapscript.outputFormatObj_transparent_set)
    bands = property(_mapscript.outputFormatObj_bands_get, _mapscript.outputFormatObj_bands_set)
    numformatoptions = property(_mapscript.outputFormatObj_numformatoptions_get, _mapscript.outputFormatObj_numformatoptions_set)
    formatoptions = property(_mapscript.outputFormatObj_formatoptions_get, _mapscript.outputFormatObj_formatoptions_set)
    refcount = property(_mapscript.outputFormatObj_refcount_get, _mapscript.outputFormatObj_refcount_set)
    inmapfile = property(_mapscript.outputFormatObj_inmapfile_get, _mapscript.outputFormatObj_inmapfile_set)
    def __init__(self, *args):
        newobj = _mapscript.new_outputFormatObj(*args)
        self.this = newobj.this
        self.thisown = 1
        del newobj.thisown
    def __del__(self, destroy=_mapscript.delete_outputFormatObj):
        try:
            if self.thisown: destroy(self)
        except: pass
    def setExtension(*args): return _mapscript.outputFormatObj_setExtension(*args)
    def setMimetype(*args): return _mapscript.outputFormatObj_setMimetype(*args)
    def setOption(*args): return _mapscript.outputFormatObj_setOption(*args)
    def validate(*args): return _mapscript.outputFormatObj_validate(*args)
    def getOption(*args): return _mapscript.outputFormatObj_getOption(*args)

class outputFormatObjPtr(outputFormatObj):
    def __init__(self, this):
        self.this = this
        if not hasattr(self,"thisown"): self.thisown = 0
        self.__class__ = outputFormatObj
_mapscript.outputFormatObj_swigregister(outputFormatObjPtr)

MS_NOOVERRIDE = _mapscript.MS_NOOVERRIDE
class queryMapObj(object):
    def __repr__(self):
        return "<C queryMapObj instance at %s>" % (self.this,)
    height = property(_mapscript.queryMapObj_height_get, _mapscript.queryMapObj_height_set)
    width = property(_mapscript.queryMapObj_width_get, _mapscript.queryMapObj_width_set)
    status = property(_mapscript.queryMapObj_status_get, _mapscript.queryMapObj_status_set)
    style = property(_mapscript.queryMapObj_style_get, _mapscript.queryMapObj_style_set)
    color = property(_mapscript.queryMapObj_color_get, _mapscript.queryMapObj_color_set)
    def updateFromString(*args): return _mapscript.queryMapObj_updateFromString(*args)
    def __init__(self, *args):
        newobj = _mapscript.new_queryMapObj(*args)
        self.this = newobj.this
        self.thisown = 1
        del newobj.thisown
    def __del__(self, destroy=_mapscript.delete_queryMapObj):
        try:
            if self.thisown: destroy(self)
        except: pass

class queryMapObjPtr(queryMapObj):
    def __init__(self, this):
        self.this = this
        if not hasattr(self,"thisown"): self.thisown = 0
        self.__class__ = queryMapObj
_mapscript.queryMapObj_swigregister(queryMapObjPtr)

class labelObj(object):
    def __repr__(self):
        return "<C labelObj instance at %s>" % (self.this,)
    font = property(_mapscript.labelObj_font_get, _mapscript.labelObj_font_set)
    type = property(_mapscript.labelObj_type_get, _mapscript.labelObj_type_set)
    color = property(_mapscript.labelObj_color_get, _mapscript.labelObj_color_set)
    outlinecolor = property(_mapscript.labelObj_outlinecolor_get, _mapscript.labelObj_outlinecolor_set)
    outlinewidth = property(_mapscript.labelObj_outlinewidth_get, _mapscript.labelObj_outlinewidth_set)
    shadowcolor = property(_mapscript.labelObj_shadowcolor_get, _mapscript.labelObj_shadowcolor_set)
    shadowsizex = property(_mapscript.labelObj_shadowsizex_get, _mapscript.labelObj_shadowsizex_set)
    shadowsizey = property(_mapscript.labelObj_shadowsizey_get, _mapscript.labelObj_shadowsizey_set)
    backgroundcolor = property(_mapscript.labelObj_backgroundcolor_get, _mapscript.labelObj_backgroundcolor_set)
    backgroundshadowcolor = property(_mapscript.labelObj_backgroundshadowcolor_get, _mapscript.labelObj_backgroundshadowcolor_set)
    backgroundshadowsizex = property(_mapscript.labelObj_backgroundshadowsizex_get, _mapscript.labelObj_backgroundshadowsizex_set)
    backgroundshadowsizey = property(_mapscript.labelObj_backgroundshadowsizey_get, _mapscript.labelObj_backgroundshadowsizey_set)
    size = property(_mapscript.labelObj_size_get, _mapscript.labelObj_size_set)
    minsize = property(_mapscript.labelObj_minsize_get, _mapscript.labelObj_minsize_set)
    maxsize = property(_mapscript.labelObj_maxsize_get, _mapscript.labelObj_maxsize_set)
    position = property(_mapscript.labelObj_position_get, _mapscript.labelObj_position_set)
    offsetx = property(_mapscript.labelObj_offsetx_get, _mapscript.labelObj_offsetx_set)
    offsety = property(_mapscript.labelObj_offsety_get, _mapscript.labelObj_offsety_set)
    angle = property(_mapscript.labelObj_angle_get, _mapscript.labelObj_angle_set)
    autoangle = property(_mapscript.labelObj_autoangle_get, _mapscript.labelObj_autoangle_set)
    autofollow = property(_mapscript.labelObj_autofollow_get, _mapscript.labelObj_autofollow_set)
    buffer = property(_mapscript.labelObj_buffer_get, _mapscript.labelObj_buffer_set)
    antialias = property(_mapscript.labelObj_antialias_get, _mapscript.labelObj_antialias_set)
    wrap = property(_mapscript.labelObj_wrap_get, _mapscript.labelObj_wrap_set)
    minfeaturesize = property(_mapscript.labelObj_minfeaturesize_get, _mapscript.labelObj_minfeaturesize_set)
    autominfeaturesize = property(_mapscript.labelObj_autominfeaturesize_get, _mapscript.labelObj_autominfeaturesize_set)
    mindistance = property(_mapscript.labelObj_mindistance_get, _mapscript.labelObj_mindistance_set)
    partials = property(_mapscript.labelObj_partials_get, _mapscript.labelObj_partials_set)
    force = property(_mapscript.labelObj_force_get, _mapscript.labelObj_force_set)
    encoding = property(_mapscript.labelObj_encoding_get, _mapscript.labelObj_encoding_set)
    priority = property(_mapscript.labelObj_priority_get, _mapscript.labelObj_priority_set)
    def updateFromString(*args): return _mapscript.labelObj_updateFromString(*args)
    def removeBinding(*args): return _mapscript.labelObj_removeBinding(*args)
    def setBinding(*args): return _mapscript.labelObj_setBinding(*args)
    def __init__(self, *args):
        newobj = _mapscript.new_labelObj(*args)
        self.this = newobj.this
        self.thisown = 1
        del newobj.thisown
    def __del__(self, destroy=_mapscript.delete_labelObj):
        try:
            if self.thisown: destroy(self)
        except: pass

class labelObjPtr(labelObj):
    def __init__(self, this):
        self.this = this
        if not hasattr(self,"thisown"): self.thisown = 0
        self.__class__ = labelObj
_mapscript.labelObj_swigregister(labelObjPtr)

class webObj(object):
    def __repr__(self):
        return "<C webObj instance at %s>" % (self.this,)
    log = property(_mapscript.webObj_log_get, _mapscript.webObj_log_set)
    imagepath = property(_mapscript.webObj_imagepath_get, _mapscript.webObj_imagepath_set)
    imageurl = property(_mapscript.webObj_imageurl_get, _mapscript.webObj_imageurl_set)
    map = property(_mapscript.webObj_map_get)
    template = property(_mapscript.webObj_template_get, _mapscript.webObj_template_set)
    header = property(_mapscript.webObj_header_get, _mapscript.webObj_header_set)
    footer = property(_mapscript.webObj_footer_get, _mapscript.webObj_footer_set)
    empty = property(_mapscript.webObj_empty_get, _mapscript.webObj_empty_set)
    error = property(_mapscript.webObj_error_get, _mapscript.webObj_error_set)
    extent = property(_mapscript.webObj_extent_get, _mapscript.webObj_extent_set)
    minscaledenom = property(_mapscript.webObj_minscaledenom_get, _mapscript.webObj_minscaledenom_set)
    maxscaledenom = property(_mapscript.webObj_maxscaledenom_get, _mapscript.webObj_maxscaledenom_set)
    mintemplate = property(_mapscript.webObj_mintemplate_get, _mapscript.webObj_mintemplate_set)
    maxtemplate = property(_mapscript.webObj_maxtemplate_get, _mapscript.webObj_maxtemplate_set)
    queryformat = property(_mapscript.webObj_queryformat_get, _mapscript.webObj_queryformat_set)
    legendformat = property(_mapscript.webObj_legendformat_get, _mapscript.webObj_legendformat_set)
    browseformat = property(_mapscript.webObj_browseformat_get, _mapscript.webObj_browseformat_set)
    metadata = property(_mapscript.webObj_metadata_get)
    def __init__(self, *args):
        newobj = _mapscript.new_webObj(*args)
        self.this = newobj.this
        self.thisown = 1
        del newobj.thisown
    def __del__(self, destroy=_mapscript.delete_webObj):
        try:
            if self.thisown: destroy(self)
        except: pass
    def updateFromString(*args): return _mapscript.webObj_updateFromString(*args)

class webObjPtr(webObj):
    def __init__(self, this):
        self.this = this
        if not hasattr(self,"thisown"): self.thisown = 0
        self.__class__ = webObj
_mapscript.webObj_swigregister(webObjPtr)

class styleObj(object):
    def __repr__(self):
        return "<C styleObj instance at %s>" % (self.this,)
    refcount = property(_mapscript.styleObj_refcount_get)
    color = property(_mapscript.styleObj_color_get, _mapscript.styleObj_color_set)
    backgroundcolor = property(_mapscript.styleObj_backgroundcolor_get, _mapscript.styleObj_backgroundcolor_set)
    outlinecolor = property(_mapscript.styleObj_outlinecolor_get, _mapscript.styleObj_outlinecolor_set)
    opacity = property(_mapscript.styleObj_opacity_get, _mapscript.styleObj_opacity_set)
    mincolor = property(_mapscript.styleObj_mincolor_get, _mapscript.styleObj_mincolor_set)
    maxcolor = property(_mapscript.styleObj_maxcolor_get, _mapscript.styleObj_maxcolor_set)
    minvalue = property(_mapscript.styleObj_minvalue_get, _mapscript.styleObj_minvalue_set)
    maxvalue = property(_mapscript.styleObj_maxvalue_get, _mapscript.styleObj_maxvalue_set)
    rangeitem = property(_mapscript.styleObj_rangeitem_get, _mapscript.styleObj_rangeitem_set)
    rangeitemindex = property(_mapscript.styleObj_rangeitemindex_get, _mapscript.styleObj_rangeitemindex_set)
    symbol = property(_mapscript.styleObj_symbol_get, _mapscript.styleObj_symbol_set)
    symbolname = property(_mapscript.styleObj_symbolname_get, _mapscript.styleObj_symbolname_set)
    size = property(_mapscript.styleObj_size_get, _mapscript.styleObj_size_set)
    minsize = property(_mapscript.styleObj_minsize_get, _mapscript.styleObj_minsize_set)
    maxsize = property(_mapscript.styleObj_maxsize_get, _mapscript.styleObj_maxsize_set)
    width = property(_mapscript.styleObj_width_get, _mapscript.styleObj_width_set)
    minwidth = property(_mapscript.styleObj_minwidth_get, _mapscript.styleObj_minwidth_set)
    maxwidth = property(_mapscript.styleObj_maxwidth_get, _mapscript.styleObj_maxwidth_set)
    offsetx = property(_mapscript.styleObj_offsetx_get, _mapscript.styleObj_offsetx_set)
    offsety = property(_mapscript.styleObj_offsety_get, _mapscript.styleObj_offsety_set)
    angle = property(_mapscript.styleObj_angle_get, _mapscript.styleObj_angle_set)
    antialias = property(_mapscript.styleObj_antialias_get, _mapscript.styleObj_antialias_set)
    def __init__(self, *args):
        newobj = _mapscript.new_styleObj(*args)
        self.this = newobj.this
        self.thisown = 1
        del newobj.thisown
    def __del__(self, destroy=_mapscript.delete_styleObj):
        try:
            if self.thisown: destroy(self)
        except: pass
    def updateFromString(*args): return _mapscript.styleObj_updateFromString(*args)
    def clone(*args): return _mapscript.styleObj_clone(*args)
    def setSymbolByName(*args): return _mapscript.styleObj_setSymbolByName(*args)
    def removeBinding(*args): return _mapscript.styleObj_removeBinding(*args)
    def setBinding(*args): return _mapscript.styleObj_setBinding(*args)

class styleObjPtr(styleObj):
    def __init__(self, this):
        self.this = this
        if not hasattr(self,"thisown"): self.thisown = 0
        self.__class__ = styleObj
_mapscript.styleObj_swigregister(styleObjPtr)

class classObj(object):
    def __repr__(self):
        return "<C classObj instance at %s>" % (self.this,)
    status = property(_mapscript.classObj_status_get, _mapscript.classObj_status_set)
    numstyles = property(_mapscript.classObj_numstyles_get, _mapscript.classObj_numstyles_set)
    label = property(_mapscript.classObj_label_get)
    name = property(_mapscript.classObj_name_get, _mapscript.classObj_name_set)
    title = property(_mapscript.classObj_title_get, _mapscript.classObj_title_set)
    template = property(_mapscript.classObj_template_get, _mapscript.classObj_template_set)
    type = property(_mapscript.classObj_type_get, _mapscript.classObj_type_set)
    metadata = property(_mapscript.classObj_metadata_get)
    minscaledenom = property(_mapscript.classObj_minscaledenom_get, _mapscript.classObj_minscaledenom_set)
    maxscaledenom = property(_mapscript.classObj_maxscaledenom_get, _mapscript.classObj_maxscaledenom_set)
    refcount = property(_mapscript.classObj_refcount_get)
    layer = property(_mapscript.classObj_layer_get)
    debug = property(_mapscript.classObj_debug_get, _mapscript.classObj_debug_set)
    keyimage = property(_mapscript.classObj_keyimage_get, _mapscript.classObj_keyimage_set)
    group = property(_mapscript.classObj_group_get, _mapscript.classObj_group_set)
    def __init__(self, *args):
        newobj = _mapscript.new_classObj(*args)
        self.this = newobj.this
        self.thisown = 1
        del newobj.thisown
    def __del__(self, destroy=_mapscript.delete_classObj):
        try:
            if self.thisown: destroy(self)
        except: pass
    def updateFromString(*args): return _mapscript.classObj_updateFromString(*args)
    def clone(*args): return _mapscript.classObj_clone(*args)
    def setExpression(*args): return _mapscript.classObj_setExpression(*args)
    def getExpressionString(*args): return _mapscript.classObj_getExpressionString(*args)
    def setText(*args): return _mapscript.classObj_setText(*args)
    def getTextString(*args): return _mapscript.classObj_getTextString(*args)
    def getMetaData(*args): return _mapscript.classObj_getMetaData(*args)
    def setMetaData(*args): return _mapscript.classObj_setMetaData(*args)
    def getFirstMetaDataKey(*args): return _mapscript.classObj_getFirstMetaDataKey(*args)
    def getNextMetaDataKey(*args): return _mapscript.classObj_getNextMetaDataKey(*args)
    def drawLegendIcon(*args): return _mapscript.classObj_drawLegendIcon(*args)
    def createLegendIcon(*args): return _mapscript.classObj_createLegendIcon(*args)
    def getStyle(*args): return _mapscript.classObj_getStyle(*args)
    def insertStyle(*args): return _mapscript.classObj_insertStyle(*args)
    def removeStyle(*args): return _mapscript.classObj_removeStyle(*args)
    def moveStyleUp(*args): return _mapscript.classObj_moveStyleUp(*args)
    def moveStyleDown(*args): return _mapscript.classObj_moveStyleDown(*args)

class classObjPtr(classObj):
    def __init__(self, this):
        self.this = this
        if not hasattr(self,"thisown"): self.thisown = 0
        self.__class__ = classObj
_mapscript.classObj_swigregister(classObjPtr)

class labelCacheMemberObj(object):
    def __repr__(self):
        return "<C labelCacheMemberObj instance at %s>" % (self.this,)
    text = property(_mapscript.labelCacheMemberObj_text_get)
    featuresize = property(_mapscript.labelCacheMemberObj_featuresize_get)
    styles = property(_mapscript.labelCacheMemberObj_styles_get)
    numstyles = property(_mapscript.labelCacheMemberObj_numstyles_get)
    label = property(_mapscript.labelCacheMemberObj_label_get)
    layerindex = property(_mapscript.labelCacheMemberObj_layerindex_get)
    classindex = property(_mapscript.labelCacheMemberObj_classindex_get)
    tileindex = property(_mapscript.labelCacheMemberObj_tileindex_get)
    shapeindex = property(_mapscript.labelCacheMemberObj_shapeindex_get)
    point = property(_mapscript.labelCacheMemberObj_point_get)
    poly = property(_mapscript.labelCacheMemberObj_poly_get)
    status = property(_mapscript.labelCacheMemberObj_status_get)
    def __init__(self, *args):
        newobj = _mapscript.new_labelCacheMemberObj(*args)
        self.this = newobj.this
        self.thisown = 1
        del newobj.thisown
    def __del__(self, destroy=_mapscript.delete_labelCacheMemberObj):
        try:
            if self.thisown: destroy(self)
        except: pass

class labelCacheMemberObjPtr(labelCacheMemberObj):
    def __init__(self, this):
        self.this = this
        if not hasattr(self,"thisown"): self.thisown = 0
        self.__class__ = labelCacheMemberObj
_mapscript.labelCacheMemberObj_swigregister(labelCacheMemberObjPtr)

class markerCacheMemberObj(object):
    def __repr__(self):
        return "<C markerCacheMemberObj instance at %s>" % (self.this,)
    id = property(_mapscript.markerCacheMemberObj_id_get)
    poly = property(_mapscript.markerCacheMemberObj_poly_get)
    def __init__(self, *args):
        newobj = _mapscript.new_markerCacheMemberObj(*args)
        self.this = newobj.this
        self.thisown = 1
        del newobj.thisown
    def __del__(self, destroy=_mapscript.delete_markerCacheMemberObj):
        try:
            if self.thisown: destroy(self)
        except: pass

class markerCacheMemberObjPtr(markerCacheMemberObj):
    def __init__(self, this):
        self.this = this
        if not hasattr(self,"thisown"): self.thisown = 0
        self.__class__ = markerCacheMemberObj
_mapscript.markerCacheMemberObj_swigregister(markerCacheMemberObjPtr)

class labelCacheSlotObj(object):
    def __repr__(self):
        return "<C labelCacheSlotObj instance at %s>" % (self.this,)
    labels = property(_mapscript.labelCacheSlotObj_labels_get)
    numlabels = property(_mapscript.labelCacheSlotObj_numlabels_get)
    cachesize = property(_mapscript.labelCacheSlotObj_cachesize_get)
    markers = property(_mapscript.labelCacheSlotObj_markers_get)
    nummarkers = property(_mapscript.labelCacheSlotObj_nummarkers_get)
    markercachesize = property(_mapscript.labelCacheSlotObj_markercachesize_get)
    def __init__(self, *args):
        newobj = _mapscript.new_labelCacheSlotObj(*args)
        self.this = newobj.this
        self.thisown = 1
        del newobj.thisown
    def __del__(self, destroy=_mapscript.delete_labelCacheSlotObj):
        try:
            if self.thisown: destroy(self)
        except: pass

class labelCacheSlotObjPtr(labelCacheSlotObj):
    def __init__(self, this):
        self.this = this
        if not hasattr(self,"thisown"): self.thisown = 0
        self.__class__ = labelCacheSlotObj
_mapscript.labelCacheSlotObj_swigregister(labelCacheSlotObjPtr)

class labelCacheObj(object):
    def __repr__(self):
        return "<C labelCacheObj instance at %s>" % (self.this,)
    slots = property(_mapscript.labelCacheObj_slots_get)
    numlabels = property(_mapscript.labelCacheObj_numlabels_get)
    def freeCache(*args): return _mapscript.labelCacheObj_freeCache(*args)
    def __init__(self, *args):
        newobj = _mapscript.new_labelCacheObj(*args)
        self.this = newobj.this
        self.thisown = 1
        del newobj.thisown
    def __del__(self, destroy=_mapscript.delete_labelCacheObj):
        try:
            if self.thisown: destroy(self)
        except: pass

class labelCacheObjPtr(labelCacheObj):
    def __init__(self, this):
        self.this = this
        if not hasattr(self,"thisown"): self.thisown = 0
        self.__class__ = labelCacheObj
_mapscript.labelCacheObj_swigregister(labelCacheObjPtr)

class resultCacheMemberObj(object):
    def __repr__(self):
        return "<C resultCacheMemberObj instance at %s>" % (self.this,)
    shapeindex = property(_mapscript.resultCacheMemberObj_shapeindex_get)
    tileindex = property(_mapscript.resultCacheMemberObj_tileindex_get)
    classindex = property(_mapscript.resultCacheMemberObj_classindex_get)
    def __init__(self, *args):
        newobj = _mapscript.new_resultCacheMemberObj(*args)
        self.this = newobj.this
        self.thisown = 1
        del newobj.thisown
    def __del__(self, destroy=_mapscript.delete_resultCacheMemberObj):
        try:
            if self.thisown: destroy(self)
        except: pass

class resultCacheMemberObjPtr(resultCacheMemberObj):
    def __init__(self, this):
        self.this = this
        if not hasattr(self,"thisown"): self.thisown = 0
        self.__class__ = resultCacheMemberObj
_mapscript.resultCacheMemberObj_swigregister(resultCacheMemberObjPtr)

class resultCacheObj(object):
    def __repr__(self):
        return "<C resultCacheObj instance at %s>" % (self.this,)
    numresults = property(_mapscript.resultCacheObj_numresults_get)
    bounds = property(_mapscript.resultCacheObj_bounds_get)
    def getResult(*args): return _mapscript.resultCacheObj_getResult(*args)
    def __init__(self, *args):
        newobj = _mapscript.new_resultCacheObj(*args)
        self.this = newobj.this
        self.thisown = 1
        del newobj.thisown
    def __del__(self, destroy=_mapscript.delete_resultCacheObj):
        try:
            if self.thisown: destroy(self)
        except: pass

class resultCacheObjPtr(resultCacheObj):
    def __init__(self, this):
        self.this = this
        if not hasattr(self,"thisown"): self.thisown = 0
        self.__class__ = resultCacheObj
_mapscript.resultCacheObj_swigregister(resultCacheObjPtr)

class symbolSetObj(object):
    def __repr__(self):
        return "<C symbolSetObj instance at %s>" % (self.this,)
    filename = property(_mapscript.symbolSetObj_filename_get, _mapscript.symbolSetObj_filename_set)
    imagecachesize = property(_mapscript.symbolSetObj_imagecachesize_get, _mapscript.symbolSetObj_imagecachesize_set)
    numsymbols = property(_mapscript.symbolSetObj_numsymbols_get)
    maxsymbols = property(_mapscript.symbolSetObj_maxsymbols_get)
    def __init__(self, *args):
        newobj = _mapscript.new_symbolSetObj(*args)
        self.this = newobj.this
        self.thisown = 1
        del newobj.thisown
    def __del__(self, destroy=_mapscript.delete_symbolSetObj):
        try:
            if self.thisown: destroy(self)
        except: pass
    def getSymbol(*args): return _mapscript.symbolSetObj_getSymbol(*args)
    def getSymbolByName(*args): return _mapscript.symbolSetObj_getSymbolByName(*args)
    def index(*args): return _mapscript.symbolSetObj_index(*args)
    def appendSymbol(*args): return _mapscript.symbolSetObj_appendSymbol(*args)
    def removeSymbol(*args): return _mapscript.symbolSetObj_removeSymbol(*args)
    def save(*args): return _mapscript.symbolSetObj_save(*args)

class symbolSetObjPtr(symbolSetObj):
    def __init__(self, this):
        self.this = this
        if not hasattr(self,"thisown"): self.thisown = 0
        self.__class__ = symbolSetObj
_mapscript.symbolSetObj_swigregister(symbolSetObjPtr)

class referenceMapObj(object):
    def __repr__(self):
        return "<C referenceMapObj instance at %s>" % (self.this,)
    extent = property(_mapscript.referenceMapObj_extent_get, _mapscript.referenceMapObj_extent_set)
    height = property(_mapscript.referenceMapObj_height_get, _mapscript.referenceMapObj_height_set)
    width = property(_mapscript.referenceMapObj_width_get, _mapscript.referenceMapObj_width_set)
    color = property(_mapscript.referenceMapObj_color_get, _mapscript.referenceMapObj_color_set)
    outlinecolor = property(_mapscript.referenceMapObj_outlinecolor_get, _mapscript.referenceMapObj_outlinecolor_set)
    image = property(_mapscript.referenceMapObj_image_get, _mapscript.referenceMapObj_image_set)
    status = property(_mapscript.referenceMapObj_status_get, _mapscript.referenceMapObj_status_set)
    marker = property(_mapscript.referenceMapObj_marker_get, _mapscript.referenceMapObj_marker_set)
    markername = property(_mapscript.referenceMapObj_markername_get, _mapscript.referenceMapObj_markername_set)
    markersize = property(_mapscript.referenceMapObj_markersize_get, _mapscript.referenceMapObj_markersize_set)
    minboxsize = property(_mapscript.referenceMapObj_minboxsize_get, _mapscript.referenceMapObj_minboxsize_set)
    maxboxsize = property(_mapscript.referenceMapObj_maxboxsize_get, _mapscript.referenceMapObj_maxboxsize_set)
    map = property(_mapscript.referenceMapObj_map_get)
    def updateFromString(*args): return _mapscript.referenceMapObj_updateFromString(*args)
    def __init__(self, *args):
        newobj = _mapscript.new_referenceMapObj(*args)
        self.this = newobj.this
        self.thisown = 1
        del newobj.thisown
    def __del__(self, destroy=_mapscript.delete_referenceMapObj):
        try:
            if self.thisown: destroy(self)
        except: pass

class referenceMapObjPtr(referenceMapObj):
    def __init__(self, this):
        self.this = this
        if not hasattr(self,"thisown"): self.thisown = 0
        self.__class__ = referenceMapObj
_mapscript.referenceMapObj_swigregister(referenceMapObjPtr)

class scalebarObj(object):
    def __repr__(self):
        return "<C scalebarObj instance at %s>" % (self.this,)
    imagecolor = property(_mapscript.scalebarObj_imagecolor_get, _mapscript.scalebarObj_imagecolor_set)
    height = property(_mapscript.scalebarObj_height_get, _mapscript.scalebarObj_height_set)
    width = property(_mapscript.scalebarObj_width_get, _mapscript.scalebarObj_width_set)
    style = property(_mapscript.scalebarObj_style_get, _mapscript.scalebarObj_style_set)
    intervals = property(_mapscript.scalebarObj_intervals_get, _mapscript.scalebarObj_intervals_set)
    label = property(_mapscript.scalebarObj_label_get, _mapscript.scalebarObj_label_set)
    color = property(_mapscript.scalebarObj_color_get, _mapscript.scalebarObj_color_set)
    backgroundcolor = property(_mapscript.scalebarObj_backgroundcolor_get, _mapscript.scalebarObj_backgroundcolor_set)
    outlinecolor = property(_mapscript.scalebarObj_outlinecolor_get, _mapscript.scalebarObj_outlinecolor_set)
    units = property(_mapscript.scalebarObj_units_get, _mapscript.scalebarObj_units_set)
    status = property(_mapscript.scalebarObj_status_get, _mapscript.scalebarObj_status_set)
    position = property(_mapscript.scalebarObj_position_get, _mapscript.scalebarObj_position_set)
    postlabelcache = property(_mapscript.scalebarObj_postlabelcache_get, _mapscript.scalebarObj_postlabelcache_set)
    align = property(_mapscript.scalebarObj_align_get, _mapscript.scalebarObj_align_set)
    def updateFromString(*args): return _mapscript.scalebarObj_updateFromString(*args)
    def __init__(self, *args):
        newobj = _mapscript.new_scalebarObj(*args)
        self.this = newobj.this
        self.thisown = 1
        del newobj.thisown
    def __del__(self, destroy=_mapscript.delete_scalebarObj):
        try:
            if self.thisown: destroy(self)
        except: pass

class scalebarObjPtr(scalebarObj):
    def __init__(self, this):
        self.this = this
        if not hasattr(self,"thisown"): self.thisown = 0
        self.__class__ = scalebarObj
_mapscript.scalebarObj_swigregister(scalebarObjPtr)

class legendObj(object):
    def __repr__(self):
        return "<C legendObj instance at %s>" % (self.this,)
    imagecolor = property(_mapscript.legendObj_imagecolor_get, _mapscript.legendObj_imagecolor_set)
    label = property(_mapscript.legendObj_label_get)
    keysizex = property(_mapscript.legendObj_keysizex_get, _mapscript.legendObj_keysizex_set)
    keysizey = property(_mapscript.legendObj_keysizey_get, _mapscript.legendObj_keysizey_set)
    keyspacingx = property(_mapscript.legendObj_keyspacingx_get, _mapscript.legendObj_keyspacingx_set)
    keyspacingy = property(_mapscript.legendObj_keyspacingy_get, _mapscript.legendObj_keyspacingy_set)
    outlinecolor = property(_mapscript.legendObj_outlinecolor_get, _mapscript.legendObj_outlinecolor_set)
    status = property(_mapscript.legendObj_status_get, _mapscript.legendObj_status_set)
    height = property(_mapscript.legendObj_height_get, _mapscript.legendObj_height_set)
    width = property(_mapscript.legendObj_width_get, _mapscript.legendObj_width_set)
    position = property(_mapscript.legendObj_position_get, _mapscript.legendObj_position_set)
    postlabelcache = property(_mapscript.legendObj_postlabelcache_get, _mapscript.legendObj_postlabelcache_set)
    template = property(_mapscript.legendObj_template_get, _mapscript.legendObj_template_set)
    map = property(_mapscript.legendObj_map_get)
    def updateFromString(*args): return _mapscript.legendObj_updateFromString(*args)
    def __init__(self, *args):
        newobj = _mapscript.new_legendObj(*args)
        self.this = newobj.this
        self.thisown = 1
        del newobj.thisown
    def __del__(self, destroy=_mapscript.delete_legendObj):
        try:
            if self.thisown: destroy(self)
        except: pass

class legendObjPtr(legendObj):
    def __init__(self, this):
        self.this = this
        if not hasattr(self,"thisown"): self.thisown = 0
        self.__class__ = legendObj
_mapscript.legendObj_swigregister(legendObjPtr)

class layerObj(object):
    def __repr__(self):
        return "<C layerObj instance at %s>" % (self.this,)
    classitem = property(_mapscript.layerObj_classitem_get, _mapscript.layerObj_classitem_set)
    refcount = property(_mapscript.layerObj_refcount_get)
    numclasses = property(_mapscript.layerObj_numclasses_get)
    maxclasses = property(_mapscript.layerObj_maxclasses_get)
    index = property(_mapscript.layerObj_index_get)
    map = property(_mapscript.layerObj_map_get)
    header = property(_mapscript.layerObj_header_get, _mapscript.layerObj_header_set)
    footer = property(_mapscript.layerObj_footer_get, _mapscript.layerObj_footer_set)
    template = property(_mapscript.layerObj_template_get, _mapscript.layerObj_template_set)
    name = property(_mapscript.layerObj_name_get, _mapscript.layerObj_name_set)
    group = property(_mapscript.layerObj_group_get, _mapscript.layerObj_group_set)
    status = property(_mapscript.layerObj_status_get, _mapscript.layerObj_status_set)
    data = property(_mapscript.layerObj_data_get, _mapscript.layerObj_data_set)
    type = property(_mapscript.layerObj_type_get, _mapscript.layerObj_type_set)
    tolerance = property(_mapscript.layerObj_tolerance_get, _mapscript.layerObj_tolerance_set)
    toleranceunits = property(_mapscript.layerObj_toleranceunits_get, _mapscript.layerObj_toleranceunits_set)
    symbolscaledenom = property(_mapscript.layerObj_symbolscaledenom_get, _mapscript.layerObj_symbolscaledenom_set)
    minscaledenom = property(_mapscript.layerObj_minscaledenom_get, _mapscript.layerObj_minscaledenom_set)
    maxscaledenom = property(_mapscript.layerObj_maxscaledenom_get, _mapscript.layerObj_maxscaledenom_set)
    labelminscaledenom = property(_mapscript.layerObj_labelminscaledenom_get, _mapscript.layerObj_labelminscaledenom_set)
    labelmaxscaledenom = property(_mapscript.layerObj_labelmaxscaledenom_get, _mapscript.layerObj_labelmaxscaledenom_set)
    sizeunits = property(_mapscript.layerObj_sizeunits_get, _mapscript.layerObj_sizeunits_set)
    maxfeatures = property(_mapscript.layerObj_maxfeatures_get, _mapscript.layerObj_maxfeatures_set)
    offsite = property(_mapscript.layerObj_offsite_get, _mapscript.layerObj_offsite_set)
    transform = property(_mapscript.layerObj_transform_get, _mapscript.layerObj_transform_set)
    labelcache = property(_mapscript.layerObj_labelcache_get, _mapscript.layerObj_labelcache_set)
    postlabelcache = property(_mapscript.layerObj_postlabelcache_get, _mapscript.layerObj_postlabelcache_set)
    labelitem = property(_mapscript.layerObj_labelitem_get, _mapscript.layerObj_labelitem_set)
    tileitem = property(_mapscript.layerObj_tileitem_get, _mapscript.layerObj_tileitem_set)
    tileindex = property(_mapscript.layerObj_tileindex_get, _mapscript.layerObj_tileindex_set)
    units = property(_mapscript.layerObj_units_get, _mapscript.layerObj_units_set)
    connection = property(_mapscript.layerObj_connection_get, _mapscript.layerObj_connection_set)
    plugin_library = property(_mapscript.layerObj_plugin_library_get, _mapscript.layerObj_plugin_library_set)
    plugin_library_original = property(_mapscript.layerObj_plugin_library_original_get, _mapscript.layerObj_plugin_library_original_set)
    connectiontype = property(_mapscript.layerObj_connectiontype_get, _mapscript.layerObj_connectiontype_set)
    numitems = property(_mapscript.layerObj_numitems_get)
    bandsitem = property(_mapscript.layerObj_bandsitem_get, _mapscript.layerObj_bandsitem_set)
    filteritem = property(_mapscript.layerObj_filteritem_get, _mapscript.layerObj_filteritem_set)
    styleitem = property(_mapscript.layerObj_styleitem_get, _mapscript.layerObj_styleitem_set)
    requires = property(_mapscript.layerObj_requires_get, _mapscript.layerObj_requires_set)
    labelrequires = property(_mapscript.layerObj_labelrequires_get, _mapscript.layerObj_labelrequires_set)
    metadata = property(_mapscript.layerObj_metadata_get)
    opacity = property(_mapscript.layerObj_opacity_get, _mapscript.layerObj_opacity_set)
    dump = property(_mapscript.layerObj_dump_get, _mapscript.layerObj_dump_set)
    debug = property(_mapscript.layerObj_debug_get, _mapscript.layerObj_debug_set)
    extent = property(_mapscript.layerObj_extent_get)
    numprocessing = property(_mapscript.layerObj_numprocessing_get)
    numjoins = property(_mapscript.layerObj_numjoins_get)
    classgroup = property(_mapscript.layerObj_classgroup_get, _mapscript.layerObj_classgroup_set)
    def __init__(self, *args):
        newobj = _mapscript.new_layerObj(*args)
        self.this = newobj.this
        self.thisown = 1
        del newobj.thisown
    def __del__(self, destroy=_mapscript.delete_layerObj):
        try:
            if self.thisown: destroy(self)
        except: pass
    def clone(*args): return _mapscript.layerObj_clone(*args)
    def updateFromString(*args): return _mapscript.layerObj_updateFromString(*args)
    def insertClass(*args):
           actualIndex=_mapscript.layerObj_insertClass(*args)
           args[1].p_layer=args[0]
           return actualIndex

    def removeClass(*args): return _mapscript.layerObj_removeClass(*args)
    def open(*args): return _mapscript.layerObj_open(*args)
    def whichShapes(*args): return _mapscript.layerObj_whichShapes(*args)
    def nextShape(*args): return _mapscript.layerObj_nextShape(*args)
    def close(*args): return _mapscript.layerObj_close(*args)
    def getFeature(*args): return _mapscript.layerObj_getFeature(*args)
    def getShape(*args): return _mapscript.layerObj_getShape(*args)
    def getNumResults(*args): return _mapscript.layerObj_getNumResults(*args)
    def getResult(*args): return _mapscript.layerObj_getResult(*args)
    def getClass(*args):
    	clazz = _mapscript.layerObj_getClass(*args)
    	if clazz:
    		if args and len(args)!=0:
    			clazz.p_layer=args[0]
    		else:
    			clazz.p_layer=None
    	return clazz

    def getItem(*args): return _mapscript.layerObj_getItem(*args)
    def draw(*args): return _mapscript.layerObj_draw(*args)
    def drawQuery(*args): return _mapscript.layerObj_drawQuery(*args)
    def queryByAttributes(*args): return _mapscript.layerObj_queryByAttributes(*args)
    def queryByPoint(*args): return _mapscript.layerObj_queryByPoint(*args)
    def queryByRect(*args): return _mapscript.layerObj_queryByRect(*args)
    def queryByFeatures(*args): return _mapscript.layerObj_queryByFeatures(*args)
    def queryByShape(*args): return _mapscript.layerObj_queryByShape(*args)
    def queryByIndex(*args): return _mapscript.layerObj_queryByIndex(*args)
    def getResults(*args): return _mapscript.layerObj_getResults(*args)
    def setFilter(*args): return _mapscript.layerObj_setFilter(*args)
    def getFilterString(*args): return _mapscript.layerObj_getFilterString(*args)
    def setWKTProjection(*args): return _mapscript.layerObj_setWKTProjection(*args)
    def getProjection(*args): return _mapscript.layerObj_getProjection(*args)
    def setProjection(*args): return _mapscript.layerObj_setProjection(*args)
    def addFeature(*args): return _mapscript.layerObj_addFeature(*args)
    def getNumFeatures(*args): return _mapscript.layerObj_getNumFeatures(*args)
    def getExtent(*args): return _mapscript.layerObj_getExtent(*args)
    def setExtent(*args): return _mapscript.layerObj_setExtent(*args)
    def getMetaData(*args): return _mapscript.layerObj_getMetaData(*args)
    def setMetaData(*args): return _mapscript.layerObj_setMetaData(*args)
    def removeMetaData(*args): return _mapscript.layerObj_removeMetaData(*args)
    def getFirstMetaDataKey(*args): return _mapscript.layerObj_getFirstMetaDataKey(*args)
    def getNextMetaDataKey(*args): return _mapscript.layerObj_getNextMetaDataKey(*args)
    def getWMSFeatureInfoURL(*args): return _mapscript.layerObj_getWMSFeatureInfoURL(*args)
    def executeWFSGetFeature(*args): return _mapscript.layerObj_executeWFSGetFeature(*args)
    def applySLD(*args): return _mapscript.layerObj_applySLD(*args)
    def applySLDURL(*args): return _mapscript.layerObj_applySLDURL(*args)
    def generateSLD(*args): return _mapscript.layerObj_generateSLD(*args)
    def isVisible(*args): return _mapscript.layerObj_isVisible(*args)
    def moveClassUp(*args): return _mapscript.layerObj_moveClassUp(*args)
    def moveClassDown(*args): return _mapscript.layerObj_moveClassDown(*args)
    def setProcessingKey(*args): return _mapscript.layerObj_setProcessingKey(*args)
    def setProcessing(*args): return _mapscript.layerObj_setProcessing(*args)
    def addProcessing(*args): return _mapscript.layerObj_addProcessing(*args)
    def getProcessing(*args): return _mapscript.layerObj_getProcessing(*args)
    def getProcessingKey(*args): return _mapscript.layerObj_getProcessingKey(*args)
    def clearProcessing(*args): return _mapscript.layerObj_clearProcessing(*args)

class layerObjPtr(layerObj):
    def __init__(self, this):
        self.this = this
        if not hasattr(self,"thisown"): self.thisown = 0
        self.__class__ = layerObj
_mapscript.layerObj_swigregister(layerObjPtr)

class mapObj(object):
    def __repr__(self):
        return "<C mapObj instance at %s>" % (self.this,)
    name = property(_mapscript.mapObj_name_get, _mapscript.mapObj_name_set)
    status = property(_mapscript.mapObj_status_get, _mapscript.mapObj_status_set)
    height = property(_mapscript.mapObj_height_get, _mapscript.mapObj_height_set)
    width = property(_mapscript.mapObj_width_get, _mapscript.mapObj_width_set)
    maxsize = property(_mapscript.mapObj_maxsize_get, _mapscript.mapObj_maxsize_set)
    refcount = property(_mapscript.mapObj_refcount_get)
    numlayers = property(_mapscript.mapObj_numlayers_get)
    maxlayers = property(_mapscript.mapObj_maxlayers_get)
    symbolset = property(_mapscript.mapObj_symbolset_get)
    fontset = property(_mapscript.mapObj_fontset_get)
    labelcache = property(_mapscript.mapObj_labelcache_get)
    transparent = property(_mapscript.mapObj_transparent_get, _mapscript.mapObj_transparent_set)
    interlace = property(_mapscript.mapObj_interlace_get, _mapscript.mapObj_interlace_set)
    imagequality = property(_mapscript.mapObj_imagequality_get, _mapscript.mapObj_imagequality_set)
    extent = property(_mapscript.mapObj_extent_get, _mapscript.mapObj_extent_set)
    cellsize = property(_mapscript.mapObj_cellsize_get, _mapscript.mapObj_cellsize_set)
    saved_extent = property(_mapscript.mapObj_saved_extent_get, _mapscript.mapObj_saved_extent_set)
    units = property(_mapscript.mapObj_units_get, _mapscript.mapObj_units_set)
    scaledenom = property(_mapscript.mapObj_scaledenom_get, _mapscript.mapObj_scaledenom_set)
    resolution = property(_mapscript.mapObj_resolution_get, _mapscript.mapObj_resolution_set)
    shapepath = property(_mapscript.mapObj_shapepath_get, _mapscript.mapObj_shapepath_set)
    mappath = property(_mapscript.mapObj_mappath_get, _mapscript.mapObj_mappath_set)
    imagecolor = property(_mapscript.mapObj_imagecolor_get, _mapscript.mapObj_imagecolor_set)
    numoutputformats = property(_mapscript.mapObj_numoutputformats_get)
    outputformatlist = property(_mapscript.mapObj_outputformatlist_get)
    outputformat = property(_mapscript.mapObj_outputformat_get)
    imagetype = property(_mapscript.mapObj_imagetype_get)
    reference = property(_mapscript.mapObj_reference_get)
    scalebar = property(_mapscript.mapObj_scalebar_get)
    legend = property(_mapscript.mapObj_legend_get)
    querymap = property(_mapscript.mapObj_querymap_get)
    web = property(_mapscript.mapObj_web_get)
    layerorder = property(_mapscript.mapObj_layerorder_get, _mapscript.mapObj_layerorder_set)
    debug = property(_mapscript.mapObj_debug_get, _mapscript.mapObj_debug_set)
    datapattern = property(_mapscript.mapObj_datapattern_get, _mapscript.mapObj_datapattern_set)
    templatepattern = property(_mapscript.mapObj_templatepattern_get, _mapscript.mapObj_templatepattern_set)
    configoptions = property(_mapscript.mapObj_configoptions_get)
    def __init__(self, *args):
        newobj = _mapscript.new_mapObj(*args)
        self.this = newobj.this
        self.thisown = 1
        del newobj.thisown
    def __del__(self, destroy=_mapscript.delete_mapObj):
        try:
            if self.thisown: destroy(self)
        except: pass
    def clone(*args): return _mapscript.mapObj_clone(*args)
    def insertLayer(*args):
           actualIndex=_mapscript.mapObj_insertLayer(*args)
           args[1].p_map=args[0]
           return actualIndex

    def removeLayer(*args): return _mapscript.mapObj_removeLayer(*args)
    def setExtent(*args): return _mapscript.mapObj_setExtent(*args)
    def offsetExtent(*args): return _mapscript.mapObj_offsetExtent(*args)
    def scaleExtent(*args): return _mapscript.mapObj_scaleExtent(*args)
    def setCenter(*args): return _mapscript.mapObj_setCenter(*args)
    def setSize(*args): return _mapscript.mapObj_setSize(*args)
    def setRotation(*args): return _mapscript.mapObj_setRotation(*args)
    def getLayer(*args):
    	layer = _mapscript.mapObj_getLayer(*args)
    	if layer:
    		if args and len(args)!=0:
    			layer.p_map=args[0]
    		else:
    			layer.p_map=None
    	return layer

    def getLayerByName(*args):
    	layer = _mapscript.mapObj_getLayerByName(*args)
    	if layer:
    		if args and len(args)!=0:
    			layer.p_map=args[0]
    		else:
    			layer.p_map=None
    	return layer

    def getSymbolByName(*args): return _mapscript.mapObj_getSymbolByName(*args)
    def prepareQuery(*args): return _mapscript.mapObj_prepareQuery(*args)
    def prepareImage(*args): return _mapscript.mapObj_prepareImage(*args)
    def setImageType(*args): return _mapscript.mapObj_setImageType(*args)
    def selectOutputFormat(*args): return _mapscript.mapObj_selectOutputFormat(*args)
    def setOutputFormat(*args): return _mapscript.mapObj_setOutputFormat(*args)
    def draw(*args): return _mapscript.mapObj_draw(*args)
    def drawQuery(*args): return _mapscript.mapObj_drawQuery(*args)
    def drawLegend(*args): return _mapscript.mapObj_drawLegend(*args)
    def drawScalebar(*args): return _mapscript.mapObj_drawScalebar(*args)
    def drawReferenceMap(*args): return _mapscript.mapObj_drawReferenceMap(*args)
    def embedScalebar(*args): return _mapscript.mapObj_embedScalebar(*args)
    def embedLegend(*args): return _mapscript.mapObj_embedLegend(*args)
    def drawLabelCache(*args): return _mapscript.mapObj_drawLabelCache(*args)
    def getLabel(*args): return _mapscript.mapObj_getLabel(*args)
    def nextLabel(*args): return _mapscript.mapObj_nextLabel(*args)
    def queryByPoint(*args): return _mapscript.mapObj_queryByPoint(*args)
    def queryByRect(*args): return _mapscript.mapObj_queryByRect(*args)
    def queryByFeatures(*args): return _mapscript.mapObj_queryByFeatures(*args)
    def queryByShape(*args): return _mapscript.mapObj_queryByShape(*args)
    def setWKTProjection(*args): return _mapscript.mapObj_setWKTProjection(*args)
    def getProjection(*args): return _mapscript.mapObj_getProjection(*args)
    def setProjection(*args): return _mapscript.mapObj_setProjection(*args)
    def save(*args): return _mapscript.mapObj_save(*args)
    def saveQuery(*args): return _mapscript.mapObj_saveQuery(*args)
    def loadQuery(*args): return _mapscript.mapObj_loadQuery(*args)
    def freeQuery(*args): return _mapscript.mapObj_freeQuery(*args)
    def saveQueryAsGML(*args): return _mapscript.mapObj_saveQueryAsGML(*args)
    def getMetaData(*args): return _mapscript.mapObj_getMetaData(*args)
    def setMetaData(*args): return _mapscript.mapObj_setMetaData(*args)
    def removeMetaData(*args): return _mapscript.mapObj_removeMetaData(*args)
    def getFirstMetaDataKey(*args): return _mapscript.mapObj_getFirstMetaDataKey(*args)
    def getNextMetaDataKey(*args): return _mapscript.mapObj_getNextMetaDataKey(*args)
    def setSymbolSet(*args): return _mapscript.mapObj_setSymbolSet(*args)
    def getNumSymbols(*args): return _mapscript.mapObj_getNumSymbols(*args)
    def setFontSet(*args): return _mapscript.mapObj_setFontSet(*args)
    def saveMapContext(*args): return _mapscript.mapObj_saveMapContext(*args)
    def loadMapContext(*args): return _mapscript.mapObj_loadMapContext(*args)
    def moveLayerUp(*args): return _mapscript.mapObj_moveLayerUp(*args)
    def moveLayerDown(*args): return _mapscript.mapObj_moveLayerDown(*args)
    def getLayersDrawingOrder(*args): return _mapscript.mapObj_getLayersDrawingOrder(*args)
    def setLayersDrawingOrder(*args): return _mapscript.mapObj_setLayersDrawingOrder(*args)
    def setConfigOption(*args): return _mapscript.mapObj_setConfigOption(*args)
    def getConfigOption(*args): return _mapscript.mapObj_getConfigOption(*args)
    def applyConfigOptions(*args): return _mapscript.mapObj_applyConfigOptions(*args)
    def applySLD(*args): return _mapscript.mapObj_applySLD(*args)
    def applySLDURL(*args): return _mapscript.mapObj_applySLDURL(*args)
    def generateSLD(*args): return _mapscript.mapObj_generateSLD(*args)
    def processTemplate(*args): return _mapscript.mapObj_processTemplate(*args)
    def processLegendTemplate(*args): return _mapscript.mapObj_processLegendTemplate(*args)
    def processQueryTemplate(*args): return _mapscript.mapObj_processQueryTemplate(*args)
    def getOutputFormatByName(*args): return _mapscript.mapObj_getOutputFormatByName(*args)
    def appendOutputFormat(*args): return _mapscript.mapObj_appendOutputFormat(*args)
    def removeOutputFormat(*args): return _mapscript.mapObj_removeOutputFormat(*args)
    def loadOWSParameters(*args): return _mapscript.mapObj_loadOWSParameters(*args)
    def OWSDispatch(*args): return _mapscript.mapObj_OWSDispatch(*args)
    def zoomPoint(*args): return _mapscript.mapObj_zoomPoint(*args)
    def zoomRectangle(*args): return _mapscript.mapObj_zoomRectangle(*args)
    def zoomScale(*args): return _mapscript.mapObj_zoomScale(*args)
    def getLayerOrder(*args): return _mapscript.mapObj_getLayerOrder(*args)
    def setLayerOrder(*args): return _mapscript.mapObj_setLayerOrder(*args)
    def getSize(*args): return _mapscript.mapObj_getSize(*args)
    def get_height(self):
        return self.getSize()[1] # <-- second member is the height
    def get_width(self):
        return self.getSize()[0] # <-- first member is the width
    def set_height(self, value):
        return self.setSize(self.getSize()[0], value)
    def set_width(self, value):
        return self.setSize(value, self.getSize()[1])
    width = property(get_width, set_width)
    height = property(get_height, set_height)



class mapObjPtr(mapObj):
    def __init__(self, this):
        self.this = this
        if not hasattr(self,"thisown"): self.thisown = 0
        self.__class__ = mapObj
_mapscript.mapObj_swigregister(mapObjPtr)

class imageObj(object):
    def __repr__(self):
        return "<C imageObj instance at %s>" % (self.this,)
    width = property(_mapscript.imageObj_width_get)
    height = property(_mapscript.imageObj_height_get)
    imagepath = property(_mapscript.imageObj_imagepath_get)
    imageurl = property(_mapscript.imageObj_imageurl_get)
    format = property(_mapscript.imageObj_format_get)
    buffer_format = property(_mapscript.imageObj_buffer_format_get)
    renderer = property(_mapscript.imageObj_renderer_get, _mapscript.imageObj_renderer_set)
    def __del__(self, destroy=_mapscript.delete_imageObj):
        try:
            if self.thisown: destroy(self)
        except: pass
    def save(*args): return _mapscript.imageObj_save(*args)
    def getBytes(*args): return _mapscript.imageObj_getBytes(*args)
    def getSize(*args): return _mapscript.imageObj_getSize(*args)
    def __init__(self, *args):
        newobj = _mapscript.new_imageObj(*args)
        self.this = newobj.this
        self.thisown = 1
        del newobj.thisown
    def write(*args): return _mapscript.imageObj_write(*args)
    def saveToString(*args): return _mapscript.imageObj_saveToString(*args)

class imageObjPtr(imageObj):
    def __init__(self, this):
        self.this = this
        if not hasattr(self,"thisown"): self.thisown = 0
        self.__class__ = imageObj
_mapscript.imageObj_swigregister(imageObjPtr)


msSaveImage = _mapscript.msSaveImage

msFreeImage = _mapscript.msFreeImage

msSetup = _mapscript.msSetup

msCleanup = _mapscript.msCleanup

msLoadMapFromString = _mapscript.msLoadMapFromString
class rectObj(object):
    def __repr__(self):
        return "<C rectObj instance at %s>" % (self.this,)
    minx = property(_mapscript.rectObj_minx_get, _mapscript.rectObj_minx_set)
    miny = property(_mapscript.rectObj_miny_get, _mapscript.rectObj_miny_set)
    maxx = property(_mapscript.rectObj_maxx_get, _mapscript.rectObj_maxx_set)
    maxy = property(_mapscript.rectObj_maxy_get, _mapscript.rectObj_maxy_set)
    def __init__(self, *args):
        newobj = _mapscript.new_rectObj(*args)
        self.this = newobj.this
        self.thisown = 1
        del newobj.thisown
    def __del__(self, destroy=_mapscript.delete_rectObj):
        try:
            if self.thisown: destroy(self)
        except: pass
    def project(*args): return _mapscript.rectObj_project(*args)
    def fit(*args): return _mapscript.rectObj_fit(*args)
    def draw(*args): return _mapscript.rectObj_draw(*args)
    def getCenter(*args): return _mapscript.rectObj_getCenter(*args)
    def toPolygon(*args): return _mapscript.rectObj_toPolygon(*args)
    def toString(*args): return _mapscript.rectObj_toString(*args)
    def __str__(self):
        return self.toString()
        
    def __contains__(self, item):
        item_type = str(type(item))
        if item_type == "<class 'mapscript.pointObj'>":
            if item.x >= self.minx and item.x <= self.maxx \
            and item.y >= self.miny and item.y <= self.maxy:
                return True
            else:
                return False
        else:
            raise TypeError, \
                '__contains__ does not yet handle %s' % (item_type)
        


class rectObjPtr(rectObj):
    def __init__(self, this):
        self.this = this
        if not hasattr(self,"thisown"): self.thisown = 0
        self.__class__ = rectObj
_mapscript.rectObj_swigregister(rectObjPtr)

class pointObj(object):
    def __repr__(self):
        return "<C pointObj instance at %s>" % (self.this,)
    x = property(_mapscript.pointObj_x_get, _mapscript.pointObj_x_set)
    y = property(_mapscript.pointObj_y_get, _mapscript.pointObj_y_set)
    def __init__(self, *args):
        newobj = _mapscript.new_pointObj(*args)
        self.this = newobj.this
        self.thisown = 1
        del newobj.thisown
    def __del__(self, destroy=_mapscript.delete_pointObj):
        try:
            if self.thisown: destroy(self)
        except: pass
    def project(*args): return _mapscript.pointObj_project(*args)
    def draw(*args): return _mapscript.pointObj_draw(*args)
    def distanceToPoint(*args): return _mapscript.pointObj_distanceToPoint(*args)
    def distanceToSegment(*args): return _mapscript.pointObj_distanceToSegment(*args)
    def distanceToShape(*args): return _mapscript.pointObj_distanceToShape(*args)
    def setXY(*args): return _mapscript.pointObj_setXY(*args)
    def setXYZ(*args): return _mapscript.pointObj_setXYZ(*args)
    def setXYZM(*args): return _mapscript.pointObj_setXYZM(*args)
    def toString(*args): return _mapscript.pointObj_toString(*args)
    def toShape(*args): return _mapscript.pointObj_toShape(*args)
    def __str__(self):
        return self.toString()



class pointObjPtr(pointObj):
    def __init__(self, this):
        self.this = this
        if not hasattr(self,"thisown"): self.thisown = 0
        self.__class__ = pointObj
_mapscript.pointObj_swigregister(pointObjPtr)

class lineObj(object):
    def __repr__(self):
        return "<C lineObj instance at %s>" % (self.this,)
    numpoints = property(_mapscript.lineObj_numpoints_get)
    point = property(_mapscript.lineObj_point_get)
    def __init__(self, *args):
        newobj = _mapscript.new_lineObj(*args)
        self.this = newobj.this
        self.thisown = 1
        del newobj.thisown
    def __del__(self, destroy=_mapscript.delete_lineObj):
        try:
            if self.thisown: destroy(self)
        except: pass
    def project(*args): return _mapscript.lineObj_project(*args)
    def get(*args): return _mapscript.lineObj_get(*args)
    def add(*args): return _mapscript.lineObj_add(*args)
    def set(*args): return _mapscript.lineObj_set(*args)

class lineObjPtr(lineObj):
    def __init__(self, this):
        self.this = this
        if not hasattr(self,"thisown"): self.thisown = 0
        self.__class__ = lineObj
_mapscript.lineObj_swigregister(lineObjPtr)

class shapeObj(object):
    def __repr__(self):
        return "<C shapeObj instance at %s>" % (self.this,)
    numlines = property(_mapscript.shapeObj_numlines_get)
    numvalues = property(_mapscript.shapeObj_numvalues_get)
    line = property(_mapscript.shapeObj_line_get)
    values = property(_mapscript.shapeObj_values_get)
    bounds = property(_mapscript.shapeObj_bounds_get, _mapscript.shapeObj_bounds_set)
    type = property(_mapscript.shapeObj_type_get, _mapscript.shapeObj_type_set)
    index = property(_mapscript.shapeObj_index_get, _mapscript.shapeObj_index_set)
    tileindex = property(_mapscript.shapeObj_tileindex_get, _mapscript.shapeObj_tileindex_set)
    classindex = property(_mapscript.shapeObj_classindex_get, _mapscript.shapeObj_classindex_set)
    text = property(_mapscript.shapeObj_text_get, _mapscript.shapeObj_text_set)
    def __init__(self, *args):
        newobj = _mapscript.new_shapeObj(*args)
        self.this = newobj.this
        self.thisown = 1
        del newobj.thisown
    def __del__(self, destroy=_mapscript.delete_shapeObj):
        try:
            if self.thisown: destroy(self)
        except: pass
    fromWKT = staticmethod(_mapscript.shapeObj_fromWKT)
    def project(*args): return _mapscript.shapeObj_project(*args)
    def get(*args): return _mapscript.shapeObj_get(*args)
    def add(*args): return _mapscript.shapeObj_add(*args)
    def draw(*args): return _mapscript.shapeObj_draw(*args)
    def setBounds(*args): return _mapscript.shapeObj_setBounds(*args)
    def clone(*args): return _mapscript.shapeObj_clone(*args)
    def copy(*args): return _mapscript.shapeObj_copy(*args)
    def toWKT(*args): return _mapscript.shapeObj_toWKT(*args)
    def buffer(*args): return _mapscript.shapeObj_buffer(*args)
    def convexHull(*args): return _mapscript.shapeObj_convexHull(*args)
    def boundary(*args): return _mapscript.shapeObj_boundary(*args)
    def getCentroid(*args): return _mapscript.shapeObj_getCentroid(*args)
    def Union(*args): return _mapscript.shapeObj_Union(*args)
    def intersection(*args): return _mapscript.shapeObj_intersection(*args)
    def difference(*args): return _mapscript.shapeObj_difference(*args)
    def symDifference(*args): return _mapscript.shapeObj_symDifference(*args)
    def overlaps(*args): return _mapscript.shapeObj_overlaps(*args)
    def within(*args): return _mapscript.shapeObj_within(*args)
    def crosses(*args): return _mapscript.shapeObj_crosses(*args)
    def intersects(*args): return _mapscript.shapeObj_intersects(*args)
    def touches(*args): return _mapscript.shapeObj_touches(*args)
    def equals(*args): return _mapscript.shapeObj_equals(*args)
    def disjoint(*args): return _mapscript.shapeObj_disjoint(*args)
    def getArea(*args): return _mapscript.shapeObj_getArea(*args)
    def getLength(*args): return _mapscript.shapeObj_getLength(*args)
    def getValue(*args): return _mapscript.shapeObj_getValue(*args)
    def contains(*args): return _mapscript.shapeObj_contains(*args)
    def distanceToPoint(*args): return _mapscript.shapeObj_distanceToPoint(*args)
    def distanceToShape(*args): return _mapscript.shapeObj_distanceToShape(*args)
    def getLabelPoint(*args): return _mapscript.shapeObj_getLabelPoint(*args)
    def setValue(*args): return _mapscript.shapeObj_setValue(*args)
    def initValues(*args): return _mapscript.shapeObj_initValues(*args)

class shapeObjPtr(shapeObj):
    def __init__(self, this):
        self.this = this
        if not hasattr(self,"thisown"): self.thisown = 0
        self.__class__ = shapeObj
_mapscript.shapeObj_swigregister(shapeObjPtr)

shapeObj_fromWKT = _mapscript.shapeObj_fromWKT

MS_SHAPEFILE_POINT = _mapscript.MS_SHAPEFILE_POINT
MS_SHAPEFILE_ARC = _mapscript.MS_SHAPEFILE_ARC
MS_SHAPEFILE_POLYGON = _mapscript.MS_SHAPEFILE_POLYGON
MS_SHAPEFILE_MULTIPOINT = _mapscript.MS_SHAPEFILE_MULTIPOINT
MS_SHP_POINTZ = _mapscript.MS_SHP_POINTZ
MS_SHP_ARCZ = _mapscript.MS_SHP_ARCZ
MS_SHP_POLYGONZ = _mapscript.MS_SHP_POLYGONZ
MS_SHP_MULTIPOINTZ = _mapscript.MS_SHP_MULTIPOINTZ
MS_SHP_POINTM = _mapscript.MS_SHP_POINTM
MS_SHP_ARCM = _mapscript.MS_SHP_ARCM
MS_SHP_POLYGONM = _mapscript.MS_SHP_POLYGONM
MS_SHP_MULTIPOINTM = _mapscript.MS_SHP_MULTIPOINTM
class DBFInfo(object):
    def __repr__(self):
        return "<C DBFInfo instance at %s>" % (self.this,)
    fp = property(_mapscript.DBFInfo_fp_get)
    nRecords = property(_mapscript.DBFInfo_nRecords_get)
    nRecordLength = property(_mapscript.DBFInfo_nRecordLength_get)
    nHeaderLength = property(_mapscript.DBFInfo_nHeaderLength_get)
    nFields = property(_mapscript.DBFInfo_nFields_get)
    panFieldOffset = property(_mapscript.DBFInfo_panFieldOffset_get)
    panFieldSize = property(_mapscript.DBFInfo_panFieldSize_get)
    panFieldDecimals = property(_mapscript.DBFInfo_panFieldDecimals_get)
    pachFieldType = property(_mapscript.DBFInfo_pachFieldType_get)
    pszHeader = property(_mapscript.DBFInfo_pszHeader_get)
    nCurrentRecord = property(_mapscript.DBFInfo_nCurrentRecord_get)
    bCurrentRecordModified = property(_mapscript.DBFInfo_bCurrentRecordModified_get)
    pszCurrentRecord = property(_mapscript.DBFInfo_pszCurrentRecord_get)
    bNoHeader = property(_mapscript.DBFInfo_bNoHeader_get)
    bUpdated = property(_mapscript.DBFInfo_bUpdated_get)
    pszStringField = property(_mapscript.DBFInfo_pszStringField_get)
    nStringFieldLen = property(_mapscript.DBFInfo_nStringFieldLen_get)
    def getFieldName(*args): return _mapscript.DBFInfo_getFieldName(*args)
    def getFieldWidth(*args): return _mapscript.DBFInfo_getFieldWidth(*args)
    def getFieldDecimals(*args): return _mapscript.DBFInfo_getFieldDecimals(*args)
    def getFieldType(*args): return _mapscript.DBFInfo_getFieldType(*args)
    def __init__(self, *args):
        newobj = _mapscript.new_DBFInfo(*args)
        self.this = newobj.this
        self.thisown = 1
        del newobj.thisown
    def __del__(self, destroy=_mapscript.delete_DBFInfo):
        try:
            if self.thisown: destroy(self)
        except: pass

class DBFInfoPtr(DBFInfo):
    def __init__(self, this):
        self.this = this
        if not hasattr(self,"thisown"): self.thisown = 0
        self.__class__ = DBFInfo
_mapscript.DBFInfo_swigregister(DBFInfoPtr)

FTString = _mapscript.FTString
FTInteger = _mapscript.FTInteger
FTDouble = _mapscript.FTDouble
FTInvalid = _mapscript.FTInvalid
class shapefileObj(object):
    def __repr__(self):
        return "<C shapefileObj instance at %s>" % (self.this,)
    source = property(_mapscript.shapefileObj_source_get)
    type = property(_mapscript.shapefileObj_type_get)
    numshapes = property(_mapscript.shapefileObj_numshapes_get)
    bounds = property(_mapscript.shapefileObj_bounds_get)
    lastshape = property(_mapscript.shapefileObj_lastshape_get)
    status = property(_mapscript.shapefileObj_status_get)
    statusbounds = property(_mapscript.shapefileObj_statusbounds_get)
    isopen = property(_mapscript.shapefileObj_isopen_get)
    def __init__(self, *args):
        newobj = _mapscript.new_shapefileObj(*args)
        self.this = newobj.this
        self.thisown = 1
        del newobj.thisown
    def __del__(self, destroy=_mapscript.delete_shapefileObj):
        try:
            if self.thisown: destroy(self)
        except: pass
    def get(*args): return _mapscript.shapefileObj_get(*args)
    def getShape(*args): return _mapscript.shapefileObj_getShape(*args)
    def getPoint(*args): return _mapscript.shapefileObj_getPoint(*args)
    def getTransformed(*args): return _mapscript.shapefileObj_getTransformed(*args)
    def getExtent(*args): return _mapscript.shapefileObj_getExtent(*args)
    def add(*args): return _mapscript.shapefileObj_add(*args)
    def addPoint(*args): return _mapscript.shapefileObj_addPoint(*args)
    def getDBF(*args): return _mapscript.shapefileObj_getDBF(*args)

class shapefileObjPtr(shapefileObj):
    def __init__(self, this):
        self.this = this
        if not hasattr(self,"thisown"): self.thisown = 0
        self.__class__ = shapefileObj
_mapscript.shapefileObj_swigregister(shapefileObjPtr)

class projectionObj(object):
    def __repr__(self):
        return "<C projectionObj instance at %s>" % (self.this,)
    numargs = property(_mapscript.projectionObj_numargs_get)
    def __init__(self, *args):
        newobj = _mapscript.new_projectionObj(*args)
        self.this = newobj.this
        self.thisown = 1
        del newobj.thisown
    def __del__(self, destroy=_mapscript.delete_projectionObj):
        try:
            if self.thisown: destroy(self)
        except: pass
    def setWKTProjection(*args): return _mapscript.projectionObj_setWKTProjection(*args)

class projectionObjPtr(projectionObj):
    def __init__(self, this):
        self.this = this
        if not hasattr(self,"thisown"): self.thisown = 0
        self.__class__ = projectionObj
_mapscript.projectionObj_swigregister(projectionObjPtr)

MS_SYMBOL_SIMPLE = _mapscript.MS_SYMBOL_SIMPLE
MS_SYMBOL_VECTOR = _mapscript.MS_SYMBOL_VECTOR
MS_SYMBOL_ELLIPSE = _mapscript.MS_SYMBOL_ELLIPSE
MS_SYMBOL_PIXMAP = _mapscript.MS_SYMBOL_PIXMAP
MS_SYMBOL_TRUETYPE = _mapscript.MS_SYMBOL_TRUETYPE
MS_SYMBOL_CARTOLINE = _mapscript.MS_SYMBOL_CARTOLINE
MS_SYMBOL_HATCH = _mapscript.MS_SYMBOL_HATCH
MS_SYMBOL_ALLOCSIZE = _mapscript.MS_SYMBOL_ALLOCSIZE
MS_MAXVECTORPOINTS = _mapscript.MS_MAXVECTORPOINTS
MS_MAXPATTERNLENGTH = _mapscript.MS_MAXPATTERNLENGTH
MS_IMAGECACHESIZE = _mapscript.MS_IMAGECACHESIZE
class colorObj(object):
    def __repr__(self):
        return "<C colorObj instance at %s>" % (self.this,)
    pen = property(_mapscript.colorObj_pen_get, _mapscript.colorObj_pen_set)
    red = property(_mapscript.colorObj_red_get, _mapscript.colorObj_red_set)
    green = property(_mapscript.colorObj_green_get, _mapscript.colorObj_green_set)
    blue = property(_mapscript.colorObj_blue_get, _mapscript.colorObj_blue_set)
    def __init__(self, *args):
        newobj = _mapscript.new_colorObj(*args)
        self.this = newobj.this
        self.thisown = 1
        del newobj.thisown
    def __del__(self, destroy=_mapscript.delete_colorObj):
        try:
            if self.thisown: destroy(self)
        except: pass
    def setRGB(*args): return _mapscript.colorObj_setRGB(*args)
    def setHex(*args): return _mapscript.colorObj_setHex(*args)
    def toHex(*args): return _mapscript.colorObj_toHex(*args)

class colorObjPtr(colorObj):
    def __init__(self, this):
        self.this = this
        if not hasattr(self,"thisown"): self.thisown = 0
        self.__class__ = colorObj
_mapscript.colorObj_swigregister(colorObjPtr)

class symbolObj(object):
    def __repr__(self):
        return "<C symbolObj instance at %s>" % (self.this,)
    name = property(_mapscript.symbolObj_name_get, _mapscript.symbolObj_name_set)
    type = property(_mapscript.symbolObj_type_get, _mapscript.symbolObj_type_set)
    sizex = property(_mapscript.symbolObj_sizex_get, _mapscript.symbolObj_sizex_set)
    sizey = property(_mapscript.symbolObj_sizey_get, _mapscript.symbolObj_sizey_set)
    refcount = property(_mapscript.symbolObj_refcount_get)
    numpoints = property(_mapscript.symbolObj_numpoints_get)
    filled = property(_mapscript.symbolObj_filled_get, _mapscript.symbolObj_filled_set)
    patternlength = property(_mapscript.symbolObj_patternlength_get, _mapscript.symbolObj_patternlength_set)
    pattern = property(_mapscript.symbolObj_pattern_get, _mapscript.symbolObj_pattern_set)
    imagepath = property(_mapscript.symbolObj_imagepath_get)
    transparent = property(_mapscript.symbolObj_transparent_get, _mapscript.symbolObj_transparent_set)
    transparentcolor = property(_mapscript.symbolObj_transparentcolor_get, _mapscript.symbolObj_transparentcolor_set)
    character = property(_mapscript.symbolObj_character_get, _mapscript.symbolObj_character_set)
    antialias = property(_mapscript.symbolObj_antialias_get, _mapscript.symbolObj_antialias_set)
    font = property(_mapscript.symbolObj_font_get, _mapscript.symbolObj_font_set)
    gap = property(_mapscript.symbolObj_gap_get, _mapscript.symbolObj_gap_set)
    position = property(_mapscript.symbolObj_position_get, _mapscript.symbolObj_position_set)
    linecap = property(_mapscript.symbolObj_linecap_get, _mapscript.symbolObj_linecap_set)
    linejoin = property(_mapscript.symbolObj_linejoin_get, _mapscript.symbolObj_linejoin_set)
    linejoinmaxsize = property(_mapscript.symbolObj_linejoinmaxsize_get, _mapscript.symbolObj_linejoinmaxsize_set)
    def __init__(self, *args):
        newobj = _mapscript.new_symbolObj(*args)
        self.this = newobj.this
        self.thisown = 1
        del newobj.thisown
    def __del__(self, destroy=_mapscript.delete_symbolObj):
        try:
            if self.thisown: destroy(self)
        except: pass
    def setImagepath(*args): return _mapscript.symbolObj_setImagepath(*args)
    def setPoints(*args): return _mapscript.symbolObj_setPoints(*args)
    def getPoints(*args): return _mapscript.symbolObj_getPoints(*args)
    def setPattern(*args): return _mapscript.symbolObj_setPattern(*args)
    def getImage(*args): return _mapscript.symbolObj_getImage(*args)
    def setImage(*args): return _mapscript.symbolObj_setImage(*args)

class symbolObjPtr(symbolObj):
    def __init__(self, this):
        self.this = this
        if not hasattr(self,"thisown"): self.thisown = 0
        self.__class__ = symbolObj
_mapscript.symbolObj_swigregister(symbolObjPtr)

MS_NOERR = _mapscript.MS_NOERR
MS_IOERR = _mapscript.MS_IOERR
MS_MEMERR = _mapscript.MS_MEMERR
MS_TYPEERR = _mapscript.MS_TYPEERR
MS_SYMERR = _mapscript.MS_SYMERR
MS_REGEXERR = _mapscript.MS_REGEXERR
MS_TTFERR = _mapscript.MS_TTFERR
MS_DBFERR = _mapscript.MS_DBFERR
MS_GDERR = _mapscript.MS_GDERR
MS_IDENTERR = _mapscript.MS_IDENTERR
MS_EOFERR = _mapscript.MS_EOFERR
MS_PROJERR = _mapscript.MS_PROJERR
MS_MISCERR = _mapscript.MS_MISCERR
MS_CGIERR = _mapscript.MS_CGIERR
MS_WEBERR = _mapscript.MS_WEBERR
MS_IMGERR = _mapscript.MS_IMGERR
MS_HASHERR = _mapscript.MS_HASHERR
MS_JOINERR = _mapscript.MS_JOINERR
MS_NOTFOUND = _mapscript.MS_NOTFOUND
MS_SHPERR = _mapscript.MS_SHPERR
MS_PARSEERR = _mapscript.MS_PARSEERR
MS_SDEERR = _mapscript.MS_SDEERR
MS_OGRERR = _mapscript.MS_OGRERR
MS_QUERYERR = _mapscript.MS_QUERYERR
MS_WMSERR = _mapscript.MS_WMSERR
MS_WMSCONNERR = _mapscript.MS_WMSCONNERR
MS_ORACLESPATIALERR = _mapscript.MS_ORACLESPATIALERR
MS_WFSERR = _mapscript.MS_WFSERR
MS_WFSCONNERR = _mapscript.MS_WFSCONNERR
MS_MAPCONTEXTERR = _mapscript.MS_MAPCONTEXTERR
MS_HTTPERR = _mapscript.MS_HTTPERR
MS_CHILDERR = _mapscript.MS_CHILDERR
MS_WCSERR = _mapscript.MS_WCSERR
MS_GEOSERR = _mapscript.MS_GEOSERR
MS_RECTERR = _mapscript.MS_RECTERR
MS_TIMEERR = _mapscript.MS_TIMEERR
MS_GMLERR = _mapscript.MS_GMLERR
MS_SOSERR = _mapscript.MS_SOSERR
MS_NULLPARENTERR = _mapscript.MS_NULLPARENTERR
MS_AGGERR = _mapscript.MS_AGGERR
MS_NUMERRORCODES = _mapscript.MS_NUMERRORCODES
MESSAGELENGTH = _mapscript.MESSAGELENGTH
ROUTINELENGTH = _mapscript.ROUTINELENGTH
MS_ERROR_LANGUAGE = _mapscript.MS_ERROR_LANGUAGE
class errorObj(object):
    def __repr__(self):
        return "<C errorObj instance at %s>" % (self.this,)
    code = property(_mapscript.errorObj_code_get, _mapscript.errorObj_code_set)
    routine = property(_mapscript.errorObj_routine_get, _mapscript.errorObj_routine_set)
    message = property(_mapscript.errorObj_message_get, _mapscript.errorObj_message_set)
    def __init__(self, *args):
        newobj = _mapscript.new_errorObj(*args)
        self.this = newobj.this
        self.thisown = 1
        del newobj.thisown
    def __del__(self, destroy=_mapscript.delete_errorObj):
        try:
            if self.thisown: destroy(self)
        except: pass
    def next(*args): return _mapscript.errorObj_next(*args)

class errorObjPtr(errorObj):
    def __init__(self, this):
        self.this = this
        if not hasattr(self,"thisown"): self.thisown = 0
        self.__class__ = errorObj
_mapscript.errorObj_swigregister(errorObjPtr)


msGetErrorObj = _mapscript.msGetErrorObj

msResetErrorList = _mapscript.msResetErrorList

msGetVersion = _mapscript.msGetVersion

msGetVersionInt = _mapscript.msGetVersionInt

msGetErrorString = _mapscript.msGetErrorString
MS_DEBUGLEVEL_ERRORSONLY = _mapscript.MS_DEBUGLEVEL_ERRORSONLY
MS_DEBUGLEVEL_DEBUG = _mapscript.MS_DEBUGLEVEL_DEBUG
MS_DEBUGLEVEL_TUNING = _mapscript.MS_DEBUGLEVEL_TUNING
MS_DEBUGLEVEL_V = _mapscript.MS_DEBUGLEVEL_V
MS_DEBUGLEVEL_VV = _mapscript.MS_DEBUGLEVEL_VV
MS_DEBUGLEVEL_VVV = _mapscript.MS_DEBUGLEVEL_VVV
MS_HASHSIZE = _mapscript.MS_HASHSIZE
class hashTableObj(object):
    def __repr__(self):
        return "<C hashTableObj instance at %s>" % (self.this,)
    numitems = property(_mapscript.hashTableObj_numitems_get)
    def __init__(self, *args):
        newobj = _mapscript.new_hashTableObj(*args)
        self.this = newobj.this
        self.thisown = 1
        del newobj.thisown
    def __del__(self, destroy=_mapscript.delete_hashTableObj):
        try:
            if self.thisown: destroy(self)
        except: pass
    def set(*args): return _mapscript.hashTableObj_set(*args)
    def get(*args): return _mapscript.hashTableObj_get(*args)
    def remove(*args): return _mapscript.hashTableObj_remove(*args)
    def clear(*args): return _mapscript.hashTableObj_clear(*args)
    def nextKey(*args): return _mapscript.hashTableObj_nextKey(*args)

class hashTableObjPtr(hashTableObj):
    def __init__(self, this):
        self.this = this
        if not hasattr(self,"thisown"): self.thisown = 0
        self.__class__ = hashTableObj
_mapscript.hashTableObj_swigregister(hashTableObjPtr)

MS_MAX_CGI_PARAMS = _mapscript.MS_MAX_CGI_PARAMS
MS_GET_REQUEST = _mapscript.MS_GET_REQUEST
MS_POST_REQUEST = _mapscript.MS_POST_REQUEST
class OWSRequest(object):
    def __repr__(self):
        return "<C cgiRequestObj instance at %s>" % (self.this,)
    NumParams = property(_mapscript.OWSRequest_NumParams_get)
    type = property(_mapscript.OWSRequest_type_get, _mapscript.OWSRequest_type_set)
    contenttype = property(_mapscript.OWSRequest_contenttype_get, _mapscript.OWSRequest_contenttype_set)
    postrequest = property(_mapscript.OWSRequest_postrequest_get, _mapscript.OWSRequest_postrequest_set)
    def __init__(self, *args):
        newobj = _mapscript.new_OWSRequest(*args)
        self.this = newobj.this
        self.thisown = 1
        del newobj.thisown
    def __del__(self, destroy=_mapscript.delete_OWSRequest):
        try:
            if self.thisown: destroy(self)
        except: pass
    def loadParams(*args): return _mapscript.OWSRequest_loadParams(*args)
    def setParameter(*args): return _mapscript.OWSRequest_setParameter(*args)
    def getName(*args): return _mapscript.OWSRequest_getName(*args)
    def getValue(*args): return _mapscript.OWSRequest_getValue(*args)
    def getValueByName(*args): return _mapscript.OWSRequest_getValueByName(*args)

class OWSRequestPtr(OWSRequest):
    def __init__(self, this):
        self.this = this
        if not hasattr(self,"thisown"): self.thisown = 0
        self.__class__ = OWSRequest
_mapscript.OWSRequest_swigregister(OWSRequestPtr)


msConnPoolCloseUnreferenced = _mapscript.msConnPoolCloseUnreferenced

msIO_resetHandlers = _mapscript.msIO_resetHandlers

msIO_installStdoutToBuffer = _mapscript.msIO_installStdoutToBuffer

msIO_installStdinFromBuffer = _mapscript.msIO_installStdinFromBuffer

msIO_stripStdoutBufferContentType = _mapscript.msIO_stripStdoutBufferContentType

msIO_getStdoutBufferString = _mapscript.msIO_getStdoutBufferString

msIO_getStdoutBufferBytes = _mapscript.msIO_getStdoutBufferBytes
def fromstring(data, mappath=None):
    """Creates map objects from mapfile strings.

    Parameters
    ==========
    data : string
        Mapfile in a string.
    mappath : string
        Optional root map path, enabling relative paths in mapfile.

    Example
    =======
    >>> mo = fromstring("MAP\nNAME 'test'\nEND")
    >>> mo.name
    'test'
    """
    import re
    if re.search("^\s*MAP", data, re.I): 
        return msLoadMapFromString(data, mappath)
    elif re.search("^\s*LAYER", data, re.I):
        ob = layerObj()
        ob.updateFromString(data)
        return ob
    elif re.search("^\s*CLASS", data, re.I):
        ob = classObj()
        ob.updateFromString(data)
        return ob
    elif re.search("^\s*STYLE", data, re.I):
        ob = styleObj()
        ob.updateFromString(data)
        return ob
    else:
        raise ValueError, "No map, layer, class, or style found. Can not load from provided string"


