# Auto-generated — Rhino 8 — Eto.Drawing

class Bitmap(Image):
    """.NET: Eto.Drawing.Bitmap"""
    def __init__(self, *args) -> None: ...
    Size: Size
    Width: int
    Height: int
    Platform: Platform
    Handler: object
    NativeHandle: IntPtr
    Properties: PropertyStore
    ID: str
    Style: str
    ControlObject: object
    IsDisposed: bool
    def Clone(self, rectangle: Nullable) -> Bitmap: ...
    @staticmethod
    def FromResource(resourceName: str, assembly: Assembly) -> Bitmap: ...
    def GetPixel(self, x: int, y: int) -> Color: ...
    def Lock(self, ) -> BitmapData: ...
    def Save(self, fileName: str, format: ImageFormat) -> None: ...
    def SetPixel(self, x: int, y: int, color: Color) -> None: ...
    def ToByteArray(self, imageFormat: ImageFormat) -> list: ...
    def WithSize(self, width: int, height: int) -> Icon: ...

class BitmapData:
    """.NET: Eto.Drawing.BitmapData"""
    def __init__(self, *args) -> None: ...
    Image: Image
    BitsPerPixel: int
    BytesPerPixel: int
    Data: IntPtr
    Flipped: bool
    ScanWidth: int
    ControlObject: object
    PremultipliedAlpha: bool
    def Dispose(self, ) -> None: ...
    def GetPixel(self, x: int, y: int) -> Color: ...
    def GetPixels(self, ) -> IEnumerable: ...
    def SetPixel(self, x: int, y: int, color: Color) -> None: ...
    def SetPixels(self, pixels: IEnumerable) -> None: ...
    def TranslateArgbToData(self, argb: int) -> int: ...
    def TranslateDataToArgb(self, bitmapData: int) -> int: ...

class Brush:
    """.NET: Eto.Drawing.Brush"""
    def __init__(self, *args) -> None: ...
    ControlObject: object
    Handler: object
    def Dispose(self, ) -> None: ...

class Brushes:
    """.NET: Eto.Drawing.Brushes"""
    def __init__(self, *args) -> None: ...
    Transparent: SolidBrush
    IndianRed: SolidBrush
    LightCoral: SolidBrush
    Salmon: SolidBrush
    DarkSalmon: SolidBrush
    LightSalmon: SolidBrush
    Red: SolidBrush
    Crimson: SolidBrush
    Firebrick: SolidBrush
    DarkRed: SolidBrush
    Pink: SolidBrush
    LightPink: SolidBrush
    HotPink: SolidBrush
    DeepPink: SolidBrush
    MediumVioletRed: SolidBrush
    PaleVioletRed: SolidBrush
    Coral: SolidBrush
    Tomato: SolidBrush
    OrangeRed: SolidBrush
    DarkOrange: SolidBrush
    Orange: SolidBrush
    Gold: SolidBrush
    Yellow: SolidBrush
    LightYellow: SolidBrush
    LemonChiffon: SolidBrush
    LightGoldenrodYellow: SolidBrush
    PapayaWhip: SolidBrush
    Moccasin: SolidBrush
    PeachPuff: SolidBrush
    PaleGoldenrod: SolidBrush
    Khaki: SolidBrush
    DarkKhaki: SolidBrush
    Lavender: SolidBrush
    Thistle: SolidBrush
    Plum: SolidBrush
    Violet: SolidBrush
    Orchid: SolidBrush
    Fuchsia: SolidBrush
    Magenta: SolidBrush
    MediumOrchid: SolidBrush
    MediumPurple: SolidBrush
    BlueViolet: SolidBrush
    DarkViolet: SolidBrush
    DarkOrchid: SolidBrush
    DarkMagenta: SolidBrush
    Purple: SolidBrush
    Indigo: SolidBrush
    DarkSlateBlue: SolidBrush
    SlateBlue: SolidBrush
    MediumSlateBlue: SolidBrush
    GreenYellow: SolidBrush
    Chartreuse: SolidBrush
    LawnGreen: SolidBrush
    Lime: SolidBrush
    LimeGreen: SolidBrush
    PaleGreen: SolidBrush
    LightGreen: SolidBrush
    MediumSpringGreen: SolidBrush
    SpringGreen: SolidBrush
    MediumSeaGreen: SolidBrush
    SeaGreen: SolidBrush
    ForestGreen: SolidBrush
    Green: SolidBrush
    DarkGreen: SolidBrush
    YellowGreen: SolidBrush
    OliveDrab: SolidBrush
    Olive: SolidBrush
    DarkOliveGreen: SolidBrush
    MediumAquamarine: SolidBrush
    DarkSeaGreen: SolidBrush
    LightSeaGreen: SolidBrush
    DarkCyan: SolidBrush
    Teal: SolidBrush
    Aqua: SolidBrush
    Cyan: SolidBrush
    LightCyan: SolidBrush
    PaleTurquoise: SolidBrush
    Aquamarine: SolidBrush
    Turquoise: SolidBrush
    MediumTurquoise: SolidBrush
    DarkTurquoise: SolidBrush
    CadetBlue: SolidBrush
    SteelBlue: SolidBrush
    LightSteelBlue: SolidBrush
    PowderBlue: SolidBrush
    LightBlue: SolidBrush
    SkyBlue: SolidBrush
    LightSkyBlue: SolidBrush
    DeepSkyBlue: SolidBrush
    DodgerBlue: SolidBrush
    CornflowerBlue: SolidBrush
    RoyalBlue: SolidBrush
    Blue: SolidBrush
    MediumBlue: SolidBrush
    DarkBlue: SolidBrush
    Navy: SolidBrush
    MidnightBlue: SolidBrush
    Cornsilk: SolidBrush
    BlanchedAlmond: SolidBrush
    Bisque: SolidBrush
    NavajoWhite: SolidBrush
    Wheat: SolidBrush
    BurlyWood: SolidBrush
    Tan: SolidBrush
    RosyBrown: SolidBrush
    SandyBrown: SolidBrush
    Goldenrod: SolidBrush
    DarkGoldenrod: SolidBrush
    Peru: SolidBrush
    Chocolate: SolidBrush
    SaddleBrown: SolidBrush
    Sienna: SolidBrush
    Brown: SolidBrush
    Maroon: SolidBrush
    White: SolidBrush
    Snow: SolidBrush
    Honeydew: SolidBrush
    MintCream: SolidBrush
    Azure: SolidBrush
    AliceBlue: SolidBrush
    GhostWhite: SolidBrush
    WhiteSmoke: SolidBrush
    Seashell: SolidBrush
    Beige: SolidBrush
    OldLace: SolidBrush
    FloralWhite: SolidBrush
    Ivory: SolidBrush
    AntiqueWhite: SolidBrush
    Linen: SolidBrush
    LavenderBlush: SolidBrush
    MistyRose: SolidBrush
    Gainsboro: SolidBrush
    LightGrey: SolidBrush
    Silver: SolidBrush
    DarkGray: SolidBrush
    Gray: SolidBrush
    DimGray: SolidBrush
    LightSlateGray: SolidBrush
    SlateGray: SolidBrush
    DarkSlateGray: SolidBrush
    Black: SolidBrush
    @staticmethod
    def Cached(color: Color) -> SolidBrush: ...
    @staticmethod
    def ClearCache() -> None: ...

class Color:
    """.NET: Eto.Drawing.Color"""
    def __init__(self, *args) -> None: ...
    A: float
    R: float
    G: float
    B: float
    Ab: int
    Rb: int
    Gb: int
    Bb: int
    ControlObject: object
    @staticmethod
    def Blend(baseColor: Color, blendColor: Color, blendFactor: float) -> Color: ...
    @staticmethod
    def Distance(value1: Color, value2: Color) -> float: ...
    def Equals(self, obj: object) -> bool: ...
    @staticmethod
    def FromArgb(red: int, green: int, blue: int, alpha: int) -> Color: ...
    @staticmethod
    def FromElementId(id: int, alpha: int) -> Color: ...
    @staticmethod
    def FromGrayscale(val: float, alpha: float) -> Color: ...
    @staticmethod
    def FromPremultipliedArgb(red: int, green: int, blue: int, alpha: int) -> Color: ...
    @staticmethod
    def FromRgb(argb: int) -> Color: ...
    def GetHashCode(self, ) -> int: ...
    def Invert(self, ) -> None: ...
    @staticmethod
    def Parse(value: str) -> Color: ...
    def ToArgb(self, style: ColorStyles) -> int: ...
    def ToCMYK(self, ) -> ColorCMYK: ...
    def ToElementId(self, ) -> int: ...
    def ToHSB(self, ) -> ColorHSB: ...
    def ToHSL(self, ) -> ColorHSL: ...
    def ToHex(self, includeAlpha: bool) -> str: ...
    def ToPremultipliedArgb(self, ) -> int: ...
    def ToString(self, ) -> str: ...
    @staticmethod
    def TryParse(value: str, color: Color, style: ColorStyles) -> bool: ...

class ColorCMYK:
    """.NET: Eto.Drawing.ColorCMYK"""
    def __init__(self, *args) -> None: ...
    C: float
    M: float
    Y: float
    K: float
    A: float
    @staticmethod
    def Distance(value1: ColorCMYK, value2: ColorCMYK) -> float: ...
    def Equals(self, obj: object) -> bool: ...
    def GetHashCode(self, ) -> int: ...
    def ToColor(self, ) -> Color: ...

class ColorConverter(TypeConverter):
    """.NET: Eto.Drawing.ColorConverter"""
    def __init__(self, *args) -> None: ...
    def CanConvertFrom(self, context: ITypeDescriptorContext, sourceType: Type) -> bool: ...
    def CanConvertTo(self, context: ITypeDescriptorContext, destinationType: Type) -> bool: ...
    def ConvertFrom(self, context: ITypeDescriptorContext, culture: CultureInfo, value: object) -> object: ...
    def ConvertTo(self, context: ITypeDescriptorContext, culture: CultureInfo, value: object, destinationType: Type) -> object: ...

class ColorHSB:
    """.NET: Eto.Drawing.ColorHSB"""
    def __init__(self, *args) -> None: ...
    A: float
    H: float
    S: float
    B: float
    @staticmethod
    def Distance(value1: ColorHSB, value2: ColorHSB) -> float: ...
    def Equals(self, obj: object) -> bool: ...
    def GetHashCode(self, ) -> int: ...
    def ToColor(self, ) -> Color: ...

class ColorHSL:
    """.NET: Eto.Drawing.ColorHSL"""
    def __init__(self, *args) -> None: ...
    A: float
    H: float
    S: float
    L: float
    @staticmethod
    def Distance(value1: ColorHSL, value2: ColorHSL) -> float: ...
    def Equals(self, obj: object) -> bool: ...
    def GetHashCode(self, ) -> int: ...
    def ToColor(self, ) -> Color: ...

class ColorStyles:
    """.NET: Eto.Drawing.ColorStyles"""
    def __init__(self, *args) -> None: ...
    ...

class Colors:
    """.NET: Eto.Drawing.Colors"""
    def __init__(self, *args) -> None: ...
    Transparent: Color
    IndianRed: Color
    LightCoral: Color
    Salmon: Color
    DarkSalmon: Color
    LightSalmon: Color
    Red: Color
    Crimson: Color
    Firebrick: Color
    DarkRed: Color
    Pink: Color
    LightPink: Color
    HotPink: Color
    DeepPink: Color
    MediumVioletRed: Color
    PaleVioletRed: Color
    Coral: Color
    Tomato: Color
    OrangeRed: Color
    DarkOrange: Color
    Orange: Color
    Gold: Color
    Yellow: Color
    LightYellow: Color
    LemonChiffon: Color
    LightGoldenrodYellow: Color
    PapayaWhip: Color
    Moccasin: Color
    PeachPuff: Color
    PaleGoldenrod: Color
    Khaki: Color
    DarkKhaki: Color
    Lavender: Color
    Thistle: Color
    Plum: Color
    Violet: Color
    Orchid: Color
    Fuchsia: Color
    Magenta: Color
    MediumOrchid: Color
    MediumPurple: Color
    BlueViolet: Color
    DarkViolet: Color
    DarkOrchid: Color
    DarkMagenta: Color
    Purple: Color
    Indigo: Color
    DarkSlateBlue: Color
    SlateBlue: Color
    MediumSlateBlue: Color
    GreenYellow: Color
    Chartreuse: Color
    LawnGreen: Color
    Lime: Color
    LimeGreen: Color
    PaleGreen: Color
    LightGreen: Color
    MediumSpringGreen: Color
    SpringGreen: Color
    MediumSeaGreen: Color
    SeaGreen: Color
    ForestGreen: Color
    Green: Color
    DarkGreen: Color
    YellowGreen: Color
    OliveDrab: Color
    Olive: Color
    DarkOliveGreen: Color
    MediumAquamarine: Color
    DarkSeaGreen: Color
    LightSeaGreen: Color
    DarkCyan: Color
    Teal: Color
    Aqua: Color
    Cyan: Color
    LightCyan: Color
    PaleTurquoise: Color
    Aquamarine: Color
    Turquoise: Color
    MediumTurquoise: Color
    DarkTurquoise: Color
    CadetBlue: Color
    SteelBlue: Color
    LightSteelBlue: Color
    PowderBlue: Color
    LightBlue: Color
    SkyBlue: Color
    LightSkyBlue: Color
    DeepSkyBlue: Color
    DodgerBlue: Color
    CornflowerBlue: Color
    RoyalBlue: Color
    Blue: Color
    MediumBlue: Color
    DarkBlue: Color
    Navy: Color
    MidnightBlue: Color
    Cornsilk: Color
    BlanchedAlmond: Color
    Bisque: Color
    NavajoWhite: Color
    Wheat: Color
    BurlyWood: Color
    Tan: Color
    RosyBrown: Color
    SandyBrown: Color
    Goldenrod: Color
    DarkGoldenrod: Color
    Peru: Color
    Chocolate: Color
    SaddleBrown: Color
    Sienna: Color
    Brown: Color
    Maroon: Color
    White: Color
    Snow: Color
    Honeydew: Color
    MintCream: Color
    Azure: Color
    AliceBlue: Color
    GhostWhite: Color
    WhiteSmoke: Color
    Seashell: Color
    Beige: Color
    OldLace: Color
    FloralWhite: Color
    Ivory: Color
    AntiqueWhite: Color
    Linen: Color
    LavenderBlush: Color
    MistyRose: Color
    Gainsboro: Color
    LightGrey: Color
    Silver: Color
    DarkGray: Color
    Gray: Color
    DimGray: Color
    LightSlateGray: Color
    SlateGray: Color
    DarkSlateGray: Color
    Black: Color

class DashStyle:
    """.NET: Eto.Drawing.DashStyle"""
    def __init__(self, *args) -> None: ...
    Dashes: list
    Offset: float
    IsSolid: bool
    def Equals(self, other: DashStyle) -> bool: ...
    def GetHashCode(self, ) -> int: ...
    @staticmethod
    def Parse(value: str) -> DashStyle: ...
    def ToString(self, ) -> str: ...
    @staticmethod
    def TryParse(value: str, style: DashStyle) -> bool: ...

class DashStyles:
    """.NET: Eto.Drawing.DashStyles"""
    def __init__(self, *args) -> None: ...
    Solid: DashStyle
    Dash: DashStyle
    Dot: DashStyle
    DashDot: DashStyle
    DashDotDot: DashStyle

class FillMode:
    """.NET: Eto.Drawing.FillMode"""
    def __init__(self, *args) -> None: ...
    ...

class Font(Widget):
    """.NET: Eto.Drawing.Font"""
    def __init__(self, *args) -> None: ...
    FamilyName: str
    FontStyle: FontStyle
    FontDecoration: FontDecoration
    Family: FontFamily
    Typeface: FontTypeface
    XHeight: float
    Ascent: float
    Descent: float
    LineHeight: float
    Leading: float
    Baseline: float
    Size: float
    Bold: bool
    Italic: bool
    Underline: bool
    Strikethrough: bool
    Platform: Platform
    Handler: object
    NativeHandle: IntPtr
    Properties: PropertyStore
    ID: str
    Style: str
    ControlObject: object
    IsDisposed: bool
    def Equals(self, obj: object) -> bool: ...
    @staticmethod
    def FromFile(fileName: str, size: float, decoration: FontDecoration) -> Font: ...
    @staticmethod
    def FromStream(stream: Stream, size: float, decoration: FontDecoration) -> Font: ...
    def GetHashCode(self, ) -> int: ...
    def MeasureString(self, text: str) -> SizeF: ...
    def ToString(self, ) -> str: ...

class FontDecoration:
    """.NET: Eto.Drawing.FontDecoration"""
    def __init__(self, *args) -> None: ...
    ...

class FontFamilies:
    """.NET: Eto.Drawing.FontFamilies"""
    def __init__(self, *args) -> None: ...
    Monospace: FontFamily
    Sans: FontFamily
    Serif: FontFamily
    Cursive: FontFamily
    Fantasy: FontFamily

class FontFamily(Widget):
    """.NET: Eto.Drawing.FontFamily"""
    def __init__(self, *args) -> None: ...
    Name: str
    LocalizedName: str
    Typefaces: IEnumerable
    Platform: Platform
    Handler: object
    NativeHandle: IntPtr
    Properties: PropertyStore
    ID: str
    Style: str
    ControlObject: object
    IsDisposed: bool
    def Equals(self, other: FontFamily) -> bool: ...
    @staticmethod
    def FromFiles(fileNames: list) -> FontFamily: ...
    @staticmethod
    def FromStreams(streams: list) -> FontFamily: ...
    def GetHashCode(self, ) -> int: ...
    def ToString(self, ) -> str: ...

class FontStyle:
    """.NET: Eto.Drawing.FontStyle"""
    def __init__(self, *args) -> None: ...
    ...

class FontTypeface(Widget):
    """.NET: Eto.Drawing.FontTypeface"""
    def __init__(self, *args) -> None: ...
    Family: FontFamily
    Name: str
    LocalizedName: str
    FontStyle: FontStyle
    Bold: bool
    Italic: bool
    IsSymbol: bool
    Platform: Platform
    Handler: object
    NativeHandle: IntPtr
    Properties: PropertyStore
    ID: str
    Style: str
    ControlObject: object
    IsDisposed: bool
    def Equals(self, other: FontTypeface) -> bool: ...
    def GetHashCode(self, ) -> int: ...
    def HasCharacterRange(self, start: int, end: int) -> bool: ...
    def HasCharacterRanges(self, ranges: IEnumerable) -> bool: ...
    def ToString(self, ) -> str: ...

class Fonts:
    """.NET: Eto.Drawing.Fonts"""
    def __init__(self, *args) -> None: ...
    AvailableFontFamilies: IEnumerable
    @staticmethod
    def Cached(familyName: str, size: float, style: FontStyle, decoration: FontDecoration) -> Font: ...
    @staticmethod
    def ClearCache() -> None: ...
    @staticmethod
    def Cursive(size: float, style: FontStyle, decoration: FontDecoration) -> Font: ...
    @staticmethod
    def Fantasy(size: float, style: FontStyle, decoration: FontDecoration) -> Font: ...
    @staticmethod
    def Monospace(size: float, style: FontStyle, decoration: FontDecoration) -> Font: ...
    @staticmethod
    def Sans(size: float, style: FontStyle, decoration: FontDecoration) -> Font: ...
    @staticmethod
    def Serif(size: float, style: FontStyle, decoration: FontDecoration) -> Font: ...

class FormattedText(Widget):
    """.NET: Eto.Drawing.FormattedText"""
    def __init__(self, *args) -> None: ...
    Wrap: FormattedTextWrapMode
    Trimming: FormattedTextTrimming
    Alignment: FormattedTextAlignment
    Font: Font
    Text: str
    MaximumWidth: float
    MaximumHeight: float
    MaximumSize: SizeF
    ForegroundBrush: Brush
    Platform: Platform
    Handler: object
    NativeHandle: IntPtr
    Properties: PropertyStore
    ID: str
    Style: str
    ControlObject: object
    IsDisposed: bool
    def Measure(self, ) -> SizeF: ...

class FormattedTextAlignment:
    """.NET: Eto.Drawing.FormattedTextAlignment"""
    def __init__(self, *args) -> None: ...
    ...

class FormattedTextTrimming:
    """.NET: Eto.Drawing.FormattedTextTrimming"""
    def __init__(self, *args) -> None: ...
    ...

class FormattedTextWrapMode:
    """.NET: Eto.Drawing.FormattedTextWrapMode"""
    def __init__(self, *args) -> None: ...
    ...

class GradientWrapMode:
    """.NET: Eto.Drawing.GradientWrapMode"""
    def __init__(self, *args) -> None: ...
    ...

class Graphics(Widget):
    """.NET: Eto.Drawing.Graphics"""
    def __init__(self, *args) -> None: ...
    AntiAlias: bool
    ImageInterpolation: ImageInterpolation
    DPI: float
    PointsPerPixel: float
    PixelsPerPoint: float
    PixelOffsetMode: PixelOffsetMode
    IsRetained: bool
    CurrentTransform: IMatrix
    ClipBounds: RectangleF
    Platform: Platform
    Handler: object
    NativeHandle: IntPtr
    Properties: PropertyStore
    ID: str
    Style: str
    ControlObject: object
    IsDisposed: bool
    def Clear(self, brush: SolidBrush) -> None: ...
    def DrawArc(self, color: Color, x: float, y: float, width: float, height: float, startAngle: float, sweepAngle: float) -> None: ...
    def DrawEllipse(self, color: Color, x: float, y: float, width: float, height: float) -> None: ...
    def DrawImage(self, image: Image, x: float, y: float, width: float, height: float) -> None: ...
    def DrawInsetRectangle(self, topLeftColor: Color, bottomRightColor: Color, rectangle: RectangleF, width: int) -> None: ...
    def DrawLine(self, color: Color, startx: float, starty: float, endx: float, endy: float) -> None: ...
    def DrawLines(self, color: Color, points: list) -> None: ...
    def DrawPath(self, color: Color, path: IGraphicsPath) -> None: ...
    def DrawPolygon(self, color: Color, points: list) -> None: ...
    def DrawRectangle(self, pen: Pen, x: float, y: float, width: float, height: float) -> None: ...
    def DrawText(self, font: Font, brush: Brush, frame: RectangleF, text: str, wrap: FormattedTextWrapMode, alignment: FormattedTextAlignment, trimming: FormattedTextTrimming) -> None: ...
    def FillEllipse(self, color: Color, x: float, y: float, width: float, height: float) -> None: ...
    def FillPath(self, color: Color, path: IGraphicsPath) -> None: ...
    def FillPie(self, color: Color, x: float, y: float, width: float, height: float, startAngle: float, sweepAngle: float) -> None: ...
    def FillPolygon(self, color: Color, points: list) -> None: ...
    def FillRectangle(self, color: Color, x: float, y: float, width: float, height: float) -> None: ...
    def FillRectangles(self, color: Color, rectangles: IEnumerable) -> None: ...
    def Flush(self, ) -> None: ...
    def IsVisible(self, rectangle: RectangleF) -> bool: ...
    def MeasureString(self, font: Font, text: str) -> SizeF: ...
    def MultiplyTransform(self, matrix: IMatrix) -> None: ...
    def ResetClip(self, ) -> None: ...
    def RestoreTransform(self, ) -> None: ...
    def RotateTransform(self, angle: float) -> None: ...
    def SaveTransform(self, ) -> None: ...
    def SaveTransformState(self, ) -> IDisposable: ...
    def ScaleTransform(self, scaleX: float, scaleY: float) -> None: ...
    def SetClip(self, rectangle: RectangleF) -> None: ...
    def TranslateTransform(self, offsetX: float, offsetY: float) -> None: ...

class GraphicsPath:
    """.NET: Eto.Drawing.GraphicsPath"""
    def __init__(self, *args) -> None: ...
    Bounds: RectangleF
    FillMode: FillMode
    IsEmpty: bool
    CurrentPoint: PointF
    Instantiator: Func
    def AddArc(self, x: float, y: float, width: float, height: float, startAngle: float, sweepAngle: float) -> None: ...
    def AddBezier(self, start: PointF, control1: PointF, control2: PointF, end: PointF) -> None: ...
    def AddCurve(self, points: IEnumerable, tension: float) -> None: ...
    def AddEllipse(self, x: float, y: float, width: float, height: float) -> None: ...
    def AddLine(self, startX: float, startY: float, endX: float, endY: float) -> None: ...
    def AddLines(self, points: IEnumerable) -> None: ...
    def AddPath(self, path: IGraphicsPath, connect: bool) -> None: ...
    def AddRectangle(self, x: float, y: float, width: float, height: float) -> None: ...
    def Clone(self, ) -> IGraphicsPath: ...
    def CloseFigure(self, ) -> None: ...
    @staticmethod
    def Create() -> IGraphicsPath: ...
    def Dispose(self, ) -> None: ...
    def FillContains(self, point: PointF) -> bool: ...
    @staticmethod
    def GetRoundRect(rectangle: RectangleF, nwRadius: float, neRadius: float, seRadius: float, swRadius: float) -> IGraphicsPath: ...
    def LineTo(self, x: float, y: float) -> None: ...
    def MoveTo(self, x: float, y: float) -> None: ...
    def StartFigure(self, ) -> None: ...
    def StrokeContains(self, pen: Pen, point: PointF) -> bool: ...
    def Transform(self, matrix: IMatrix) -> None: ...

class GraphicsPathExtensions:
    """.NET: Eto.Drawing.GraphicsPathExtensions"""
    def __init__(self, *args) -> None: ...
    @staticmethod
    def AddArc(path: IGraphicsPath, location: RectangleF, startAngle: float, sweepAngle: float) -> None: ...
    @staticmethod
    def AddCurve(path: IGraphicsPath, tension: float, points: list) -> None: ...
    @staticmethod
    def AddEllipse(path: IGraphicsPath, location: RectangleF) -> None: ...
    @staticmethod
    def AddLine(path: IGraphicsPath, start: PointF, end: PointF) -> None: ...
    @staticmethod
    def AddLines(path: IGraphicsPath, points: list) -> None: ...
    @staticmethod
    def AddRectangle(path: IGraphicsPath, location: RectangleF) -> None: ...
    @staticmethod
    def LineTo(path: IGraphicsPath, point: PointF) -> None: ...
    @staticmethod
    def MoveTo(path: IGraphicsPath, point: PointF) -> None: ...

class IGraphicsPath:
    """.NET: Eto.Drawing.IGraphicsPath"""
    def __init__(self, *args) -> None: ...
    Bounds: RectangleF
    FillMode: FillMode
    IsEmpty: bool
    CurrentPoint: PointF
    def AddArc(self, x: float, y: float, width: float, height: float, startAngle: float, sweepAngle: float) -> None: ...
    def AddBezier(self, start: PointF, control1: PointF, control2: PointF, end: PointF) -> None: ...
    def AddCurve(self, points: IEnumerable, tension: float) -> None: ...
    def AddEllipse(self, x: float, y: float, width: float, height: float) -> None: ...
    def AddLine(self, startX: float, startY: float, endX: float, endY: float) -> None: ...
    def AddLines(self, points: IEnumerable) -> None: ...
    def AddPath(self, path: IGraphicsPath, connect: bool) -> None: ...
    def AddRectangle(self, x: float, y: float, width: float, height: float) -> None: ...
    def Clone(self, ) -> IGraphicsPath: ...
    def CloseFigure(self, ) -> None: ...
    def FillContains(self, point: PointF) -> bool: ...
    def LineTo(self, x: float, y: float) -> None: ...
    def MoveTo(self, x: float, y: float) -> None: ...
    def StartFigure(self, ) -> None: ...
    def StrokeContains(self, pen: Pen, point: PointF) -> bool: ...
    def Transform(self, matrix: IMatrix) -> None: ...

class ILockableImage:
    """.NET: Eto.Drawing.ILockableImage"""
    def __init__(self, *args) -> None: ...
    def Lock(self, ) -> BitmapData: ...
    def Unlock(self, bitmapData: BitmapData) -> None: ...

class IMatrix:
    """.NET: Eto.Drawing.IMatrix"""
    def __init__(self, *args) -> None: ...
    Elements: list
    Xx: float
    Yx: float
    Xy: float
    Yy: float
    X0: float
    Y0: float
    def Append(self, matrix: IMatrix) -> None: ...
    def Clone(self, ) -> IMatrix: ...
    def Invert(self, ) -> None: ...
    def Prepend(self, matrix: IMatrix) -> None: ...
    def Rotate(self, angle: float) -> None: ...
    def RotateAt(self, angle: float, centerX: float, centerY: float) -> None: ...
    def Scale(self, scaleX: float, scaleY: float) -> None: ...
    def ScaleAt(self, scaleX: float, scaleY: float, centerX: float, centerY: float) -> None: ...
    def Skew(self, skewX: float, skewY: float) -> None: ...
    def TransformPoint(self, point: Point) -> PointF: ...
    def Translate(self, offsetX: float, offsetY: float) -> None: ...

class ITransformBrush:
    """.NET: Eto.Drawing.ITransformBrush"""
    def __init__(self, *args) -> None: ...
    Transform: IMatrix

class Icon(Image):
    """.NET: Eto.Drawing.Icon"""
    def __init__(self, *args) -> None: ...
    Frames: IEnumerable
    Size: Size
    Width: int
    Height: int
    Platform: Platform
    Handler: object
    NativeHandle: IntPtr
    Properties: PropertyStore
    ID: str
    Style: str
    ControlObject: object
    IsDisposed: bool
    @staticmethod
    def FromResource(resourceName: str, assembly: Assembly) -> Icon: ...
    def GetFrame(self, scale: float, fittingSize: Nullable) -> IconFrame: ...
    def WithSize(self, width: int, height: int) -> Icon: ...

class IconFrame:
    """.NET: Eto.Drawing.IconFrame"""
    def __init__(self, *args) -> None: ...
    ControlObject: object
    PixelSize: Size
    Scale: float
    Size: Size
    Bitmap: Bitmap
    @staticmethod
    def FromControlObject(scale: float, controlObject: object) -> IconFrame: ...
    @staticmethod
    def FromResource(scale: float, resourceName: str, assembly: Assembly) -> IconFrame: ...

class Image(Widget):
    """.NET: Eto.Drawing.Image"""
    def __init__(self, *args) -> None: ...
    Size: Size
    Width: int
    Height: int
    Platform: Platform
    Handler: object
    NativeHandle: IntPtr
    Properties: PropertyStore
    ID: str
    Style: str
    ControlObject: object
    IsDisposed: bool

class ImageConverter(TypeConverter):
    """.NET: Eto.Drawing.ImageConverter"""
    def __init__(self, *args) -> None: ...
    def CanConvertFrom(self, context: ITypeDescriptorContext, sourceType: Type) -> bool: ...
    def CanConvertTo(self, context: ITypeDescriptorContext, destinationType: Type) -> bool: ...
    def ConvertFrom(self, context: ITypeDescriptorContext, culture: CultureInfo, value: object) -> object: ...

class ImageFormat:
    """.NET: Eto.Drawing.ImageFormat"""
    def __init__(self, *args) -> None: ...
    ...

class ImageInterpolation:
    """.NET: Eto.Drawing.ImageInterpolation"""
    def __init__(self, *args) -> None: ...
    ...

class IndexedBitmap(Image):
    """.NET: Eto.Drawing.IndexedBitmap"""
    def __init__(self, *args) -> None: ...
    BitsPerPixel: int
    Palette: Palette
    Size: Size
    Width: int
    Height: int
    Platform: Platform
    Handler: object
    NativeHandle: IntPtr
    Properties: PropertyStore
    ID: str
    Style: str
    ControlObject: object
    IsDisposed: bool
    def Lock(self, ) -> BitmapData: ...
    def Resize(self, width: int, height: int) -> None: ...

class LinearGradientBrush(Brush):
    """.NET: Eto.Drawing.LinearGradientBrush"""
    def __init__(self, *args) -> None: ...
    Handler: object
    Instantiator: Func
    Transform: IMatrix
    Wrap: GradientWrapMode
    ControlObject: object

class Matrix:
    """.NET: Eto.Drawing.Matrix"""
    def __init__(self, *args) -> None: ...
    Instantiator: Func
    InstantiatorWithElements: Func
    @staticmethod
    def Append(matrix: IMatrix, matrices: list) -> None: ...
    @staticmethod
    def Create(xx: float, yx: float, xy: float, yy: float, x0: float, y0: float) -> IMatrix: ...
    @staticmethod
    def FromRotation(angle: float) -> IMatrix: ...
    @staticmethod
    def FromRotationAt(angle: float, centerX: float, centerY: float) -> IMatrix: ...
    @staticmethod
    def FromScale(scaleX: float, scaleY: float) -> IMatrix: ...
    @staticmethod
    def FromScaleAt(scaleX: float, scaleY: float, centerX: float, centerY: float) -> IMatrix: ...
    @staticmethod
    def FromSkew(skewX: float, skewY: float) -> IMatrix: ...
    @staticmethod
    def FromTranslation(distanceX: float, distanceY: float) -> IMatrix: ...
    @staticmethod
    def GetScale(matrix: IMatrix) -> PointF: ...
    @staticmethod
    def Inverse(matrix: IMatrix) -> IMatrix: ...
    @staticmethod
    def Multiply(matrix: IMatrix, matrices: list) -> IMatrix: ...
    @staticmethod
    def Prepend(matrix: IMatrix, matrices: list) -> None: ...
    @staticmethod
    def RotateAt(matrix: IMatrix, angle: float, center: PointF) -> None: ...
    @staticmethod
    def Scale(matrix: IMatrix, scale: SizeF) -> None: ...
    @staticmethod
    def ScaleAt(matrix: IMatrix, scale: float, centerX: float, centerY: float) -> None: ...
    @staticmethod
    def TransformRectangle(matrix: IMatrix, rect: RectangleF) -> RectangleF: ...
    @staticmethod
    def TransformSize(matrix: IMatrix, size: SizeF) -> SizeF: ...
    @staticmethod
    def Translate(matrix: IMatrix, offset: SizeF) -> None: ...

class Padding:
    """.NET: Eto.Drawing.Padding"""
    def __init__(self, *args) -> None: ...
    Top: int
    Left: int
    Right: int
    Bottom: int
    Horizontal: int
    Vertical: int
    Size: Size
    IsZero: bool
    @staticmethod
    def Ceiling(padding: PaddingF) -> Padding: ...
    def Equals(self, obj: object) -> bool: ...
    def GetHashCode(self, ) -> int: ...
    @staticmethod
    def Round(padding: PaddingF) -> Padding: ...
    def ToString(self, ) -> str: ...
    @staticmethod
    def Truncate(padding: PaddingF) -> Padding: ...

class PaddingConverter(TypeConverter):
    """.NET: Eto.Drawing.PaddingConverter"""
    def __init__(self, *args) -> None: ...
    def CanConvertFrom(self, context: ITypeDescriptorContext, sourceType: Type) -> bool: ...
    def ConvertFrom(self, context: ITypeDescriptorContext, culture: CultureInfo, value: object) -> object: ...

class PaddingF:
    """.NET: Eto.Drawing.PaddingF"""
    def __init__(self, *args) -> None: ...
    Top: float
    Left: float
    Right: float
    Bottom: float
    Horizontal: float
    Vertical: float
    Size: SizeF
    IsZero: bool
    def Equals(self, obj: object) -> bool: ...
    def GetHashCode(self, ) -> int: ...
    def ToString(self, ) -> str: ...

class Palette(ObservableCollection):
    """.NET: Eto.Drawing.Palette"""
    def __init__(self, *args) -> None: ...
    EGAColors: list
    Count: int
    Item: Color
    def AddRange(self, colors: IEnumerable) -> None: ...
    def Clone(self, ) -> Palette: ...
    def Equals(self, obj: object) -> bool: ...
    def FindAddColour(self, color: Color) -> int: ...
    def FindClosest(self, color: Color) -> int: ...
    @staticmethod
    def FromEGA(palEGA: Palette) -> Palette: ...
    @staticmethod
    def GetDosPalette() -> Palette: ...
    @staticmethod
    def GetEgaPalette() -> Palette: ...
    def GetHashCode(self, ) -> int: ...
    def GetRGBColor(self, index: int) -> int: ...
    def Load(self, reader: BinaryReader, size: int, shift: int, includeAlpha: bool) -> None: ...
    def Save(self, writer: BinaryWriter, shift: int, includeAlpha: bool) -> None: ...

class Pen:
    """.NET: Eto.Drawing.Pen"""
    def __init__(self, *args) -> None: ...
    ControlObject: object
    Handler: object
    Instantiator: Func
    Color: Color
    Brush: Brush
    Thickness: float
    LineJoin: PenLineJoin
    LineCap: PenLineCap
    MiterLimit: float
    DashStyle: DashStyle
    def Dispose(self, ) -> None: ...

class PenLineCap:
    """.NET: Eto.Drawing.PenLineCap"""
    def __init__(self, *args) -> None: ...
    ...

class PenLineJoin:
    """.NET: Eto.Drawing.PenLineJoin"""
    def __init__(self, *args) -> None: ...
    ...

class Pens:
    """.NET: Eto.Drawing.Pens"""
    def __init__(self, *args) -> None: ...
    Transparent: Pen
    IndianRed: Pen
    LightCoral: Pen
    Salmon: Pen
    DarkSalmon: Pen
    LightSalmon: Pen
    Red: Pen
    Crimson: Pen
    Firebrick: Pen
    DarkRed: Pen
    Pink: Pen
    LightPink: Pen
    HotPink: Pen
    DeepPink: Pen
    MediumVioletRed: Pen
    PaleVioletRed: Pen
    Coral: Pen
    Tomato: Pen
    OrangeRed: Pen
    DarkOrange: Pen
    Orange: Pen
    Gold: Pen
    Yellow: Pen
    LightYellow: Pen
    LemonChiffon: Pen
    LightGoldenrodYellow: Pen
    PapayaWhip: Pen
    Moccasin: Pen
    PeachPuff: Pen
    PaleGoldenrod: Pen
    Khaki: Pen
    DarkKhaki: Pen
    Lavender: Pen
    Thistle: Pen
    Plum: Pen
    Violet: Pen
    Orchid: Pen
    Fuchsia: Pen
    Magenta: Pen
    MediumOrchid: Pen
    MediumPurple: Pen
    BlueViolet: Pen
    DarkViolet: Pen
    DarkOrchid: Pen
    DarkMagenta: Pen
    Purple: Pen
    Indigo: Pen
    DarkSlateBlue: Pen
    SlateBlue: Pen
    MediumSlateBlue: Pen
    GreenYellow: Pen
    Chartreuse: Pen
    LawnGreen: Pen
    Lime: Pen
    LimeGreen: Pen
    PaleGreen: Pen
    LightGreen: Pen
    MediumSpringGreen: Pen
    SpringGreen: Pen
    MediumSeaGreen: Pen
    SeaGreen: Pen
    ForestGreen: Pen
    Green: Pen
    DarkGreen: Pen
    YellowGreen: Pen
    OliveDrab: Pen
    Olive: Pen
    DarkOliveGreen: Pen
    MediumAquamarine: Pen
    DarkSeaGreen: Pen
    LightSeaGreen: Pen
    DarkCyan: Pen
    Teal: Pen
    Aqua: Pen
    Cyan: Pen
    LightCyan: Pen
    PaleTurquoise: Pen
    Aquamarine: Pen
    Turquoise: Pen
    MediumTurquoise: Pen
    DarkTurquoise: Pen
    CadetBlue: Pen
    SteelBlue: Pen
    LightSteelBlue: Pen
    PowderBlue: Pen
    LightBlue: Pen
    SkyBlue: Pen
    LightSkyBlue: Pen
    DeepSkyBlue: Pen
    DodgerBlue: Pen
    CornflowerBlue: Pen
    RoyalBlue: Pen
    Blue: Pen
    MediumBlue: Pen
    DarkBlue: Pen
    Navy: Pen
    MidnightBlue: Pen
    Cornsilk: Pen
    BlanchedAlmond: Pen
    Bisque: Pen
    NavajoWhite: Pen
    Wheat: Pen
    BurlyWood: Pen
    Tan: Pen
    RosyBrown: Pen
    SandyBrown: Pen
    Goldenrod: Pen
    DarkGoldenrod: Pen
    Peru: Pen
    Chocolate: Pen
    SaddleBrown: Pen
    Sienna: Pen
    Brown: Pen
    Maroon: Pen
    White: Pen
    Snow: Pen
    Honeydew: Pen
    MintCream: Pen
    Azure: Pen
    AliceBlue: Pen
    GhostWhite: Pen
    WhiteSmoke: Pen
    Seashell: Pen
    Beige: Pen
    OldLace: Pen
    FloralWhite: Pen
    Ivory: Pen
    AntiqueWhite: Pen
    Linen: Pen
    LavenderBlush: Pen
    MistyRose: Pen
    Gainsboro: Pen
    LightGrey: Pen
    Silver: Pen
    DarkGray: Pen
    Gray: Pen
    DimGray: Pen
    LightSlateGray: Pen
    SlateGray: Pen
    DarkSlateGray: Pen
    Black: Pen
    @staticmethod
    def Cached(color: Color, thickness: float, dashStyle: DashStyle) -> Pen: ...
    @staticmethod
    def ClearCache() -> None: ...

class PixelFormat:
    """.NET: Eto.Drawing.PixelFormat"""
    def __init__(self, *args) -> None: ...
    ...

class PixelOffsetMode:
    """.NET: Eto.Drawing.PixelOffsetMode"""
    def __init__(self, *args) -> None: ...
    ...

class Point:
    """.NET: Eto.Drawing.Point"""
    def __init__(self, *args) -> None: ...
    X: int
    Y: int
    Normal: Point
    UnitVector: PointF
    Length: float
    LengthSquared: int
    IsZero: bool
    @staticmethod
    def Abs(point: Point) -> Point: ...
    @staticmethod
    def Distance(point1: Point, point2: Point) -> float: ...
    @staticmethod
    def DotProduct(point1: Point, point2: Point) -> int: ...
    def Equals(self, obj: object) -> bool: ...
    def GetHashCode(self, ) -> int: ...
    @staticmethod
    def Max(point1: Point, point2: Point) -> Point: ...
    @staticmethod
    def Min(point1: Point, point2: Point) -> Point: ...
    @staticmethod
    def Offset(point: Point, x: int, y: int) -> Point: ...
    @staticmethod
    def Restrict(point: Point, rectangle: Rectangle) -> Point: ...
    @staticmethod
    def Round(point: PointF) -> Point: ...
    def ToString(self, ) -> str: ...
    @staticmethod
    def Truncate(point: PointF) -> Point: ...
    @staticmethod
    def UnitVectorAtAngle(angle: float) -> PointF: ...

class PointConverter(TypeConverter):
    """.NET: Eto.Drawing.PointConverter"""
    def __init__(self, *args) -> None: ...
    def CanConvertFrom(self, context: ITypeDescriptorContext, sourceType: Type) -> bool: ...
    def ConvertFrom(self, context: ITypeDescriptorContext, culture: CultureInfo, value: object) -> object: ...

class PointF:
    """.NET: Eto.Drawing.PointF"""
    def __init__(self, *args) -> None: ...
    X: float
    Y: float
    Normal: PointF
    UnitVector: PointF
    Angle: float
    Length: float
    LengthSquared: float
    IsZero: bool
    @staticmethod
    def Abs(point: PointF) -> PointF: ...
    def AngleTo(self, destination: PointF) -> float: ...
    @staticmethod
    def Distance(point1: PointF, point2: PointF) -> float: ...
    @staticmethod
    def DotProduct(point1: PointF, point2: PointF) -> float: ...
    def Equals(self, obj: object) -> bool: ...
    def GetHashCode(self, ) -> int: ...
    def LengthTo(self, destination: PointF) -> float: ...
    @staticmethod
    def Max(point1: PointF, point2: PointF) -> PointF: ...
    @staticmethod
    def Min(point1: PointF, point2: PointF) -> PointF: ...
    @staticmethod
    def Offset(point: PointF, x: float, y: float) -> PointF: ...
    @staticmethod
    def Restrict(point: Point, rectangle: Rectangle) -> Point: ...
    @staticmethod
    def Rotate(point: PointF, angle: float) -> PointF: ...
    def ToString(self, ) -> str: ...
    @staticmethod
    def UnitVectorAtAngle(angle: float) -> PointF: ...

class PointFConverter(TypeConverter):
    """.NET: Eto.Drawing.PointFConverter"""
    def __init__(self, *args) -> None: ...
    def CanConvertFrom(self, context: ITypeDescriptorContext, sourceType: Type) -> bool: ...
    def ConvertFrom(self, context: ITypeDescriptorContext, culture: CultureInfo, value: object) -> object: ...

class RadialGradientBrush(Brush):
    """.NET: Eto.Drawing.RadialGradientBrush"""
    def __init__(self, *args) -> None: ...
    Handler: object
    Instantiator: Func
    Transform: IMatrix
    Wrap: GradientWrapMode
    ControlObject: object

class Rectangle:
    """.NET: Eto.Drawing.Rectangle"""
    def __init__(self, *args) -> None: ...
    IsZero: bool
    IsEmpty: bool
    Location: Point
    EndLocation: Point
    Size: Size
    X: int
    Y: int
    Width: int
    Height: int
    Top: int
    Left: int
    Right: int
    Bottom: int
    TopLeft: Point
    TopRight: Point
    BottomRight: Point
    BottomLeft: Point
    MiddleLeft: Point
    MiddleRight: Point
    MiddleTop: Point
    MiddleBottom: Point
    InnerTopRight: Point
    InnerBottomRight: Point
    InnerBottomLeft: Point
    InnerBottom: int
    InnerRight: int
    Center: Point
    MiddleX: int
    MiddleY: int
    @staticmethod
    def Align(rectangle: Rectangle, gridWidth: int, gridHeight: int) -> Rectangle: ...
    @staticmethod
    def Ceiling(rectangle: RectangleF) -> Rectangle: ...
    def Contains(self, x: int, y: int) -> bool: ...
    def Equals(self, obj: object) -> bool: ...
    @staticmethod
    def FromCenter(center: Point, size: Size) -> Rectangle: ...
    @staticmethod
    def FromSides(left: int, top: int, right: int, bottom: int) -> Rectangle: ...
    def GetHashCode(self, ) -> int: ...
    @staticmethod
    def Inflate(rectangle: Rectangle, width: int, height: int) -> Rectangle: ...
    @staticmethod
    def Inset(rectangle: Rectangle, padding: Padding) -> Rectangle: ...
    @staticmethod
    def Intersect(rect1: Rectangle, rect2: Rectangle) -> Rectangle: ...
    def Intersects(self, rectangle: Rectangle) -> bool: ...
    def Normalize(self, ) -> None: ...
    @staticmethod
    def Offset(rectangle: Rectangle, x: int, y: int) -> Rectangle: ...
    def Restrict(self, location: Point, size: Size) -> None: ...
    @staticmethod
    def Round(rectangle: RectangleF) -> Rectangle: ...
    def ToString(self, ) -> str: ...
    @staticmethod
    def Truncate(rectangle: RectangleF) -> Rectangle: ...
    @staticmethod
    def Union(rect1: Rectangle, rect2: Rectangle) -> Rectangle: ...

class RectangleConverter(TypeConverter):
    """.NET: Eto.Drawing.RectangleConverter"""
    def __init__(self, *args) -> None: ...
    def CanConvertFrom(self, context: ITypeDescriptorContext, sourceType: Type) -> bool: ...
    def ConvertFrom(self, context: ITypeDescriptorContext, culture: CultureInfo, value: object) -> object: ...

class RectangleF:
    """.NET: Eto.Drawing.RectangleF"""
    def __init__(self, *args) -> None: ...
    IsZero: bool
    IsEmpty: bool
    Location: PointF
    EndLocation: PointF
    Size: SizeF
    X: float
    Y: float
    Width: float
    Height: float
    Top: float
    Left: float
    Right: float
    Bottom: float
    TopLeft: PointF
    TopRight: PointF
    BottomRight: PointF
    BottomLeft: PointF
    MiddleLeft: PointF
    MiddleRight: PointF
    MiddleTop: PointF
    MiddleBottom: PointF
    InnerTopRight: PointF
    InnerBottomRight: PointF
    InnerBottomLeft: PointF
    InnerBottom: float
    InnerRight: float
    Center: PointF
    MiddleX: float
    MiddleY: float
    @staticmethod
    def Align(rectangle: RectangleF, gridWidth: float, gridHeight: float) -> RectangleF: ...
    def Contains(self, x: float, y: float) -> bool: ...
    @staticmethod
    def Distance(rect: RectangleF, point: PointF) -> SizeF: ...
    def Equals(self, obj: object) -> bool: ...
    @staticmethod
    def FromCenter(center: PointF, size: SizeF) -> RectangleF: ...
    @staticmethod
    def FromSides(left: float, top: float, right: float, bottom: float) -> RectangleF: ...
    def GetHashCode(self, ) -> int: ...
    @staticmethod
    def Inflate(rectangle: RectangleF, width: float, height: float) -> RectangleF: ...
    @staticmethod
    def Inset(rectangle: RectangleF, padding: PaddingF) -> RectangleF: ...
    @staticmethod
    def Intersect(rect1: RectangleF, rect2: RectangleF) -> RectangleF: ...
    def Intersects(self, rectangle: RectangleF) -> bool: ...
    def Normalize(self, ) -> None: ...
    @staticmethod
    def Offset(rectangle: RectangleF, x: float, y: float) -> RectangleF: ...
    def Restrict(self, point: PointF, size: SizeF) -> None: ...
    def ToString(self, ) -> str: ...
    @staticmethod
    def Union(rect1: RectangleF, rect2: RectangleF) -> RectangleF: ...

class RectangleFConverter(TypeConverter):
    """.NET: Eto.Drawing.RectangleFConverter"""
    def __init__(self, *args) -> None: ...
    def CanConvertFrom(self, context: ITypeDescriptorContext, sourceType: Type) -> bool: ...
    def ConvertFrom(self, context: ITypeDescriptorContext, culture: CultureInfo, value: object) -> object: ...

class Region(Widget):
    """.NET: Eto.Drawing.Region"""
    def __init__(self, *args) -> None: ...
    Platform: Platform
    Handler: object
    NativeHandle: IntPtr
    Properties: PropertyStore
    ID: str
    Style: str
    ControlObject: object
    IsDisposed: bool
    def Exclude(self, rectangle: Rectangle) -> None: ...
    def Reset(self, ) -> None: ...
    def Set(self, rectangle: Rectangle) -> None: ...

class Size:
    """.NET: Eto.Drawing.Size"""
    def __init__(self, *args) -> None: ...
    Width: int
    Height: int
    IsZero: bool
    IsEmpty: bool
    @staticmethod
    def Abs(size: Size) -> Size: ...
    @staticmethod
    def Ceiling(size: SizeF) -> Size: ...
    def Contains(self, x: int, y: int) -> bool: ...
    def Equals(self, obj: object) -> bool: ...
    def FitTo(self, constraint: Size) -> Size: ...
    def GetHashCode(self, ) -> int: ...
    @staticmethod
    def Max(size1: Size, size2: Size) -> Size: ...
    @staticmethod
    def Min(size1: Size, size2: Size) -> Size: ...
    @staticmethod
    def Round(size: SizeF) -> Size: ...
    def ToString(self, ) -> str: ...
    @staticmethod
    def Truncate(size: SizeF) -> Size: ...

class SizeConverter(TypeConverter):
    """.NET: Eto.Drawing.SizeConverter"""
    def __init__(self, *args) -> None: ...
    def CanConvertFrom(self, context: ITypeDescriptorContext, sourceType: Type) -> bool: ...
    def ConvertFrom(self, context: ITypeDescriptorContext, culture: CultureInfo, value: object) -> object: ...

class SizeF:
    """.NET: Eto.Drawing.SizeF"""
    def __init__(self, *args) -> None: ...
    Width: float
    Height: float
    IsZero: bool
    IsEmpty: bool
    @staticmethod
    def Abs(size: SizeF) -> SizeF: ...
    def Contains(self, x: float, y: float) -> bool: ...
    def Equals(self, obj: object) -> bool: ...
    def FitTo(self, constraint: SizeF) -> SizeF: ...
    def GetHashCode(self, ) -> int: ...
    @staticmethod
    def Max(size1: SizeF, size2: SizeF) -> SizeF: ...
    @staticmethod
    def Min(size1: SizeF, size2: SizeF) -> SizeF: ...
    def ToString(self, ) -> str: ...

class SizeFConverter(TypeConverter):
    """.NET: Eto.Drawing.SizeFConverter"""
    def __init__(self, *args) -> None: ...
    def CanConvertFrom(self, context: ITypeDescriptorContext, sourceType: Type) -> bool: ...
    def ConvertFrom(self, context: ITypeDescriptorContext, culture: CultureInfo, value: object) -> object: ...

class SolidBrush(Brush):
    """.NET: Eto.Drawing.SolidBrush"""
    def __init__(self, *args) -> None: ...
    Handler: object
    Instantiator: Func
    Color: Color
    ControlObject: object

class SystemColors:
    """.NET: Eto.Drawing.SystemColors"""
    def __init__(self, *args) -> None: ...
    DisabledText: Color
    ControlText: Color
    HighlightText: Color
    Control: Color
    ControlBackground: Color
    Highlight: Color
    WindowBackground: Color
    SelectionText: Color
    Selection: Color
    LinkText: Color

class SystemFont:
    """.NET: Eto.Drawing.SystemFont"""
    def __init__(self, *args) -> None: ...
    ...

class SystemFonts:
    """.NET: Eto.Drawing.SystemFonts"""
    def __init__(self, *args) -> None: ...
    @staticmethod
    def Bold(size: Nullable, decoration: FontDecoration) -> Font: ...
    @staticmethod
    def Cached(systemFont: SystemFont, size: Nullable, decoration: FontDecoration) -> Font: ...
    @staticmethod
    def ClearCache() -> None: ...
    @staticmethod
    def Default(size: Nullable, decoration: FontDecoration) -> Font: ...
    @staticmethod
    def Label(size: Nullable, decoration: FontDecoration) -> Font: ...
    @staticmethod
    def Menu(size: Nullable, decoration: FontDecoration) -> Font: ...
    @staticmethod
    def MenuBar(size: Nullable, decoration: FontDecoration) -> Font: ...
    @staticmethod
    def Message(size: Nullable, decoration: FontDecoration) -> Font: ...
    @staticmethod
    def Palette(size: Nullable, decoration: FontDecoration) -> Font: ...
    @staticmethod
    def StatusBar(size: Nullable, decoration: FontDecoration) -> Font: ...
    @staticmethod
    def TitleBar(size: Nullable, decoration: FontDecoration) -> Font: ...
    @staticmethod
    def ToolTip(size: Nullable, decoration: FontDecoration) -> Font: ...
    @staticmethod
    def User(size: Nullable, decoration: FontDecoration) -> Font: ...

class SystemIconSize:
    """.NET: Eto.Drawing.SystemIconSize"""
    def __init__(self, *args) -> None: ...
    ...

class SystemIconType:
    """.NET: Eto.Drawing.SystemIconType"""
    def __init__(self, *args) -> None: ...
    ...

class SystemIcons:
    """.NET: Eto.Drawing.SystemIcons"""
    def __init__(self, *args) -> None: ...
    @staticmethod
    def Get(type: SystemIconType, size: SystemIconSize) -> Icon: ...
    @staticmethod
    def GetFileIcon(fileName: str, size: SystemIconSize) -> Icon: ...

class TextureBrush(Brush):
    """.NET: Eto.Drawing.TextureBrush"""
    def __init__(self, *args) -> None: ...
    Image: Image
    Handler: object
    Instantiator: Func
    Transform: IMatrix
    Opacity: float
    ControlObject: object
