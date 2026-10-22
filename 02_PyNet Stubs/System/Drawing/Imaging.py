# encoding: utf-8
# module System.Drawing.Imaging calls itself Imaging
# from System.Drawing, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b03f5f7f11d50a3a
# by generator 1.145
""" NamespaceTracker represent a CLS namespace. """
# no imports

# no functions
# classes

class BitmapData(object):
    """
    Specifies the attributes of a bitmap image. The System.Drawing.Imaging.BitmapData class is used by the erload:System.Drawing.Bitmap.LockBits and System.Drawing.Bitmap.UnlockBits(System.Drawing.Imaging.BitmapData) methods of the System.Drawing.Bitmap class. Not inheritable.

    

    BitmapData()
    """
    Height = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the pixel height of the System.Drawing.Bitmap object. Also sometimes referred to as the number of scan lines.



Get: Height(self: BitmapData) -> int



Set: Height(self: BitmapData) = value

"""

    PixelFormat = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the format of the pixel information in the System.Drawing.Bitmap object that returned this System.Drawing.Imaging.BitmapData object.



Get: PixelFormat(self: BitmapData) -> PixelFormat



Set: PixelFormat(self: BitmapData) = value

"""

    Reserved = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Reserved. Do not use.



Get: Reserved(self: BitmapData) -> int



Set: Reserved(self: BitmapData) = value

"""

    Scan0 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the address of the first pixel data in the bitmap. This can also be thought of as the first scan line in the bitmap.



Get: Scan0(self: BitmapData) -> IntPtr



Set: Scan0(self: BitmapData) = value

"""

    Stride = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the stride width (also called scan width) of the System.Drawing.Bitmap object.



Get: Stride(self: BitmapData) -> int



Set: Stride(self: BitmapData) = value

"""

    Width = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the pixel width of the System.Drawing.Bitmap object. This can also be thought of as the number of pixels in one scan line.



Get: Width(self: BitmapData) -> int



Set: Width(self: BitmapData) = value

"""



class ColorAdjustType:
    """.NET enum: System.Drawing.Imaging.ColorAdjustType"""
    def __init__(self, *args) -> None: ...
    Default: int  # = 0
    Bitmap: int  # = 1
    Brush: int  # = 2
    Pen: int  # = 3
    Text: int  # = 4
    Count: int  # = 5
    Any: int  # = 6
class ColorChannelFlag:
    """.NET enum: System.Drawing.Imaging.ColorChannelFlag"""
    def __init__(self, *args) -> None: ...
    ColorChannelC: int  # = 0
    ColorChannelM: int  # = 1
    ColorChannelY: int  # = 2
    ColorChannelK: int  # = 3
    ColorChannelLast: int  # = 4
class ColorMap(object):
    """
    Defines a map for converting colors. Several methods of the System.Drawing.Imaging.ImageAttributes class adjust image colors by using a color-remap table, which is an array of System.Drawing.Imaging.ColorMap structures. Not inheritable.

    

    ColorMap()
    """
    NewColor = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the new System.Drawing.Color structure to which to convert.



Get: NewColor(self: ColorMap) -> Color



Set: NewColor(self: ColorMap) = value

"""

    OldColor = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the existing System.Drawing.Color structure to be converted.



Get: OldColor(self: ColorMap) -> Color



Set: OldColor(self: ColorMap) = value

"""



class ColorMapType:
    """.NET enum: System.Drawing.Imaging.ColorMapType"""
    def __init__(self, *args) -> None: ...
    Default: int  # = 0
    Brush: int  # = 1
class ColorMatrix(object):
    """
    Defines a 5 x 5 matrix that contains the coordinates for the RGBAW space. Several methods of the System.Drawing.Imaging.ImageAttributes class adjust image colors by using a color matrix. This class cannot be inherited.

    

    ColorMatrix()

    ColorMatrix(newColorMatrix: Array[Array[Single]])
    """
    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        pass

    @staticmethod # known case of __new__
    def __new__(self, newColorMatrix=None):
        """
        __new__(cls: type)

        __new__(cls: type, newColorMatrix: Array[Array[Single]])
        """
        pass

    def __setitem__(self, *args): #cannot find CLR method
        """ x.__setitem__(i, y) <==> x[i]= """
        pass

    Matrix00 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the element at the 0 (zero) row and 0 column of this System.Drawing.Imaging.ColorMatrix.



Get: Matrix00(self: ColorMatrix) -> Single



Set: Matrix00(self: ColorMatrix) = value

"""

    Matrix01 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the element at the 0 (zero) row and first column of this System.Drawing.Imaging.ColorMatrix.



Get: Matrix01(self: ColorMatrix) -> Single



Set: Matrix01(self: ColorMatrix) = value

"""

    Matrix02 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the element at the 0 (zero) row and second column of this System.Drawing.Imaging.ColorMatrix.



Get: Matrix02(self: ColorMatrix) -> Single



Set: Matrix02(self: ColorMatrix) = value

"""

    Matrix03 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the element at the 0 (zero) row and third column of this System.Drawing.Imaging.ColorMatrix. Represents the alpha component.



Get: Matrix03(self: ColorMatrix) -> Single



Set: Matrix03(self: ColorMatrix) = value

"""

    Matrix04 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the element at the 0 (zero) row and fourth column of this System.Drawing.Imaging.ColorMatrix.



Get: Matrix04(self: ColorMatrix) -> Single



Set: Matrix04(self: ColorMatrix) = value

"""

    Matrix10 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the element at the first row and 0 (zero) column of this System.Drawing.Imaging.ColorMatrix.



Get: Matrix10(self: ColorMatrix) -> Single



Set: Matrix10(self: ColorMatrix) = value

"""

    Matrix11 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the element at the first row and first column of this System.Drawing.Imaging.ColorMatrix.



Get: Matrix11(self: ColorMatrix) -> Single



Set: Matrix11(self: ColorMatrix) = value

"""

    Matrix12 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the element at the first row and second column of this System.Drawing.Imaging.ColorMatrix.



Get: Matrix12(self: ColorMatrix) -> Single



Set: Matrix12(self: ColorMatrix) = value

"""

    Matrix13 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the element at the first row and third column of this System.Drawing.Imaging.ColorMatrix. Represents the alpha component.



Get: Matrix13(self: ColorMatrix) -> Single



Set: Matrix13(self: ColorMatrix) = value

"""

    Matrix14 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the element at the first row and fourth column of this System.Drawing.Imaging.ColorMatrix.



Get: Matrix14(self: ColorMatrix) -> Single



Set: Matrix14(self: ColorMatrix) = value

"""

    Matrix20 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the element at the second row and 0 (zero) column of this System.Drawing.Imaging.ColorMatrix.



Get: Matrix20(self: ColorMatrix) -> Single



Set: Matrix20(self: ColorMatrix) = value

"""

    Matrix21 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the element at the second row and first column of this System.Drawing.Imaging.ColorMatrix.



Get: Matrix21(self: ColorMatrix) -> Single



Set: Matrix21(self: ColorMatrix) = value

"""

    Matrix22 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the element at the second row and second column of this System.Drawing.Imaging.ColorMatrix.



Get: Matrix22(self: ColorMatrix) -> Single



Set: Matrix22(self: ColorMatrix) = value

"""

    Matrix23 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the element at the second row and third column of this System.Drawing.Imaging.ColorMatrix.



Get: Matrix23(self: ColorMatrix) -> Single



Set: Matrix23(self: ColorMatrix) = value

"""

    Matrix24 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the element at the second row and fourth column of this System.Drawing.Imaging.ColorMatrix.



Get: Matrix24(self: ColorMatrix) -> Single



Set: Matrix24(self: ColorMatrix) = value

"""

    Matrix30 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the element at the third row and 0 (zero) column of this System.Drawing.Imaging.ColorMatrix.



Get: Matrix30(self: ColorMatrix) -> Single



Set: Matrix30(self: ColorMatrix) = value

"""

    Matrix31 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the element at the third row and first column of this System.Drawing.Imaging.ColorMatrix.



Get: Matrix31(self: ColorMatrix) -> Single



Set: Matrix31(self: ColorMatrix) = value

"""

    Matrix32 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the element at the third row and second column of this System.Drawing.Imaging.ColorMatrix.



Get: Matrix32(self: ColorMatrix) -> Single



Set: Matrix32(self: ColorMatrix) = value

"""

    Matrix33 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the element at the third row and third column of this System.Drawing.Imaging.ColorMatrix. Represents the alpha component.



Get: Matrix33(self: ColorMatrix) -> Single



Set: Matrix33(self: ColorMatrix) = value

"""

    Matrix34 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the element at the third row and fourth column of this System.Drawing.Imaging.ColorMatrix.



Get: Matrix34(self: ColorMatrix) -> Single



Set: Matrix34(self: ColorMatrix) = value

"""

    Matrix40 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the element at the fourth row and 0 (zero) column of this System.Drawing.Imaging.ColorMatrix.



Get: Matrix40(self: ColorMatrix) -> Single



Set: Matrix40(self: ColorMatrix) = value

"""

    Matrix41 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the element at the fourth row and first column of this System.Drawing.Imaging.ColorMatrix.



Get: Matrix41(self: ColorMatrix) -> Single



Set: Matrix41(self: ColorMatrix) = value

"""

    Matrix42 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the element at the fourth row and second column of this System.Drawing.Imaging.ColorMatrix.



Get: Matrix42(self: ColorMatrix) -> Single



Set: Matrix42(self: ColorMatrix) = value

"""

    Matrix43 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the element at the fourth row and third column of this System.Drawing.Imaging.ColorMatrix. Represents the alpha component.



Get: Matrix43(self: ColorMatrix) -> Single



Set: Matrix43(self: ColorMatrix) = value

"""

    Matrix44 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the element at the fourth row and fourth column of this System.Drawing.Imaging.ColorMatrix.



Get: Matrix44(self: ColorMatrix) -> Single



Set: Matrix44(self: ColorMatrix) = value

"""



class ColorMatrixFlag:
    """.NET enum: System.Drawing.Imaging.ColorMatrixFlag"""
    def __init__(self, *args) -> None: ...
    Default: int  # = 0
    SkipGrays: int  # = 1
    AltGrays: int  # = 2
class ColorMode:
    """.NET enum: System.Drawing.Imaging.ColorMode"""
    def __init__(self, *args) -> None: ...
    Argb32Mode: int  # = 0
    Argb64Mode: int  # = 1
class ColorPalette(object):
    """ Defines an array of colors that make up a color palette. The colors are 32-bit ARGB colors. Not inheritable. """
    Entries = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets an array of System.Drawing.Color structures.



Get: Entries(self: ColorPalette) -> Array[Color]



"""

    Flags = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value that specifies how to interpret the color information in the array of colors.



Get: Flags(self: ColorPalette) -> int



"""



class EmfPlusRecordType:
    """.NET enum: System.Drawing.Imaging.EmfPlusRecordType"""
    def __init__(self, *args) -> None: ...
    EmfHeader: int  # = 1
    EmfMin: int  # = 1
    EmfPolyBezier: int  # = 2
    EmfPolygon: int  # = 3
    EmfPolyline: int  # = 4
    EmfPolyBezierTo: int  # = 5
    EmfPolyLineTo: int  # = 6
    EmfPolyPolyline: int  # = 7
    EmfPolyPolygon: int  # = 8
    EmfSetWindowExtEx: int  # = 9
    EmfSetWindowOrgEx: int  # = 10
    EmfSetViewportExtEx: int  # = 11
    EmfSetViewportOrgEx: int  # = 12
    EmfSetBrushOrgEx: int  # = 13
    EmfEof: int  # = 14
    EmfSetPixelV: int  # = 15
    EmfSetMapperFlags: int  # = 16
    EmfSetMapMode: int  # = 17
    EmfSetBkMode: int  # = 18
    EmfSetPolyFillMode: int  # = 19
    EmfSetROP2: int  # = 20
    EmfSetStretchBltMode: int  # = 21
    EmfSetTextAlign: int  # = 22
    EmfSetColorAdjustment: int  # = 23
    EmfSetTextColor: int  # = 24
    EmfSetBkColor: int  # = 25
    EmfOffsetClipRgn: int  # = 26
    EmfMoveToEx: int  # = 27
    EmfSetMetaRgn: int  # = 28
    EmfExcludeClipRect: int  # = 29
    EmfIntersectClipRect: int  # = 30
    EmfScaleViewportExtEx: int  # = 31
    EmfScaleWindowExtEx: int  # = 32
    EmfSaveDC: int  # = 33
    EmfRestoreDC: int  # = 34
    EmfSetWorldTransform: int  # = 35
    EmfModifyWorldTransform: int  # = 36
    EmfSelectObject: int  # = 37
    EmfCreatePen: int  # = 38
    EmfCreateBrushIndirect: int  # = 39
    EmfDeleteObject: int  # = 40
    EmfAngleArc: int  # = 41
    EmfEllipse: int  # = 42
    EmfRectangle: int  # = 43
    EmfRoundRect: int  # = 44
    EmfRoundArc: int  # = 45
    EmfChord: int  # = 46
    EmfPie: int  # = 47
    EmfSelectPalette: int  # = 48
    EmfCreatePalette: int  # = 49
    EmfSetPaletteEntries: int  # = 50
    EmfResizePalette: int  # = 51
    EmfRealizePalette: int  # = 52
    EmfExtFloodFill: int  # = 53
    EmfLineTo: int  # = 54
    EmfArcTo: int  # = 55
    EmfPolyDraw: int  # = 56
    EmfSetArcDirection: int  # = 57
    EmfSetMiterLimit: int  # = 58
    EmfBeginPath: int  # = 59
    EmfEndPath: int  # = 60
    EmfCloseFigure: int  # = 61
    EmfFillPath: int  # = 62
    EmfStrokeAndFillPath: int  # = 63
    EmfStrokePath: int  # = 64
    EmfFlattenPath: int  # = 65
    EmfWidenPath: int  # = 66
    EmfSelectClipPath: int  # = 67
    EmfAbortPath: int  # = 68
    EmfReserved069: int  # = 69
    EmfGdiComment: int  # = 70
    EmfFillRgn: int  # = 71
    EmfFrameRgn: int  # = 72
    EmfInvertRgn: int  # = 73
    EmfPaintRgn: int  # = 74
    EmfExtSelectClipRgn: int  # = 75
    EmfBitBlt: int  # = 76
    EmfStretchBlt: int  # = 77
    EmfMaskBlt: int  # = 78
    EmfPlgBlt: int  # = 79
    EmfSetDIBitsToDevice: int  # = 80
    EmfStretchDIBits: int  # = 81
    EmfExtCreateFontIndirect: int  # = 82
    EmfExtTextOutA: int  # = 83
    EmfExtTextOutW: int  # = 84
    EmfPolyBezier16: int  # = 85
    EmfPolygon16: int  # = 86
    EmfPolyline16: int  # = 87
    EmfPolyBezierTo16: int  # = 88
    EmfPolylineTo16: int  # = 89
    EmfPolyPolyline16: int  # = 90
    EmfPolyPolygon16: int  # = 91
    EmfPolyDraw16: int  # = 92
    EmfCreateMonoBrush: int  # = 93
    EmfCreateDibPatternBrushPt: int  # = 94
    EmfExtCreatePen: int  # = 95
    EmfPolyTextOutA: int  # = 96
    EmfPolyTextOutW: int  # = 97
    EmfSetIcmMode: int  # = 98
    EmfCreateColorSpace: int  # = 99
    EmfSetColorSpace: int  # = 100
    EmfDeleteColorSpace: int  # = 101
    EmfGlsRecord: int  # = 102
    EmfGlsBoundedRecord: int  # = 103
    EmfPixelFormat: int  # = 104
    EmfDrawEscape: int  # = 105
    EmfExtEscape: int  # = 106
    EmfStartDoc: int  # = 107
    EmfSmallTextOut: int  # = 108
    EmfForceUfiMapping: int  # = 109
    EmfNamedEscpae: int  # = 110
    EmfColorCorrectPalette: int  # = 111
    EmfSetIcmProfileA: int  # = 112
    EmfSetIcmProfileW: int  # = 113
    EmfAlphaBlend: int  # = 114
    EmfSetLayout: int  # = 115
    EmfTransparentBlt: int  # = 116
    EmfReserved117: int  # = 117
    EmfGradientFill: int  # = 118
    EmfSetLinkedUfis: int  # = 119
    EmfSetTextJustification: int  # = 120
    EmfColorMatchToTargetW: int  # = 121
    EmfCreateColorSpaceW: int  # = 122
    EmfMax: int  # = 122
    EmfPlusRecordBase: int  # = 16384
    Invalid: int  # = 16384
    Header: int  # = 16385
    Min: int  # = 16385
    EndOfFile: int  # = 16386
    Comment: int  # = 16387
    GetDC: int  # = 16388
    MultiFormatStart: int  # = 16389
    MultiFormatSection: int  # = 16390
    MultiFormatEnd: int  # = 16391
    Object: int  # = 16392
    Clear: int  # = 16393
    FillRects: int  # = 16394
    DrawRects: int  # = 16395
    FillPolygon: int  # = 16396
    DrawLines: int  # = 16397
    FillEllipse: int  # = 16398
    DrawEllipse: int  # = 16399
    FillPie: int  # = 16400
    DrawPie: int  # = 16401
    DrawArc: int  # = 16402
    FillRegion: int  # = 16403
    FillPath: int  # = 16404
    DrawPath: int  # = 16405
    FillClosedCurve: int  # = 16406
    DrawClosedCurve: int  # = 16407
    DrawCurve: int  # = 16408
    DrawBeziers: int  # = 16409
    DrawImage: int  # = 16410
    DrawImagePoints: int  # = 16411
    DrawString: int  # = 16412
    SetRenderingOrigin: int  # = 16413
    SetAntiAliasMode: int  # = 16414
    SetTextRenderingHint: int  # = 16415
    SetTextContrast: int  # = 16416
    SetInterpolationMode: int  # = 16417
    SetPixelOffsetMode: int  # = 16418
    SetCompositingMode: int  # = 16419
    SetCompositingQuality: int  # = 16420
    Save: int  # = 16421
    Restore: int  # = 16422
    BeginContainer: int  # = 16423
    BeginContainerNoParams: int  # = 16424
    EndContainer: int  # = 16425
    SetWorldTransform: int  # = 16426
    ResetWorldTransform: int  # = 16427
    MultiplyWorldTransform: int  # = 16428
    TranslateWorldTransform: int  # = 16429
    ScaleWorldTransform: int  # = 16430
    RotateWorldTransform: int  # = 16431
    SetPageTransform: int  # = 16432
    ResetClip: int  # = 16433
    SetClipRect: int  # = 16434
    SetClipPath: int  # = 16435
    SetClipRegion: int  # = 16436
    OffsetClip: int  # = 16437
    Max: int  # = 16438
    DrawDriverString: int  # = 16438
    Total: int  # = 16439
    WmfRecordBase: int  # = 65536
    WmfSaveDC: int  # = 65566
    WmfRealizePalette: int  # = 65589
    WmfSetPalEntries: int  # = 65591
    WmfCreatePalette: int  # = 65783
    WmfSetBkMode: int  # = 65794
    WmfSetMapMode: int  # = 65795
    WmfSetROP2: int  # = 65796
    WmfSetRelAbs: int  # = 65797
    WmfSetPolyFillMode: int  # = 65798
    WmfSetStretchBltMode: int  # = 65799
    WmfSetTextCharExtra: int  # = 65800
    WmfRestoreDC: int  # = 65831
    WmfInvertRegion: int  # = 65834
    WmfPaintRegion: int  # = 65835
    WmfSelectClipRegion: int  # = 65836
    WmfSelectObject: int  # = 65837
    WmfSetTextAlign: int  # = 65838
    WmfResizePalette: int  # = 65849
    WmfDibCreatePatternBrush: int  # = 65858
    WmfSetLayout: int  # = 65865
    WmfDeleteObject: int  # = 66032
    WmfCreatePatternBrush: int  # = 66041
    WmfSetBkColor: int  # = 66049
    WmfSetTextColor: int  # = 66057
    WmfSetTextJustification: int  # = 66058
    WmfSetWindowOrg: int  # = 66059
    WmfSetWindowExt: int  # = 66060
    WmfSetViewportOrg: int  # = 66061
    WmfSetViewportExt: int  # = 66062
    WmfOffsetWindowOrg: int  # = 66063
    WmfOffsetViewportOrg: int  # = 66065
    WmfLineTo: int  # = 66067
    WmfMoveTo: int  # = 66068
    WmfOffsetCilpRgn: int  # = 66080
    WmfFillRegion: int  # = 66088
    WmfSetMapperFlags: int  # = 66097
    WmfSelectPalette: int  # = 66100
    WmfCreatePenIndirect: int  # = 66298
    WmfCreateFontIndirect: int  # = 66299
    WmfCreateBrushIndirect: int  # = 66300
    WmfPolygon: int  # = 66340
    WmfPolyline: int  # = 66341
    WmfScaleWindowExt: int  # = 66576
    WmfScaleViewportExt: int  # = 66578
    WmfExcludeClipRect: int  # = 66581
    WmfIntersectClipRect: int  # = 66582
    WmfEllipse: int  # = 66584
    WmfFloodFill: int  # = 66585
    WmfRectangle: int  # = 66587
    WmfSetPixel: int  # = 66591
    WmfFrameRegion: int  # = 66601
    WmfAnimatePalette: int  # = 66614
    WmfTextOut: int  # = 66849
    WmfPolyPolygon: int  # = 66872
    WmfExtFloodFill: int  # = 66888
    WmfRoundRect: int  # = 67100
    WmfPatBlt: int  # = 67101
    WmfEscape: int  # = 67110
    WmfCreateRegion: int  # = 67327
    WmfArc: int  # = 67607
    WmfPie: int  # = 67610
    WmfChord: int  # = 67632
    WmfBitBlt: int  # = 67874
    WmfDibBitBlt: int  # = 67904
    WmfExtTextOut: int  # = 68146
    WmfStretchBlt: int  # = 68387
    WmfDibStretchBlt: int  # = 68417
    WmfSetDibToDev: int  # = 68915
    WmfStretchDib: int  # = 69443
class EmfType:
    """.NET enum: System.Drawing.Imaging.EmfType"""
    def __init__(self, *args) -> None: ...
    EmfOnly: int  # = 3
    EmfPlusOnly: int  # = 4
    EmfPlusDual: int  # = 5
class Encoder(object):
    """
    An System.Drawing.Imaging.Encoder object encapsulates a globally unique identifier (GUID) that identifies the category of an image encoder parameter.

    

    Encoder(guid: Guid)
    """
    @staticmethod # known case of __new__
    def __new__(self, guid):
        """ __new__(cls: type, guid: Guid) """
        pass

    Guid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a globally unique identifier (GUID) that identifies an image encoder parameter category.



Get: Guid(self: Encoder) -> Guid



"""


    ChrominanceTable = None
    ColorDepth = None
    Compression = None
    LuminanceTable = None
    Quality = None
    RenderMethod = None
    SaveFlag = None
    ScanMethod = None
    Transformation = None
    Version = None


class EncoderParameter(object, IDisposable):
    """
    Used to pass a value, or an array of values, to an image encoder.

    

    EncoderParameter(encoder: Encoder, value: Byte)

    EncoderParameter(encoder: Encoder, value: Byte, undefined: bool)

    EncoderParameter(encoder: Encoder, value: Int16)

    EncoderParameter(encoder: Encoder, value: Int64)

    EncoderParameter(encoder: Encoder, numerator: int, denominator: int)

    EncoderParameter(encoder: Encoder, rangebegin: Int64, rangeend: Int64)

    EncoderParameter(encoder: Encoder, numerator1: int, demoninator1: int, numerator2: int, demoninator2: int)

    EncoderParameter(encoder: Encoder, value: str)

    EncoderParameter(encoder: Encoder, value: Array[Byte])

    EncoderParameter(encoder: Encoder, value: Array[Byte], undefined: bool)

    EncoderParameter(encoder: Encoder, value: Array[Int16])

    EncoderParameter(encoder: Encoder, value: Array[Int64])

    EncoderParameter(encoder: Encoder, numerator: Array[int], denominator: Array[int])

    EncoderParameter(encoder: Encoder, rangebegin: Array[Int64], rangeend: Array[Int64])

    EncoderParameter(encoder: Encoder, numerator1: Array[int], denominator1: Array[int], numerator2: Array[int], denominator2: Array[int])

    EncoderParameter(encoder: Encoder, NumberOfValues: int, Type: int, Value: int)

    EncoderParameter(encoder: Encoder, numberValues: int, type: EncoderParameterValueType, value: IntPtr)
    """
    def Dispose(self):
        """
        Dispose(self: EncoderParameter)

            Releases all resources used by this System.Drawing.Imaging.EncoderParameter object.
        """
        pass

    def __enter__(self, *args): #cannot find CLR method
        """
        __enter__(self: IDisposable) -> object

        

            Provides the implementation of __enter__ for objects which implement IDisposable.
        """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """
        __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object)

            Provides the implementation of __exit__ for objects which implement IDisposable.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, encoder, *__args):
        """
        __new__(cls: type, encoder: Encoder, value: Byte)

        __new__(cls: type, encoder: Encoder, value: Byte, undefined: bool)

        __new__(cls: type, encoder: Encoder, value: Int16)

        __new__(cls: type, encoder: Encoder, value: Int64)

        __new__(cls: type, encoder: Encoder, numerator: int, denominator: int)

        __new__(cls: type, encoder: Encoder, rangebegin: Int64, rangeend: Int64)

        __new__(cls: type, encoder: Encoder, numerator1: int, demoninator1: int, numerator2: int, demoninator2: int)

        __new__(cls: type, encoder: Encoder, value: str)

        __new__(cls: type, encoder: Encoder, value: Array[Byte])

        __new__(cls: type, encoder: Encoder, value: Array[Byte], undefined: bool)

        __new__(cls: type, encoder: Encoder, value: Array[Int16])

        __new__(cls: type, encoder: Encoder, value: Array[Int64])

        __new__(cls: type, encoder: Encoder, numerator: Array[int], denominator: Array[int])

        __new__(cls: type, encoder: Encoder, rangebegin: Array[Int64], rangeend: Array[Int64])

        __new__(cls: type, encoder: Encoder, numerator1: Array[int], denominator1: Array[int], numerator2: Array[int], denominator2: Array[int])

        __new__(cls: type, encoder: Encoder, NumberOfValues: int, Type: int, Value: int)

        __new__(cls: type, encoder: Encoder, numberValues: int, type: EncoderParameterValueType, value: IntPtr)
        """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    Encoder = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the System.Drawing.Imaging.Encoder object associated with this System.Drawing.Imaging.EncoderParameter object. The System.Drawing.Imaging.Encoder object encapsulates the globally unique identifier (GUID) that specifies the category (for example System.Drawing.Imaging.Encoder.Quality, System.Drawing.Imaging.Encoder.ColorDepth, or System.Drawing.Imaging.Encoder.Compression) of the parameter stored in this System.Drawing.Imaging.EncoderParameter object.



Get: Encoder(self: EncoderParameter) -> Encoder



Set: Encoder(self: EncoderParameter) = value

"""

    NumberOfValues = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the number of elements in the array of values stored in this System.Drawing.Imaging.EncoderParameter object.



Get: NumberOfValues(self: EncoderParameter) -> int



"""

    Type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the data type of the values stored in this System.Drawing.Imaging.EncoderParameter object.



Get: Type(self: EncoderParameter) -> EncoderParameterValueType



"""

    ValueType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the data type of the values stored in this System.Drawing.Imaging.EncoderParameter object.



Get: ValueType(self: EncoderParameter) -> EncoderParameterValueType



"""



class EncoderParameters(object, IDisposable):
    """
    Encapsulates an array of System.Drawing.Imaging.EncoderParameter objects.

    

    EncoderParameters(count: int)

    EncoderParameters()
    """
    def Dispose(self):
        """
        Dispose(self: EncoderParameters)

            Releases all resources used by this System.Drawing.Imaging.EncoderParameters object.
        """
        pass

    def __enter__(self, *args): #cannot find CLR method
        """
        __enter__(self: IDisposable) -> object

        

            Provides the implementation of __enter__ for objects which implement IDisposable.
        """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """
        __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object)

            Provides the implementation of __exit__ for objects which implement IDisposable.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, count=None):
        """
        __new__(cls: type, count: int)

        __new__(cls: type)
        """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    Param = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets an array of System.Drawing.Imaging.EncoderParameter objects.



Get: Param(self: EncoderParameters) -> Array[EncoderParameter]



Set: Param(self: EncoderParameters) = value

"""



class EncoderParameterValueType:
    """.NET enum: System.Drawing.Imaging.EncoderParameterValueType"""
    def __init__(self, *args) -> None: ...
    ValueTypeByte: int  # = 1
    ValueTypeAscii: int  # = 2
    ValueTypeShort: int  # = 3
    ValueTypeLong: int  # = 4
    ValueTypeRational: int  # = 5
    ValueTypeLongRange: int  # = 6
    ValueTypeUndefined: int  # = 7
    ValueTypeRationalRange: int  # = 8
    ValueTypePointer: int  # = 9
class EncoderValue:
    """.NET enum: System.Drawing.Imaging.EncoderValue"""
    def __init__(self, *args) -> None: ...
    ColorTypeCMYK: int  # = 0
    ColorTypeYCCK: int  # = 1
    CompressionLZW: int  # = 2
    CompressionCCITT3: int  # = 3
    CompressionCCITT4: int  # = 4
    CompressionRle: int  # = 5
    CompressionNone: int  # = 6
    ScanMethodInterlaced: int  # = 7
    ScanMethodNonInterlaced: int  # = 8
    VersionGif87: int  # = 9
    VersionGif89: int  # = 10
    RenderProgressive: int  # = 11
    RenderNonProgressive: int  # = 12
    TransformRotate90: int  # = 13
    TransformRotate180: int  # = 14
    TransformRotate270: int  # = 15
    TransformFlipHorizontal: int  # = 16
    TransformFlipVertical: int  # = 17
    MultiFrame: int  # = 18
    LastFrame: int  # = 19
    Flush: int  # = 20
    FrameDimensionTime: int  # = 21
    FrameDimensionResolution: int  # = 22
    FrameDimensionPage: int  # = 23
class FrameDimension(object):
    """
    Provides properties that get the frame dimensions of an image. Not inheritable.

    

    FrameDimension(guid: Guid)
    """
    def Equals(self, o):
        """
        Equals(self: FrameDimension, o: object) -> bool

        

            Returns a value that indicates whether the specified object is a 

             System.Drawing.Imaging.FrameDimension equivalent to this System.Drawing.Imaging.FrameDimension 

             object.

        

        

            o: The object to test.

            Returns: Returns true if o is a System.Drawing.Imaging.FrameDimension equivalent to this 

             System.Drawing.Imaging.FrameDimension object; otherwise, false.
        """
        pass

    def GetHashCode(self):
        """
        GetHashCode(self: FrameDimension) -> int

        

            Returns a hash code for this System.Drawing.Imaging.FrameDimension object.

            Returns: Returns an int value that is the hash code of this System.Drawing.Imaging.FrameDimension object.
        """
        pass

    def ToString(self):
        """
        ToString(self: FrameDimension) -> str

        

            Converts this System.Drawing.Imaging.FrameDimension object to a human-readable string.

            Returns: A string that represents this System.Drawing.Imaging.FrameDimension object.
        """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        pass

    @staticmethod # known case of __new__
    def __new__(self, guid):
        """ __new__(cls: type, guid: Guid) """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    Guid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a globally unique identifier (GUID) that represents this System.Drawing.Imaging.FrameDimension object.



Get: Guid(self: FrameDimension) -> Guid



"""


    Page = None
    Resolution = None
    Time = None


class ImageAttributes(object, ICloneable, IDisposable):
    """
    Contains information about how bitmap and metafile colors are manipulated during rendering.

    

    ImageAttributes()
    """
    def ClearBrushRemapTable(self):
        """
        ClearBrushRemapTable(self: ImageAttributes)

            Clears the brush color-remap table of this System.Drawing.Imaging.ImageAttributes object.
        """
        pass

    def ClearColorKey(self, type=None):
        """
        ClearColorKey(self: ImageAttributes)

            Clears the color key (transparency range) for the default category.

        ClearColorKey(self: ImageAttributes, type: ColorAdjustType)

            Clears the color key (transparency range) for a specified category.

        

            type: An element of System.Drawing.Imaging.ColorAdjustType that specifies the category for which the 

             color key is cleared.
        """
        pass

    def ClearColorMatrix(self, type=None):
        """
        ClearColorMatrix(self: ImageAttributes, type: ColorAdjustType)

            Clears the color-adjustment matrix for a specified category.

        

            type: An element of System.Drawing.Imaging.ColorAdjustType that specifies the category for which the 

             color-adjustment matrix is cleared.

        

        ClearColorMatrix(self: ImageAttributes)

            Clears the color-adjustment matrix for the default category.
        """
        pass

    def ClearGamma(self, type=None):
        """
        ClearGamma(self: ImageAttributes, type: ColorAdjustType)

            Disables gamma correction for a specified category.

        

            type: An element of System.Drawing.Imaging.ColorAdjustType that specifies the category for which gamma 

             correction is disabled.

        

        ClearGamma(self: ImageAttributes)

            Disables gamma correction for the default category.
        """
        pass

    def ClearNoOp(self, type=None):
        """
        ClearNoOp(self: ImageAttributes, type: ColorAdjustType)

            Clears the NoOp setting for a specified category.

        

            type: An element of System.Drawing.Imaging.ColorAdjustType that specifies the category for which the 

             NoOp setting is cleared.

        

        ClearNoOp(self: ImageAttributes)

            Clears the NoOp setting for the default category.
        """
        pass

    def ClearOutputChannel(self, type=None):
        """
        ClearOutputChannel(self: ImageAttributes, type: ColorAdjustType)

            Clears the (cyan-magenta-yellow-black) output channel setting for a specified category.

        

            type: An element of System.Drawing.Imaging.ColorAdjustType that specifies the category for which the 

             output channel setting is cleared.

        

        ClearOutputChannel(self: ImageAttributes)

            Clears the CMYK (cyan-magenta-yellow-black) output channel setting for the default category.
        """
        pass

    def ClearOutputChannelColorProfile(self, type=None):
        """
        ClearOutputChannelColorProfile(self: ImageAttributes, type: ColorAdjustType)

            Clears the output channel color profile setting for a specified category.

        

            type: An element of System.Drawing.Imaging.ColorAdjustType that specifies the category for which the 

             output channel profile setting is cleared.

        

        ClearOutputChannelColorProfile(self: ImageAttributes)

            Clears the output channel color profile setting for the default category.
        """
        pass

    def ClearRemapTable(self, type=None):
        """
        ClearRemapTable(self: ImageAttributes, type: ColorAdjustType)

            Clears the color-remap table for a specified category.

        

            type: An element of System.Drawing.Imaging.ColorAdjustType that specifies the category for which the 

             remap table is cleared.

        

        ClearRemapTable(self: ImageAttributes)

            Clears the color-remap table for the default category.
        """
        pass

    def ClearThreshold(self, type=None):
        """
        ClearThreshold(self: ImageAttributes, type: ColorAdjustType)

            Clears the threshold value for a specified category.

        

            type: An element of System.Drawing.Imaging.ColorAdjustType that specifies the category for which the 

             threshold is cleared.

        

        ClearThreshold(self: ImageAttributes)

            Clears the threshold value for the default category.
        """
        pass

    def Clone(self):
        """
        Clone(self: ImageAttributes) -> object

        

            Creates an exact copy of this System.Drawing.Imaging.ImageAttributes object.

            Returns: The System.Drawing.Imaging.ImageAttributes object this class creates, cast as an object.
        """
        pass

    def Dispose(self):
        """
        Dispose(self: ImageAttributes)

            Releases all resources used by this System.Drawing.Imaging.ImageAttributes object.
        """
        pass

    def GetAdjustedPalette(self, palette, type):
        """
        GetAdjustedPalette(self: ImageAttributes, palette: ColorPalette, type: ColorAdjustType)

            Adjusts the colors in a palette according to the adjustment settings of a specified category.

        

            palette: A System.Drawing.Imaging.ColorPalette that on input contains the palette to be adjusted, and on 

             output contains the adjusted palette.

        

            type: An element of System.Drawing.Imaging.ColorAdjustType that specifies the category whose 

             adjustment settings will be applied to the palette.
        """
        pass

    def SetBrushRemapTable(self, map):
        """
        SetBrushRemapTable(self: ImageAttributes, map: Array[ColorMap])

            Sets the color-remap table for the brush category.

        

            map: An array of System.Drawing.Imaging.ColorMap objects.
        """
        pass

    def SetColorKey(self, colorLow, colorHigh, type=None):
        """
        SetColorKey(self: ImageAttributes, colorLow: Color, colorHigh: Color, type: ColorAdjustType)

            Sets the color key (transparency range) for a specified category.

        

            colorLow: The low color-key value.

            colorHigh: The high color-key value.

            type: An element of System.Drawing.Imaging.ColorAdjustType that specifies the category for which the 

             color key is set.

        

        SetColorKey(self: ImageAttributes, colorLow: Color, colorHigh: Color)

            Sets the color key for the default category.

        

            colorLow: The low color-key value.

            colorHigh: The high color-key value.
        """
        pass

    def SetColorMatrices(self, newColorMatrix, grayMatrix, *__args):
        """
        SetColorMatrices(self: ImageAttributes, newColorMatrix: ColorMatrix, grayMatrix: ColorMatrix, mode: ColorMatrixFlag, type: ColorAdjustType)

            Sets the color-adjustment matrix and the grayscale-adjustment matrix for a specified category.

        

            newColorMatrix: The color-adjustment matrix.

            grayMatrix: The grayscale-adjustment matrix.

            mode: An element of System.Drawing.Imaging.ColorMatrixFlag that specifies the type of image and color 

             that will be affected by the color-adjustment and grayscale-adjustment matrices.

        

            type: An element of System.Drawing.Imaging.ColorAdjustType that specifies the category for which the 

             color-adjustment and grayscale-adjustment matrices are set.

        

        SetColorMatrices(self: ImageAttributes, newColorMatrix: ColorMatrix, grayMatrix: ColorMatrix, flags: ColorMatrixFlag)

            Sets the color-adjustment matrix and the grayscale-adjustment matrix for the default category.

        

            newColorMatrix: The color-adjustment matrix.

            grayMatrix: The grayscale-adjustment matrix.

            flags: An element of System.Drawing.Imaging.ColorMatrixFlag that specifies the type of image and color 

             that will be affected by the color-adjustment and grayscale-adjustment matrices.

        

        SetColorMatrices(self: ImageAttributes, newColorMatrix: ColorMatrix, grayMatrix: ColorMatrix)

            Sets the color-adjustment matrix and the grayscale-adjustment matrix for the default category.

        

            newColorMatrix: The color-adjustment matrix.

            grayMatrix: The grayscale-adjustment matrix.
        """
        pass

    def SetColorMatrix(self, newColorMatrix, *__args):
        """
        SetColorMatrix(self: ImageAttributes, newColorMatrix: ColorMatrix, flags: ColorMatrixFlag)

            Sets the color-adjustment matrix for the default category.

        

            newColorMatrix: The color-adjustment matrix.

            flags: An element of System.Drawing.Imaging.ColorMatrixFlag that specifies the type of image and color 

             that will be affected by the color-adjustment matrix.

        

        SetColorMatrix(self: ImageAttributes, newColorMatrix: ColorMatrix)

            Sets the color-adjustment matrix for the default category.

        

            newColorMatrix: The color-adjustment matrix.

        SetColorMatrix(self: ImageAttributes, newColorMatrix: ColorMatrix, mode: ColorMatrixFlag, type: ColorAdjustType)

            Sets the color-adjustment matrix for a specified category.

        

            newColorMatrix: The color-adjustment matrix.

            mode: An element of System.Drawing.Imaging.ColorMatrixFlag that specifies the type of image and color 

             that will be affected by the color-adjustment matrix.

        

            type: An element of System.Drawing.Imaging.ColorAdjustType that specifies the category for which the 

             color-adjustment matrix is set.
        """
        pass

    def SetGamma(self, gamma, type=None):
        """
        SetGamma(self: ImageAttributes, gamma: Single, type: ColorAdjustType)

            Sets the gamma value for a specified category.

        

            gamma: The gamma correction value.

            type: An element of the System.Drawing.Imaging.ColorAdjustType enumeration that specifies the category 

             for which the gamma value is set.

        

        SetGamma(self: ImageAttributes, gamma: Single)

            Sets the gamma value for the default category.

        

            gamma: The gamma correction value.
        """
        pass

    def SetNoOp(self, type=None):
        """
        SetNoOp(self: ImageAttributes, type: ColorAdjustType)

            Turns off color adjustment for a specified category. You can call the 

             erload:System.Drawing.Imaging.ImageAttributes.ClearNoOp method to reinstate the color-adjustment 

             settings that were in place before the call to the 

             erload:System.Drawing.Imaging.ImageAttributes.SetNoOp method.

        

        

            type: An element of System.Drawing.Imaging.ColorAdjustType that specifies the category for which color 

             correction is turned off.

        

        SetNoOp(self: ImageAttributes)

            Turns off color adjustment for the default category. You can call the 

             erload:System.Drawing.Imaging.ImageAttributes.ClearNoOp method to reinstate the color-adjustment 

             settings that were in place before the call to the 

             erload:System.Drawing.Imaging.ImageAttributes.SetNoOp method.
        """
        pass

    def SetOutputChannel(self, flags, type=None):
        """
        SetOutputChannel(self: ImageAttributes, flags: ColorChannelFlag, type: ColorAdjustType)

            Sets the CMYK (cyan-magenta-yellow-black) output channel for a specified category.

        

            flags: An element of System.Drawing.Imaging.ColorChannelFlag that specifies the output channel.

            type: An element of System.Drawing.Imaging.ColorAdjustType that specifies the category for which the 

             output channel is set.

        

        SetOutputChannel(self: ImageAttributes, flags: ColorChannelFlag)

            Sets the CMYK (cyan-magenta-yellow-black) output channel for the default category.

        

            flags: An element of System.Drawing.Imaging.ColorChannelFlag that specifies the output channel.
        """
        pass

    def SetOutputChannelColorProfile(self, colorProfileFilename, type=None):
        """
        SetOutputChannelColorProfile(self: ImageAttributes, colorProfileFilename: str, type: ColorAdjustType)

            Sets the output channel color-profile file for a specified category.

        

            colorProfileFilename: The path name of a color-profile file. If the color-profile file is in the 

             %SystemRoot%\System32\Spool\Drivers\Color directory, this parameter can be the file name. 

             Otherwise, this parameter must be the fully qualified path name.

        

            type: An element of System.Drawing.Imaging.ColorAdjustType that specifies the category for which the 

             output channel color-profile file is set.

        

        SetOutputChannelColorProfile(self: ImageAttributes, colorProfileFilename: str)

            Sets the output channel color-profile file for the default category.

        

            colorProfileFilename: The path name of a color-profile file. If the color-profile file is in the 

             %SystemRoot%\System32\Spool\Drivers\Color directory, this parameter can be the file name. 

             Otherwise, this parameter must be the fully qualified path name.
        """
        pass

    def SetRemapTable(self, map, type=None):
        """
        SetRemapTable(self: ImageAttributes, map: Array[ColorMap], type: ColorAdjustType)

            Sets the color-remap table for a specified category.

        

            map: An array of color pairs of type System.Drawing.Imaging.ColorMap. Each color pair contains an 

             existing color (the first value) and the color that it will be mapped to (the second value).

        

            type: An element of System.Drawing.Imaging.ColorAdjustType that specifies the category for which the 

             color-remap table is set.

        

        SetRemapTable(self: ImageAttributes, map: Array[ColorMap])

            Sets the color-remap table for the default category.

        

            map: An array of color pairs of type System.Drawing.Imaging.ColorMap. Each color pair contains an 

             existing color (the first value) and the color that it will be mapped to (the second value).
        """
        pass

    def SetThreshold(self, threshold, type=None):
        """
        SetThreshold(self: ImageAttributes, threshold: Single, type: ColorAdjustType)

            Sets the threshold (transparency range) for a specified category.

        

            threshold: A threshold value from 0.0 to 1.0 that is used as a breakpoint to sort colors that will be 

             mapped to either a maximum or a minimum value.

        

            type: An element of System.Drawing.Imaging.ColorAdjustType that specifies the category for which the 

             color threshold is set.

        

        SetThreshold(self: ImageAttributes, threshold: Single)

            Sets the threshold (transparency range) for the default category.

        

            threshold: A real number that specifies the threshold value.
        """
        pass

    def SetWrapMode(self, mode, color=None, clamp=None):
        """
        SetWrapMode(self: ImageAttributes, mode: WrapMode, color: Color, clamp: bool)

            Sets the wrap mode and color used to decide how to tile a texture across a shape, or at shape 

             boundaries. A texture is tiled across a shape to fill it in when the texture is smaller than the 

             shape it is filling.

        

        

            mode: An element of System.Drawing.Drawing2D.WrapMode that specifies how repeated copies of an image 

             are used to tile an area.

        

            color: A color object that specifies the color of pixels outside of a rendered image. This color is 

             visible if the mode parameter is set to System.Drawing.Drawing2D.WrapMode.Clamp and the source 

             rectangle passed to erload:System.Drawing.Graphics.DrawImage is larger than the image itself.

        

            clamp: This parameter has no effect. Set it to false.

        SetWrapMode(self: ImageAttributes, mode: WrapMode, color: Color)

            Sets the wrap mode and color used to decide how to tile a texture across a shape, or at shape 

             boundaries. A texture is tiled across a shape to fill it in when the texture is smaller than the 

             shape it is filling.

        

        

            mode: An element of System.Drawing.Drawing2D.WrapMode that specifies how repeated copies of an image 

             are used to tile an area.

        

            color: An System.Drawing.Imaging.ImageAttributes object that specifies the color of pixels outside of a 

             rendered image. This color is visible if the mode parameter is set to 

             System.Drawing.Drawing2D.WrapMode.Clamp and the source rectangle passed to 

             erload:System.Drawing.Graphics.DrawImage is larger than the image itself.

        

        SetWrapMode(self: ImageAttributes, mode: WrapMode)

            Sets the wrap mode that is used to decide how to tile a texture across a shape, or at shape 

             boundaries. A texture is tiled across a shape to fill it in when the texture is smaller than the 

             shape it is filling.

        

        

            mode: An element of System.Drawing.Drawing2D.WrapMode that specifies how repeated copies of an image 

             are used to tile an area.
        """
        pass

    def __enter__(self, *args): #cannot find CLR method
        """
        __enter__(self: IDisposable) -> object

        

            Provides the implementation of __enter__ for objects which implement IDisposable.
        """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """
        __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object)

            Provides the implementation of __exit__ for objects which implement IDisposable.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass


class ImageCodecFlags:
    """.NET enum: System.Drawing.Imaging.ImageCodecFlags"""
    def __init__(self, *args) -> None: ...
    Encoder: int  # = 1
    Decoder: int  # = 2
    SupportBitmap: int  # = 4
    SupportVector: int  # = 8
    SeekableEncode: int  # = 16
    BlockingDecode: int  # = 32
    Builtin: int  # = 65536
    System: int  # = 131072
    User: int  # = 262144
class ImageCodecInfo(object):
    """ The System.Drawing.Imaging.ImageCodecInfo class provides the necessary storage members and methods to retrieve all pertinent information about the installed image encoders and decoders (called codecs). Not inheritable. """
    @staticmethod
    def GetImageDecoders():
        """
        GetImageDecoders() -> Array[ImageCodecInfo]

        

            Returns an array of System.Drawing.Imaging.ImageCodecInfo objects that contain information about 

             the image decoders built into GDI+.

        

            Returns: An array of System.Drawing.Imaging.ImageCodecInfo objects. Each 

             System.Drawing.Imaging.ImageCodecInfo object in the array contains information about one of the 

             built-in image decoders.
        """
        pass

    @staticmethod
    def GetImageEncoders():
        """
        GetImageEncoders() -> Array[ImageCodecInfo]

        

            Returns an array of System.Drawing.Imaging.ImageCodecInfo objects that contain information about 

             the image encoders built into GDI+.

        

            Returns: An array of System.Drawing.Imaging.ImageCodecInfo objects. Each 

             System.Drawing.Imaging.ImageCodecInfo object in the array contains information about one of the 

             built-in image encoders.
        """
        pass

    Clsid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a System.Guid structure that contains a GUID that identifies a specific codec.



Get: Clsid(self: ImageCodecInfo) -> Guid



Set: Clsid(self: ImageCodecInfo) = value

"""

    CodecName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a string that contains the name of the codec.



Get: CodecName(self: ImageCodecInfo) -> str



Set: CodecName(self: ImageCodecInfo) = value

"""

    DllName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets string that contains the path name of the DLL that holds the codec. If the codec is not in a DLL, this pointer is null.



Get: DllName(self: ImageCodecInfo) -> str



Set: DllName(self: ImageCodecInfo) = value

"""

    FilenameExtension = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets string that contains the file name extension(s) used in the codec. The extensions are separated by semicolons.



Get: FilenameExtension(self: ImageCodecInfo) -> str



Set: FilenameExtension(self: ImageCodecInfo) = value

"""

    Flags = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets 32-bit value used to store additional information about the codec. This property returns a combination of flags from the System.Drawing.Imaging.ImageCodecFlags enumeration.



Get: Flags(self: ImageCodecInfo) -> ImageCodecFlags



Set: Flags(self: ImageCodecInfo) = value

"""

    FormatDescription = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a string that describes the codec's file format.



Get: FormatDescription(self: ImageCodecInfo) -> str



Set: FormatDescription(self: ImageCodecInfo) = value

"""

    FormatID = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a System.Guid structure that contains a GUID that identifies the codec's format.



Get: FormatID(self: ImageCodecInfo) -> Guid



Set: FormatID(self: ImageCodecInfo) = value

"""

    MimeType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a string that contains the codec's Multipurpose Internet Mail Extensions (MIME) type.



Get: MimeType(self: ImageCodecInfo) -> str



Set: MimeType(self: ImageCodecInfo) = value

"""

    SignatureMasks = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a two dimensional array of bytes that can be used as a filter.



Get: SignatureMasks(self: ImageCodecInfo) -> Array[Array[Byte]]



Set: SignatureMasks(self: ImageCodecInfo) = value

"""

    SignaturePatterns = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a two dimensional array of bytes that represents the signature of the codec.



Get: SignaturePatterns(self: ImageCodecInfo) -> Array[Array[Byte]]



Set: SignaturePatterns(self: ImageCodecInfo) = value

"""

    Version = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the version number of the codec.



Get: Version(self: ImageCodecInfo) -> int



Set: Version(self: ImageCodecInfo) = value

"""



class ImageFlags:
    """.NET enum: System.Drawing.Imaging.ImageFlags"""
    def __init__(self, *args) -> None: ...
    None_: int  # = 0
    Scalable: int  # = 1
    HasAlpha: int  # = 2
    HasTranslucent: int  # = 4
    PartiallyScalable: int  # = 8
    ColorSpaceRgb: int  # = 16
    ColorSpaceCmyk: int  # = 32
    ColorSpaceGray: int  # = 64
    ColorSpaceYcbcr: int  # = 128
    ColorSpaceYcck: int  # = 256
    HasRealDpi: int  # = 4096
    HasRealPixelSize: int  # = 8192
    ReadOnly: int  # = 65536
    Caching: int  # = 131072
class ImageFormat(object):
    """
    Specifies the file format of the image. Not inheritable.

    

    ImageFormat(guid: Guid)
    """
    def Equals(self, o):
        """
        Equals(self: ImageFormat, o: object) -> bool

        

            Returns a value that indicates whether the specified object is an 

             System.Drawing.Imaging.ImageFormat object that is equivalent to this 

             System.Drawing.Imaging.ImageFormat object.

        

        

            o: The object to test.

            Returns: true if o is an System.Drawing.Imaging.ImageFormat object that is equivalent to this 

             System.Drawing.Imaging.ImageFormat object; otherwise, false.
        """
        pass

    def GetHashCode(self):
        """
        GetHashCode(self: ImageFormat) -> int

        

            Returns a hash code value that represents this object.

            Returns: A hash code that represents this object.
        """
        pass

    def ToString(self):
        """
        ToString(self: ImageFormat) -> str

        

            Converts this System.Drawing.Imaging.ImageFormat object to a human-readable string.

            Returns: A string that represents this System.Drawing.Imaging.ImageFormat object.
        """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        pass

    @staticmethod # known case of __new__
    def __new__(self, guid):
        """ __new__(cls: type, guid: Guid) """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    Guid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a System.Guid structure that represents this System.Drawing.Imaging.ImageFormat object.



Get: Guid(self: ImageFormat) -> Guid



"""


    Bmp = None
    Emf = None
    Exif = None
    Gif = None
    Icon = None
    Jpeg = None
    MemoryBmp = None
    Png = None
    Tiff = None
    Wmf = None


class ImageLockMode:
    """.NET enum: System.Drawing.Imaging.ImageLockMode"""
    def __init__(self, *args) -> None: ...
    ReadOnly: int  # = 1
    WriteOnly: int  # = 2
    ReadWrite: int  # = 3
    UserInputBuffer: int  # = 4
class Metafile(Image, ISerializable, ICloneable, IDisposable):
    """
    Defines a graphic metafile. A metafile contains records that describe a sequence of graphics operations that can be recorded (constructed) and played back (displayed). This class is not inheritable.

    

    Metafile(hmetafile: IntPtr, wmfHeader: WmfPlaceableFileHeader)

    Metafile(hmetafile: IntPtr, wmfHeader: WmfPlaceableFileHeader, deleteWmf: bool)

    Metafile(henhmetafile: IntPtr, deleteEmf: bool)

    Metafile(filename: str)

    Metafile(stream: Stream)

    Metafile(referenceHdc: IntPtr, emfType: EmfType)

    Metafile(referenceHdc: IntPtr, emfType: EmfType, description: str)

    Metafile(referenceHdc: IntPtr, frameRect: RectangleF)

    Metafile(referenceHdc: IntPtr, frameRect: RectangleF, frameUnit: MetafileFrameUnit)

    Metafile(referenceHdc: IntPtr, frameRect: RectangleF, frameUnit: MetafileFrameUnit, type: EmfType)

    Metafile(referenceHdc: IntPtr, frameRect: RectangleF, frameUnit: MetafileFrameUnit, type: EmfType, description: str)

    Metafile(referenceHdc: IntPtr, frameRect: Rectangle)

    Metafile(referenceHdc: IntPtr, frameRect: Rectangle, frameUnit: MetafileFrameUnit)

    Metafile(referenceHdc: IntPtr, frameRect: Rectangle, frameUnit: MetafileFrameUnit, type: EmfType)

    Metafile(referenceHdc: IntPtr, frameRect: Rectangle, frameUnit: MetafileFrameUnit, type: EmfType, desc: str)

    Metafile(fileName: str, referenceHdc: IntPtr)

    Metafile(fileName: str, referenceHdc: IntPtr, type: EmfType)

    Metafile(fileName: str, referenceHdc: IntPtr, type: EmfType, description: str)

    Metafile(fileName: str, referenceHdc: IntPtr, frameRect: RectangleF)

    Metafile(fileName: str, referenceHdc: IntPtr, frameRect: RectangleF, frameUnit: MetafileFrameUnit)

    Metafile(fileName: str, referenceHdc: IntPtr, frameRect: RectangleF, frameUnit: MetafileFrameUnit, type: EmfType)

    Metafile(fileName: str, referenceHdc: IntPtr, frameRect: RectangleF, frameUnit: MetafileFrameUnit, desc: str)

    Metafile(fileName: str, referenceHdc: IntPtr, frameRect: RectangleF, frameUnit: MetafileFrameUnit, type: EmfType, description: str)

    Metafile(fileName: str, referenceHdc: IntPtr, frameRect: Rectangle)

    Metafile(fileName: str, referenceHdc: IntPtr, frameRect: Rectangle, frameUnit: MetafileFrameUnit)

    Metafile(fileName: str, referenceHdc: IntPtr, frameRect: Rectangle, frameUnit: MetafileFrameUnit, type: EmfType)

    Metafile(fileName: str, referenceHdc: IntPtr, frameRect: Rectangle, frameUnit: MetafileFrameUnit, description: str)

    Metafile(fileName: str, referenceHdc: IntPtr, frameRect: Rectangle, frameUnit: MetafileFrameUnit, type: EmfType, description: str)

    Metafile(stream: Stream, referenceHdc: IntPtr)

    Metafile(stream: Stream, referenceHdc: IntPtr, type: EmfType)

    Metafile(stream: Stream, referenceHdc: IntPtr, type: EmfType, description: str)

    Metafile(stream: Stream, referenceHdc: IntPtr, frameRect: RectangleF)

    Metafile(stream: Stream, referenceHdc: IntPtr, frameRect: RectangleF, frameUnit: MetafileFrameUnit)

    Metafile(stream: Stream, referenceHdc: IntPtr, frameRect: RectangleF, frameUnit: MetafileFrameUnit, type: EmfType)

    Metafile(stream: Stream, referenceHdc: IntPtr, frameRect: RectangleF, frameUnit: MetafileFrameUnit, type: EmfType, description: str)

    Metafile(stream: Stream, referenceHdc: IntPtr, frameRect: Rectangle)

    Metafile(stream: Stream, referenceHdc: IntPtr, frameRect: Rectangle, frameUnit: MetafileFrameUnit)

    Metafile(stream: Stream, referenceHdc: IntPtr, frameRect: Rectangle, frameUnit: MetafileFrameUnit, type: EmfType)

    Metafile(stream: Stream, referenceHdc: IntPtr, frameRect: Rectangle, frameUnit: MetafileFrameUnit, type: EmfType, description: str)
    """
    def Dispose(self):
        """
        Dispose(self: Image, disposing: bool)

            Releases the unmanaged resources used by the System.Drawing.Image and optionally releases the 

             managed resources.

        

        

            disposing: true to release both managed and unmanaged resources; false to release only unmanaged resources.
        """
        pass

    def GetHenhmetafile(self):
        """
        GetHenhmetafile(self: Metafile) -> IntPtr

        

            Returns a Windows handle to an enhanced System.Drawing.Imaging.Metafile.

            Returns: A Windows handle to this enhanced System.Drawing.Imaging.Metafile.
        """
        pass

    @staticmethod
    def GetMetafileHeader(*__args):
        """
        GetMetafileHeader(stream: Stream) -> MetafileHeader

        

            Returns the System.Drawing.Imaging.MetafileHeader associated with the specified 

             System.Drawing.Imaging.Metafile.

        

        

            stream: A System.IO.Stream containing the System.Drawing.Imaging.Metafile for which a header is 

             retrieved.

        

            Returns: The System.Drawing.Imaging.MetafileHeader associated with the specified 

             System.Drawing.Imaging.Metafile.

        

        GetMetafileHeader(self: Metafile) -> MetafileHeader

        

            Returns the System.Drawing.Imaging.MetafileHeader associated with this 

             System.Drawing.Imaging.Metafile.

        

            Returns: The System.Drawing.Imaging.MetafileHeader associated with this System.Drawing.Imaging.Metafile.

        GetMetafileHeader(fileName: str) -> MetafileHeader

        

            Returns the System.Drawing.Imaging.MetafileHeader associated with the specified 

             System.Drawing.Imaging.Metafile.

        

        

            fileName: A System.String containing the name of the System.Drawing.Imaging.Metafile for which a header is 

             retrieved.

        

            Returns: The System.Drawing.Imaging.MetafileHeader associated with the specified 

             System.Drawing.Imaging.Metafile.

        

        GetMetafileHeader(hmetafile: IntPtr, wmfHeader: WmfPlaceableFileHeader) -> MetafileHeader

        

            Returns the System.Drawing.Imaging.MetafileHeader associated with the specified 

             System.Drawing.Imaging.Metafile.

        

        

            hmetafile: The handle to the System.Drawing.Imaging.Metafile for which to return a header.

            wmfHeader: A System.Drawing.Imaging.WmfPlaceableFileHeader.

            Returns: The System.Drawing.Imaging.MetafileHeader associated with the specified 

             System.Drawing.Imaging.Metafile.

        

        GetMetafileHeader(henhmetafile: IntPtr) -> MetafileHeader

        

            Returns the System.Drawing.Imaging.MetafileHeader associated with the specified 

             System.Drawing.Imaging.Metafile.

        

        

            henhmetafile: The handle to the enhanced System.Drawing.Imaging.Metafile for which a header is returned.

            Returns: The System.Drawing.Imaging.MetafileHeader associated with the specified 

             System.Drawing.Imaging.Metafile.
        """
        pass

    def MemberwiseClone(self, *args): #cannot find CLR method
        """
        MemberwiseClone(self: MarshalByRefObject, cloneIdentity: bool) -> MarshalByRefObject

        

            Creates a shallow copy of the current System.MarshalByRefObject object.

        

            cloneIdentity: false to delete the current System.MarshalByRefObject object's identity, which will cause the 

             object to be assigned a new identity when it is marshaled across a remoting boundary. A value of 

             false is usually appropriate. true to copy the current System.MarshalByRefObject object's 

             identity to its clone, which will cause remoting client calls to be routed to the remote server 

             object.

        

            Returns: A shallow copy of the current System.MarshalByRefObject object.

        MemberwiseClone(self: object) -> object

        

            Creates a shallow copy of the current System.Object.

            Returns: A shallow copy of the current System.Object.
        """
        pass

    def PlayRecord(self, recordType, flags, dataSize, data):
        """
        PlayRecord(self: Metafile, recordType: EmfPlusRecordType, flags: int, dataSize: int, data: Array[Byte])

            Plays an individual metafile record.

        

            recordType: Element of the System.Drawing.Imaging.EmfPlusRecordType that specifies the type of metafile 

             record being played.

        

            flags: A set of flags that specify attributes of the record.

            dataSize: The number of bytes in the record data.

            data: An array of bytes that contains the record data.
        """
        pass

    def __enter__(self, *args): #cannot find CLR method
        """
        __enter__(self: IDisposable) -> object

        

            Provides the implementation of __enter__ for objects which implement IDisposable.
        """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """
        __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object)

            Provides the implementation of __exit__ for objects which implement IDisposable.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type, hmetafile: IntPtr, wmfHeader: WmfPlaceableFileHeader)

        __new__(cls: type, hmetafile: IntPtr, wmfHeader: WmfPlaceableFileHeader, deleteWmf: bool)

        __new__(cls: type, henhmetafile: IntPtr, deleteEmf: bool)

        __new__(cls: type, filename: str)

        __new__(cls: type, stream: Stream)

        __new__(cls: type, referenceHdc: IntPtr, emfType: EmfType)

        __new__(cls: type, referenceHdc: IntPtr, emfType: EmfType, description: str)

        __new__(cls: type, referenceHdc: IntPtr, frameRect: RectangleF)

        __new__(cls: type, referenceHdc: IntPtr, frameRect: RectangleF, frameUnit: MetafileFrameUnit)

        __new__(cls: type, referenceHdc: IntPtr, frameRect: RectangleF, frameUnit: MetafileFrameUnit, type: EmfType)

        __new__(cls: type, referenceHdc: IntPtr, frameRect: RectangleF, frameUnit: MetafileFrameUnit, type: EmfType, description: str)

        __new__(cls: type, referenceHdc: IntPtr, frameRect: Rectangle)

        __new__(cls: type, referenceHdc: IntPtr, frameRect: Rectangle, frameUnit: MetafileFrameUnit)

        __new__(cls: type, referenceHdc: IntPtr, frameRect: Rectangle, frameUnit: MetafileFrameUnit, type: EmfType)

        __new__(cls: type, referenceHdc: IntPtr, frameRect: Rectangle, frameUnit: MetafileFrameUnit, type: EmfType, desc: str)

        __new__(cls: type, fileName: str, referenceHdc: IntPtr)

        __new__(cls: type, fileName: str, referenceHdc: IntPtr, type: EmfType)

        __new__(cls: type, fileName: str, referenceHdc: IntPtr, type: EmfType, description: str)

        __new__(cls: type, fileName: str, referenceHdc: IntPtr, frameRect: RectangleF)

        __new__(cls: type, fileName: str, referenceHdc: IntPtr, frameRect: RectangleF, frameUnit: MetafileFrameUnit)

        __new__(cls: type, fileName: str, referenceHdc: IntPtr, frameRect: RectangleF, frameUnit: MetafileFrameUnit, type: EmfType)

        __new__(cls: type, fileName: str, referenceHdc: IntPtr, frameRect: RectangleF, frameUnit: MetafileFrameUnit, desc: str)

        __new__(cls: type, fileName: str, referenceHdc: IntPtr, frameRect: RectangleF, frameUnit: MetafileFrameUnit, type: EmfType, description: str)

        __new__(cls: type, fileName: str, referenceHdc: IntPtr, frameRect: Rectangle)

        __new__(cls: type, fileName: str, referenceHdc: IntPtr, frameRect: Rectangle, frameUnit: MetafileFrameUnit)

        __new__(cls: type, fileName: str, referenceHdc: IntPtr, frameRect: Rectangle, frameUnit: MetafileFrameUnit, type: EmfType)

        __new__(cls: type, fileName: str, referenceHdc: IntPtr, frameRect: Rectangle, frameUnit: MetafileFrameUnit, description: str)

        __new__(cls: type, fileName: str, referenceHdc: IntPtr, frameRect: Rectangle, frameUnit: MetafileFrameUnit, type: EmfType, description: str)

        __new__(cls: type, stream: Stream, referenceHdc: IntPtr)

        __new__(cls: type, stream: Stream, referenceHdc: IntPtr, type: EmfType)

        __new__(cls: type, stream: Stream, referenceHdc: IntPtr, type: EmfType, description: str)

        __new__(cls: type, stream: Stream, referenceHdc: IntPtr, frameRect: RectangleF)

        __new__(cls: type, stream: Stream, referenceHdc: IntPtr, frameRect: RectangleF, frameUnit: MetafileFrameUnit)

        __new__(cls: type, stream: Stream, referenceHdc: IntPtr, frameRect: RectangleF, frameUnit: MetafileFrameUnit, type: EmfType)

        __new__(cls: type, stream: Stream, referenceHdc: IntPtr, frameRect: RectangleF, frameUnit: MetafileFrameUnit, type: EmfType, description: str)

        __new__(cls: type, stream: Stream, referenceHdc: IntPtr, frameRect: Rectangle)

        __new__(cls: type, stream: Stream, referenceHdc: IntPtr, frameRect: Rectangle, frameUnit: MetafileFrameUnit)

        __new__(cls: type, stream: Stream, referenceHdc: IntPtr, frameRect: Rectangle, frameUnit: MetafileFrameUnit, type: EmfType)

        __new__(cls: type, stream: Stream, referenceHdc: IntPtr, frameRect: Rectangle, frameUnit: MetafileFrameUnit, type: EmfType, description: str)
        """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass


class MetafileFrameUnit:
    """.NET enum: System.Drawing.Imaging.MetafileFrameUnit"""
    def __init__(self, *args) -> None: ...
    Pixel: int  # = 2
    Point: int  # = 3
    Inch: int  # = 4
    Document: int  # = 5
    Millimeter: int  # = 6
    GdiCompatible: int  # = 7
class MetafileHeader(object):
    """ Contains attributes of an associated System.Drawing.Imaging.Metafile. Not inheritable. """
    def IsDisplay(self):
        """
        IsDisplay(self: MetafileHeader) -> bool

        

            Returns a value that indicates whether the associated System.Drawing.Imaging.Metafile is device 

             dependent.

        

            Returns: true if the associated System.Drawing.Imaging.Metafile is device dependent; otherwise, false.
        """
        pass

    def IsEmf(self):
        """
        IsEmf(self: MetafileHeader) -> bool

        

            Returns a value that indicates whether the associated System.Drawing.Imaging.Metafile is in the 

             Windows enhanced metafile format.

        

            Returns: true if the associated System.Drawing.Imaging.Metafile is in the Windows enhanced metafile 

             format; otherwise, false.
        """
        pass

    def IsEmfOrEmfPlus(self):
        """
        IsEmfOrEmfPlus(self: MetafileHeader) -> bool

        

            Returns a value that indicates whether the associated System.Drawing.Imaging.Metafile is in the 

             Windows enhanced metafile format or the Windows enhanced metafile plus format.

        

            Returns: true if the associated System.Drawing.Imaging.Metafile is in the Windows enhanced metafile 

             format or the Windows enhanced metafile plus format; otherwise, false.
        """
        pass

    def IsEmfPlus(self):
        """
        IsEmfPlus(self: MetafileHeader) -> bool

        

            Returns a value that indicates whether the associated System.Drawing.Imaging.Metafile is in the 

             Windows enhanced metafile plus format.

        

            Returns: true if the associated System.Drawing.Imaging.Metafile is in the Windows enhanced metafile plus 

             format; otherwise, false.
        """
        pass

    def IsEmfPlusDual(self):
        """
        IsEmfPlusDual(self: MetafileHeader) -> bool

        

            Returns a value that indicates whether the associated System.Drawing.Imaging.Metafile is in the 

             Dual enhanced metafile format. This format supports both the enhanced and the enhanced plus 

             format.

        

            Returns: true if the associated System.Drawing.Imaging.Metafile is in the Dual enhanced metafile format; 

             otherwise, false.
        """
        pass

    def IsEmfPlusOnly(self):
        """
        IsEmfPlusOnly(self: MetafileHeader) -> bool

        

            Returns a value that indicates whether the associated System.Drawing.Imaging.Metafile supports 

             only the Windows enhanced metafile plus format.

        

            Returns: true if the associated System.Drawing.Imaging.Metafile supports only the Windows enhanced 

             metafile plus format; otherwise, false.
        """
        pass

    def IsWmf(self):
        """
        IsWmf(self: MetafileHeader) -> bool

        

            Returns a value that indicates whether the associated System.Drawing.Imaging.Metafile is in the 

             Windows metafile format.

        

            Returns: true if the associated System.Drawing.Imaging.Metafile is in the Windows metafile format; 

             otherwise, false.
        """
        pass

    def IsWmfPlaceable(self):
        """
        IsWmfPlaceable(self: MetafileHeader) -> bool

        

            Returns a value that indicates whether the associated System.Drawing.Imaging.Metafile is in the 

             Windows placeable metafile format.

        

            Returns: true if the associated System.Drawing.Imaging.Metafile is in the Windows placeable metafile 

             format; otherwise, false.
        """
        pass

    Bounds = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a System.Drawing.Rectangle that bounds the associated System.Drawing.Imaging.Metafile.



Get: Bounds(self: MetafileHeader) -> Rectangle



"""

    DpiX = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the horizontal resolution, in dots per inch, of the associated System.Drawing.Imaging.Metafile.



Get: DpiX(self: MetafileHeader) -> Single



"""

    DpiY = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the vertical resolution, in dots per inch, of the associated System.Drawing.Imaging.Metafile.



Get: DpiY(self: MetafileHeader) -> Single



"""

    EmfPlusHeaderSize = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the size, in bytes, of the enhanced metafile plus header file.



Get: EmfPlusHeaderSize(self: MetafileHeader) -> int



"""

    LogicalDpiX = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the logical horizontal resolution, in dots per inch, of the associated System.Drawing.Imaging.Metafile.



Get: LogicalDpiX(self: MetafileHeader) -> int



"""

    LogicalDpiY = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the logical vertical resolution, in dots per inch, of the associated System.Drawing.Imaging.Metafile.



Get: LogicalDpiY(self: MetafileHeader) -> int



"""

    MetafileSize = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the size, in bytes, of the associated System.Drawing.Imaging.Metafile.



Get: MetafileSize(self: MetafileHeader) -> int



"""

    Type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the type of the associated System.Drawing.Imaging.Metafile.



Get: Type(self: MetafileHeader) -> MetafileType



"""

    Version = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the version number of the associated System.Drawing.Imaging.Metafile.



Get: Version(self: MetafileHeader) -> int



"""

    WmfHeader = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the Windows metafile (WMF) header file for the associated System.Drawing.Imaging.Metafile.



Get: WmfHeader(self: MetafileHeader) -> MetaHeader



"""



class MetafileType:
    """.NET enum: System.Drawing.Imaging.MetafileType"""
    def __init__(self, *args) -> None: ...
    Invalid: int  # = 0
    Wmf: int  # = 1
    WmfPlaceable: int  # = 2
    Emf: int  # = 3
    EmfPlusOnly: int  # = 4
    EmfPlusDual: int  # = 5
class MetaHeader(object):
    """
    Contains information about a windows-format (WMF) metafile.

    

    MetaHeader()
    """
    HeaderSize = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the size, in bytes, of the header file.



Get: HeaderSize(self: MetaHeader) -> Int16



Set: HeaderSize(self: MetaHeader) = value

"""

    MaxRecord = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the size, in bytes, of the largest record in the associated System.Drawing.Imaging.Metafile object.



Get: MaxRecord(self: MetaHeader) -> int



Set: MaxRecord(self: MetaHeader) = value

"""

    NoObjects = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the maximum number of objects that exist in the System.Drawing.Imaging.Metafile object at the same time.



Get: NoObjects(self: MetaHeader) -> Int16



Set: NoObjects(self: MetaHeader) = value

"""

    NoParameters = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Not used. Always returns 0.



Get: NoParameters(self: MetaHeader) -> Int16



Set: NoParameters(self: MetaHeader) = value

"""

    Size = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the size, in bytes, of the associated System.Drawing.Imaging.Metafile object.



Get: Size(self: MetaHeader) -> int



Set: Size(self: MetaHeader) = value

"""

    Type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the type of the associated System.Drawing.Imaging.Metafile object.



Get: Type(self: MetaHeader) -> Int16



Set: Type(self: MetaHeader) = value

"""

    Version = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the version number of the header format.



Get: Version(self: MetaHeader) -> Int16



Set: Version(self: MetaHeader) = value

"""



class PaletteFlags:
    """.NET enum: System.Drawing.Imaging.PaletteFlags"""
    def __init__(self, *args) -> None: ...
    HasAlpha: int  # = 1
    GrayScale: int  # = 2
    Halftone: int  # = 4
class PixelFormat:
    """.NET enum: System.Drawing.Imaging.PixelFormat"""
    def __init__(self, *args) -> None: ...
    DontCare: int  # = 0
    Undefined: int  # = 0
    Max: int  # = 15
    Indexed: int  # = 65536
    Gdi: int  # = 131072
    Format16bppRgb555: int  # = 135173
    Format16bppRgb565: int  # = 135174
    Format24bppRgb: int  # = 137224
    Format32bppRgb: int  # = 139273
    Format1bppIndexed: int  # = 196865
    Format4bppIndexed: int  # = 197634
    Format8bppIndexed: int  # = 198659
    Alpha: int  # = 262144
    Format16bppArgb1555: int  # = 397319
    PAlpha: int  # = 524288
    Format32bppPArgb: int  # = 925707
    Extended: int  # = 1048576
    Format16bppGrayScale: int  # = 1052676
    Format48bppRgb: int  # = 1060876
    Format64bppPArgb: int  # = 1851406
    Canonical: int  # = 2097152
    Format32bppArgb: int  # = 2498570
    Format64bppArgb: int  # = 3424269
class PlayRecordCallback(MulticastDelegate, ICloneable, ISerializable):
    """
    This delegate is not used. For an example of enumerating the records of a metafile, see System.Drawing.Graphics.EnumerateMetafile(System.Drawing.Imaging.Metafile,System.Drawing.Point,System.Drawing.Graphics.EnumerateMetafileProc).

    

    PlayRecordCallback(object: object, method: IntPtr)
    """
    def BeginInvoke(self, recordType, flags, dataSize, recordData, callback, object):
        """ BeginInvoke(self: PlayRecordCallback, recordType: EmfPlusRecordType, flags: int, dataSize: int, recordData: IntPtr, callback: AsyncCallback, object: object) -> IAsyncResult """
        pass

    def CombineImpl(self, *args): #cannot find CLR method
        """
        CombineImpl(self: MulticastDelegate, follow: Delegate) -> Delegate

        

            Combines this System.Delegate with the specified System.Delegate to form a new delegate.

        

            follow: The delegate to combine with this delegate.

            Returns: A delegate that is the new root of the System.MulticastDelegate invocation list.
        """
        pass

    def DynamicInvokeImpl(self, *args): #cannot find CLR method
        """
        DynamicInvokeImpl(self: Delegate, args: Array[object]) -> object

        

            Dynamically invokes (late-bound) the method represented by the current delegate.

        

            args: An array of objects that are the arguments to pass to the method represented by the current 

             delegate.-or- null, if the method represented by the current delegate does not require 

             arguments.

        

            Returns: The object returned by the method represented by the delegate.
        """
        pass

    def EndInvoke(self, result):
        """ EndInvoke(self: PlayRecordCallback, result: IAsyncResult) """
        pass

    def GetMethodImpl(self, *args): #cannot find CLR method
        """
        GetMethodImpl(self: MulticastDelegate) -> MethodInfo

        

            Returns a static method represented by the current System.MulticastDelegate.

            Returns: A static method represented by the current System.MulticastDelegate.
        """
        pass

    def Invoke(self, recordType, flags, dataSize, recordData):
        """ Invoke(self: PlayRecordCallback, recordType: EmfPlusRecordType, flags: int, dataSize: int, recordData: IntPtr) """
        pass

    def RemoveImpl(self, *args): #cannot find CLR method
        """
        RemoveImpl(self: MulticastDelegate, value: Delegate) -> Delegate

        

            Removes an element from the invocation list of this System.MulticastDelegate that is equal to 

             the specified delegate.

        

        

            value: The delegate to search for in the invocation list.

            Returns: If value is found in the invocation list for this instance, then a new System.Delegate without 

             value in its invocation list; otherwise, this instance with its original invocation list.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, object, method):
        """ __new__(cls: type, object: object, method: IntPtr) """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass


class PropertyItem(object):
    """ Encapsulates a metadata property to be included in an image file. Not inheritable. """
    Id = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the ID of the property.



Get: Id(self: PropertyItem) -> int



Set: Id(self: PropertyItem) = value

"""

    Len = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the length (in bytes) of the System.Drawing.Imaging.PropertyItem.Value property.



Get: Len(self: PropertyItem) -> int



Set: Len(self: PropertyItem) = value

"""

    Type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets an integer that defines the type of data contained in the System.Drawing.Imaging.PropertyItem.Value property.



Get: Type(self: PropertyItem) -> Int16



Set: Type(self: PropertyItem) = value

"""

    Value = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the value of the property item.



Get: Value(self: PropertyItem) -> Array[Byte]



Set: Value(self: PropertyItem) = value

"""



class WmfPlaceableFileHeader(object):
    """
    Defines a placeable metafile. Not inheritable.

    

    WmfPlaceableFileHeader()
    """
    BboxBottom = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the y-coordinate of the lower-right corner of the bounding rectangle of the metafile image on the output device.



Get: BboxBottom(self: WmfPlaceableFileHeader) -> Int16



Set: BboxBottom(self: WmfPlaceableFileHeader) = value

"""

    BboxLeft = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the x-coordinate of the upper-left corner of the bounding rectangle of the metafile image on the output device.



Get: BboxLeft(self: WmfPlaceableFileHeader) -> Int16



Set: BboxLeft(self: WmfPlaceableFileHeader) = value

"""

    BboxRight = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the x-coordinate of the lower-right corner of the bounding rectangle of the metafile image on the output device.



Get: BboxRight(self: WmfPlaceableFileHeader) -> Int16



Set: BboxRight(self: WmfPlaceableFileHeader) = value

"""

    BboxTop = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the y-coordinate of the upper-left corner of the bounding rectangle of the metafile image on the output device.



Get: BboxTop(self: WmfPlaceableFileHeader) -> Int16



Set: BboxTop(self: WmfPlaceableFileHeader) = value

"""

    Checksum = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the checksum value for the previous ten WORD s in the header.



Get: Checksum(self: WmfPlaceableFileHeader) -> Int16



Set: Checksum(self: WmfPlaceableFileHeader) = value

"""

    Hmf = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the handle of the metafile in memory.



Get: Hmf(self: WmfPlaceableFileHeader) -> Int16



Set: Hmf(self: WmfPlaceableFileHeader) = value

"""

    Inch = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the number of twips per inch.



Get: Inch(self: WmfPlaceableFileHeader) -> Int16



Set: Inch(self: WmfPlaceableFileHeader) = value

"""

    Key = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a value indicating the presence of a placeable metafile header.



Get: Key(self: WmfPlaceableFileHeader) -> int



Set: Key(self: WmfPlaceableFileHeader) = value

"""

    Reserved = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Reserved. Do not use.



Get: Reserved(self: WmfPlaceableFileHeader) -> int



Set: Reserved(self: WmfPlaceableFileHeader) = value

"""



