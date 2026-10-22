# encoding: utf-8
# module System.Windows.Forms.VisualStyles calls itself VisualStyles
# from System.Windows.Forms, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089
# by generator 1.145
""" NamespaceTracker represent a CLS namespace. """
# no imports

# no functions
# classes

class BackgroundType:
    """.NET enum: System.Windows.Forms.VisualStyles.BackgroundType"""
    def __init__(self, *args) -> None: ...
    ImageFile: int  # = 0
    BorderFill: int  # = 1
    None_: int  # = 2
class BooleanProperty:
    """.NET enum: System.Windows.Forms.VisualStyles.BooleanProperty"""
    def __init__(self, *args) -> None: ...
    Transparent: int  # = 2201
    AutoSize: int  # = 2202
    BorderOnly: int  # = 2203
    Composited: int  # = 2204
    BackgroundFill: int  # = 2205
    GlyphTransparent: int  # = 2206
    GlyphOnly: int  # = 2207
    AlwaysShowSizingBar: int  # = 2208
    MirrorImage: int  # = 2209
    UniformSizing: int  # = 2210
    IntegralSizing: int  # = 2211
    SourceGrow: int  # = 2212
    SourceShrink: int  # = 2213
class BorderType:
    """.NET enum: System.Windows.Forms.VisualStyles.BorderType"""
    def __init__(self, *args) -> None: ...
    Rectangle: int  # = 0
    RoundedRectangle: int  # = 1
    Ellipse: int  # = 2
class CheckBoxState:
    """.NET enum: System.Windows.Forms.VisualStyles.CheckBoxState"""
    def __init__(self, *args) -> None: ...
    UncheckedNormal: int  # = 1
    UncheckedHot: int  # = 2
    UncheckedPressed: int  # = 3
    UncheckedDisabled: int  # = 4
    CheckedNormal: int  # = 5
    CheckedHot: int  # = 6
    CheckedPressed: int  # = 7
    CheckedDisabled: int  # = 8
    MixedNormal: int  # = 9
    MixedHot: int  # = 10
    MixedPressed: int  # = 11
    MixedDisabled: int  # = 12
class ColorProperty:
    """.NET enum: System.Windows.Forms.VisualStyles.ColorProperty"""
    def __init__(self, *args) -> None: ...
    BorderColor: int  # = 3801
    FillColor: int  # = 3802
    TextColor: int  # = 3803
    EdgeLightColor: int  # = 3804
    EdgeHighlightColor: int  # = 3805
    EdgeShadowColor: int  # = 3806
    EdgeDarkShadowColor: int  # = 3807
    EdgeFillColor: int  # = 3808
    TransparentColor: int  # = 3809
    GradientColor1: int  # = 3810
    GradientColor2: int  # = 3811
    GradientColor3: int  # = 3812
    GradientColor4: int  # = 3813
    GradientColor5: int  # = 3814
    ShadowColor: int  # = 3815
    GlowColor: int  # = 3816
    TextBorderColor: int  # = 3817
    TextShadowColor: int  # = 3818
    GlyphTextColor: int  # = 3819
    GlyphTransparentColor: int  # = 3820
    FillColorHint: int  # = 3821
    BorderColorHint: int  # = 3822
    AccentColorHint: int  # = 3823
class ComboBoxState:
    """.NET enum: System.Windows.Forms.VisualStyles.ComboBoxState"""
    def __init__(self, *args) -> None: ...
    Normal: int  # = 1
    Hot: int  # = 2
    Pressed: int  # = 3
    Disabled: int  # = 4
    Focused: int  # = 5
class ContentAlignment:
    """.NET enum: System.Windows.Forms.VisualStyles.ContentAlignment"""
    def __init__(self, *args) -> None: ...
    Left: int  # = 0
    Center: int  # = 1
    Right: int  # = 2
class EdgeEffects:
    """.NET enum: System.Windows.Forms.VisualStyles.EdgeEffects"""
    def __init__(self, *args) -> None: ...
    None_: int  # = 0
    FillInterior: int  # = 2048
    Soft: int  # = 4096
    Flat: int  # = 16384
    Mono: int  # = 32768
class Edges:
    """.NET enum: System.Windows.Forms.VisualStyles.Edges"""
    def __init__(self, *args) -> None: ...
    Left: int  # = 1
    Top: int  # = 2
    Right: int  # = 4
    Bottom: int  # = 8
    Diagonal: int  # = 16
class EdgeStyle:
    """.NET enum: System.Windows.Forms.VisualStyles.EdgeStyle"""
    def __init__(self, *args) -> None: ...
    Raised: int  # = 5
    Etched: int  # = 6
    Bump: int  # = 9
    Sunken: int  # = 10
class EnumProperty:
    """.NET enum: System.Windows.Forms.VisualStyles.EnumProperty"""
    def __init__(self, *args) -> None: ...
    BackgroundType: int  # = 4001
    BorderType: int  # = 4002
    FillType: int  # = 4003
    SizingType: int  # = 4004
    HorizontalAlignment: int  # = 4005
    ContentAlignment: int  # = 4006
    VerticalAlignment: int  # = 4007
    OffsetType: int  # = 4008
    IconEffect: int  # = 4009
    TextShadowType: int  # = 4010
    ImageLayout: int  # = 4011
    GlyphType: int  # = 4012
    ImageSelectType: int  # = 4013
    GlyphFontSizingType: int  # = 4014
    TrueSizeScalingType: int  # = 4015
class FilenameProperty:
    """.NET enum: System.Windows.Forms.VisualStyles.FilenameProperty"""
    def __init__(self, *args) -> None: ...
    ImageFile: int  # = 3001
    ImageFile1: int  # = 3002
    ImageFile2: int  # = 3003
    ImageFile3: int  # = 3004
    ImageFile4: int  # = 3005
    ImageFile5: int  # = 3006
    StockImageFile: int  # = 3007
    GlyphImageFile: int  # = 3008
class FillType:
    """.NET enum: System.Windows.Forms.VisualStyles.FillType"""
    def __init__(self, *args) -> None: ...
    Solid: int  # = 0
    VerticalGradient: int  # = 1
    HorizontalGradient: int  # = 2
    RadialGradient: int  # = 3
    TileImage: int  # = 4
class FontProperty:
    """.NET enum: System.Windows.Forms.VisualStyles.FontProperty"""
    def __init__(self, *args) -> None: ...
    TextFont: int  # = 210
    GlyphFont: int  # = 2601
class GlyphFontSizingType:
    """.NET enum: System.Windows.Forms.VisualStyles.GlyphFontSizingType"""
    def __init__(self, *args) -> None: ...
    None_: int  # = 0
    Size: int  # = 1
    Dpi: int  # = 2
class GlyphType:
    """.NET enum: System.Windows.Forms.VisualStyles.GlyphType"""
    def __init__(self, *args) -> None: ...
    None_: int  # = 0
    ImageGlyph: int  # = 1
    FontGlyph: int  # = 2
class GroupBoxState:
    """.NET enum: System.Windows.Forms.VisualStyles.GroupBoxState"""
    def __init__(self, *args) -> None: ...
    Normal: int  # = 1
    Disabled: int  # = 2
class HitTestCode:
    """.NET enum: System.Windows.Forms.VisualStyles.HitTestCode"""
    def __init__(self, *args) -> None: ...
    Nowhere: int  # = 0
    Client: int  # = 1
    Left: int  # = 10
    Right: int  # = 11
    Top: int  # = 12
    TopLeft: int  # = 13
    TopRight: int  # = 14
    Bottom: int  # = 15
    BottomLeft: int  # = 16
    BottomRight: int  # = 17
class HitTestOptions:
    """.NET enum: System.Windows.Forms.VisualStyles.HitTestOptions"""
    def __init__(self, *args) -> None: ...
    BackgroundSegment: int  # = 0
    FixedBorder: int  # = 2
    Caption: int  # = 4
    ResizingBorderLeft: int  # = 16
    ResizingBorderTop: int  # = 32
    ResizingBorderRight: int  # = 64
    ResizingBorderBottom: int  # = 128
    ResizingBorder: int  # = 240
    SizingTemplate: int  # = 256
    SystemSizingMargins: int  # = 512
class HorizontalAlign:
    """.NET enum: System.Windows.Forms.VisualStyles.HorizontalAlign"""
    def __init__(self, *args) -> None: ...
    Left: int  # = 0
    Center: int  # = 1
    Right: int  # = 2
class IconEffect:
    """.NET enum: System.Windows.Forms.VisualStyles.IconEffect"""
    def __init__(self, *args) -> None: ...
    None_: int  # = 0
    Glow: int  # = 1
    Shadow: int  # = 2
    Pulse: int  # = 3
    Alpha: int  # = 4
class ImageOrientation:
    """.NET enum: System.Windows.Forms.VisualStyles.ImageOrientation"""
    def __init__(self, *args) -> None: ...
    Vertical: int  # = 0
    Horizontal: int  # = 1
class ImageSelectType:
    """.NET enum: System.Windows.Forms.VisualStyles.ImageSelectType"""
    def __init__(self, *args) -> None: ...
    None_: int  # = 0
    Size: int  # = 1
    Dpi: int  # = 2
class IntegerProperty:
    """.NET enum: System.Windows.Forms.VisualStyles.IntegerProperty"""
    def __init__(self, *args) -> None: ...
    ImageCount: int  # = 2401
    AlphaLevel: int  # = 2402
    BorderSize: int  # = 2403
    RoundCornerWidth: int  # = 2404
    RoundCornerHeight: int  # = 2405
    GradientRatio1: int  # = 2406
    GradientRatio2: int  # = 2407
    GradientRatio3: int  # = 2408
    GradientRatio4: int  # = 2409
    GradientRatio5: int  # = 2410
    ProgressChunkSize: int  # = 2411
    ProgressSpaceSize: int  # = 2412
    Saturation: int  # = 2413
    TextBorderSize: int  # = 2414
    AlphaThreshold: int  # = 2415
    Width: int  # = 2416
    Height: int  # = 2417
    GlyphIndex: int  # = 2418
    TrueSizeStretchMark: int  # = 2419
    MinDpi1: int  # = 2420
    MinDpi2: int  # = 2421
    MinDpi3: int  # = 2422
    MinDpi4: int  # = 2423
    MinDpi5: int  # = 2424
class MarginProperty:
    """.NET enum: System.Windows.Forms.VisualStyles.MarginProperty"""
    def __init__(self, *args) -> None: ...
    SizingMargins: int  # = 3601
    ContentMargins: int  # = 3602
    CaptionMargins: int  # = 3603
class OffsetType:
    """.NET enum: System.Windows.Forms.VisualStyles.OffsetType"""
    def __init__(self, *args) -> None: ...
    TopLeft: int  # = 0
    TopRight: int  # = 1
    TopMiddle: int  # = 2
    BottomLeft: int  # = 3
    BottomRight: int  # = 4
    BottomMiddle: int  # = 5
    MiddleLeft: int  # = 6
    MiddleRight: int  # = 7
    LeftOfCaption: int  # = 8
    RightOfCaption: int  # = 9
    LeftOfLastButton: int  # = 10
    RightOfLastButton: int  # = 11
    AboveLastButton: int  # = 12
    BelowLastButton: int  # = 13
class PointProperty:
    """.NET enum: System.Windows.Forms.VisualStyles.PointProperty"""
    def __init__(self, *args) -> None: ...
    Offset: int  # = 3401
    TextShadowOffset: int  # = 3402
    MinSize: int  # = 3403
    MinSize1: int  # = 3404
    MinSize2: int  # = 3405
    MinSize3: int  # = 3406
    MinSize4: int  # = 3407
    MinSize5: int  # = 3408
class PushButtonState:
    """.NET enum: System.Windows.Forms.VisualStyles.PushButtonState"""
    def __init__(self, *args) -> None: ...
    Normal: int  # = 1
    Hot: int  # = 2
    Pressed: int  # = 3
    Disabled: int  # = 4
    Default: int  # = 5
class RadioButtonState:
    """.NET enum: System.Windows.Forms.VisualStyles.RadioButtonState"""
    def __init__(self, *args) -> None: ...
    UncheckedNormal: int  # = 1
    UncheckedHot: int  # = 2
    UncheckedPressed: int  # = 3
    UncheckedDisabled: int  # = 4
    CheckedNormal: int  # = 5
    CheckedHot: int  # = 6
    CheckedPressed: int  # = 7
    CheckedDisabled: int  # = 8
class ScrollBarArrowButtonState:
    """.NET enum: System.Windows.Forms.VisualStyles.ScrollBarArrowButtonState"""
    def __init__(self, *args) -> None: ...
    UpNormal: int  # = 1
    UpHot: int  # = 2
    UpPressed: int  # = 3
    UpDisabled: int  # = 4
    DownNormal: int  # = 5
    DownHot: int  # = 6
    DownPressed: int  # = 7
    DownDisabled: int  # = 8
    LeftNormal: int  # = 9
    LeftHot: int  # = 10
    LeftPressed: int  # = 11
    LeftDisabled: int  # = 12
    RightNormal: int  # = 13
    RightHot: int  # = 14
    RightPressed: int  # = 15
    RightDisabled: int  # = 16
class ScrollBarSizeBoxState:
    """.NET enum: System.Windows.Forms.VisualStyles.ScrollBarSizeBoxState"""
    def __init__(self, *args) -> None: ...
    RightAlign: int  # = 1
    LeftAlign: int  # = 2
class ScrollBarState:
    """.NET enum: System.Windows.Forms.VisualStyles.ScrollBarState"""
    def __init__(self, *args) -> None: ...
    Normal: int  # = 1
    Hot: int  # = 2
    Pressed: int  # = 3
    Disabled: int  # = 4
class SizingType:
    """.NET enum: System.Windows.Forms.VisualStyles.SizingType"""
    def __init__(self, *args) -> None: ...
    FixedSize: int  # = 0
    Stretch: int  # = 1
    Tile: int  # = 2
class StringProperty:
    """.NET enum: System.Windows.Forms.VisualStyles.StringProperty"""
    def __init__(self, *args) -> None: ...
    Text: int  # = 3201
class TabItemState:
    """.NET enum: System.Windows.Forms.VisualStyles.TabItemState"""
    def __init__(self, *args) -> None: ...
    Normal: int  # = 1
    Hot: int  # = 2
    Selected: int  # = 3
    Disabled: int  # = 4
class TextBoxState:
    """.NET enum: System.Windows.Forms.VisualStyles.TextBoxState"""
    def __init__(self, *args) -> None: ...
    Normal: int  # = 1
    Hot: int  # = 2
    Selected: int  # = 3
    Disabled: int  # = 4
    Readonly: int  # = 6
    Assist: int  # = 7
class TextMetrics(object):
    """ Provides basic information about the font specified by a visual style for a particular element. """
    Ascent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the ascent of characters in the font.



Get: Ascent(self: TextMetrics) -> int



Set: Ascent(self: TextMetrics) = value

"""

    AverageCharWidth = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the average width of characters in the font.



Get: AverageCharWidth(self: TextMetrics) -> int



Set: AverageCharWidth(self: TextMetrics) = value

"""

    BreakChar = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the character used to define word breaks for text justification.



Get: BreakChar(self: TextMetrics) -> Char



Set: BreakChar(self: TextMetrics) = value

"""

    CharSet = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the character set of the font.



Get: CharSet(self: TextMetrics) -> TextMetricsCharacterSet



Set: CharSet(self: TextMetrics) = value

"""

    DefaultChar = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the character to be substituted for characters not in the font.



Get: DefaultChar(self: TextMetrics) -> Char



Set: DefaultChar(self: TextMetrics) = value

"""

    Descent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the descent of characters in the font.



Get: Descent(self: TextMetrics) -> int



Set: Descent(self: TextMetrics) = value

"""

    DigitizedAspectX = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the horizontal aspect of the device for which the font was designed.



Get: DigitizedAspectX(self: TextMetrics) -> int



Set: DigitizedAspectX(self: TextMetrics) = value

"""

    DigitizedAspectY = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the vertical aspect of the device for which the font was designed.



Get: DigitizedAspectY(self: TextMetrics) -> int



Set: DigitizedAspectY(self: TextMetrics) = value

"""

    ExternalLeading = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the amount of extra leading that the application adds between rows.



Get: ExternalLeading(self: TextMetrics) -> int



Set: ExternalLeading(self: TextMetrics) = value

"""

    FirstChar = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the first character defined in the font.



Get: FirstChar(self: TextMetrics) -> Char



Set: FirstChar(self: TextMetrics) = value

"""

    Height = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the height of characters in the font.



Get: Height(self: TextMetrics) -> int



Set: Height(self: TextMetrics) = value

"""

    InternalLeading = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the amount of leading inside the bounds set by the System.Windows.Forms.VisualStyles.TextMetrics.Height property.



Get: InternalLeading(self: TextMetrics) -> int



Set: InternalLeading(self: TextMetrics) = value

"""

    Italic = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a value indicating whether the font is italic.



Get: Italic(self: TextMetrics) -> bool



Set: Italic(self: TextMetrics) = value

"""

    LastChar = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the last character defined in the font.



Get: LastChar(self: TextMetrics) -> Char



Set: LastChar(self: TextMetrics) = value

"""

    MaxCharWidth = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the width of the widest character in the font.



Get: MaxCharWidth(self: TextMetrics) -> int



Set: MaxCharWidth(self: TextMetrics) = value

"""

    Overhang = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the extra width per string that may be added to some synthesized fonts.



Get: Overhang(self: TextMetrics) -> int



Set: Overhang(self: TextMetrics) = value

"""

    PitchAndFamily = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets information about the pitch, technology, and family of a physical font.



Get: PitchAndFamily(self: TextMetrics) -> TextMetricsPitchAndFamilyValues



Set: PitchAndFamily(self: TextMetrics) = value

"""

    StruckOut = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a value indicating whether the font specifies a horizontal line through the characters.



Get: StruckOut(self: TextMetrics) -> bool



Set: StruckOut(self: TextMetrics) = value

"""

    Underlined = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a value indicating whether the font is underlined.



Get: Underlined(self: TextMetrics) -> bool



Set: Underlined(self: TextMetrics) = value

"""

    Weight = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the weight of the font.



Get: Weight(self: TextMetrics) -> int



Set: Weight(self: TextMetrics) = value

"""



class TextMetricsCharacterSet:
    """.NET enum: System.Windows.Forms.VisualStyles.TextMetricsCharacterSet"""
    def __init__(self, *args) -> None: ...
    Ansi: int  # = 0
    Default: int  # = 1
    Symbol: int  # = 2
    Mac: int  # = 77
    ShiftJis: int  # = 128
    Hangul: int  # = 129
    Johab: int  # = 130
    Gb2312: int  # = 134
    ChineseBig5: int  # = 136
    Greek: int  # = 161
    Turkish: int  # = 162
    Vietnamese: int  # = 163
    Hebrew: int  # = 177
    Arabic: int  # = 178
    Baltic: int  # = 186
    Russian: int  # = 204
    Thai: int  # = 222
    EastEurope: int  # = 238
    Oem: int  # = 255
class TextMetricsPitchAndFamilyValues:
    """.NET enum: System.Windows.Forms.VisualStyles.TextMetricsPitchAndFamilyValues"""
    def __init__(self, *args) -> None: ...
    FixedPitch: int  # = 1
    Vector: int  # = 2
    TrueType: int  # = 4
    Device: int  # = 8
class TextShadowType:
    """.NET enum: System.Windows.Forms.VisualStyles.TextShadowType"""
    def __init__(self, *args) -> None: ...
    None_: int  # = 0
    Single: int  # = 1
    Continuous: int  # = 2
class ThemeSizeType:
    """.NET enum: System.Windows.Forms.VisualStyles.ThemeSizeType"""
    def __init__(self, *args) -> None: ...
    Minimum: int  # = 0
    True_: int  # = 1
    Draw: int  # = 2
class ToolBarState:
    """.NET enum: System.Windows.Forms.VisualStyles.ToolBarState"""
    def __init__(self, *args) -> None: ...
    Normal: int  # = 1
    Hot: int  # = 2
    Pressed: int  # = 3
    Disabled: int  # = 4
    Checked: int  # = 5
    HotChecked: int  # = 6
class TrackBarThumbState:
    """.NET enum: System.Windows.Forms.VisualStyles.TrackBarThumbState"""
    def __init__(self, *args) -> None: ...
    Normal: int  # = 1
    Hot: int  # = 2
    Pressed: int  # = 3
    Disabled: int  # = 5
class TrueSizeScalingType:
    """.NET enum: System.Windows.Forms.VisualStyles.TrueSizeScalingType"""
    def __init__(self, *args) -> None: ...
    None_: int  # = 0
    Size: int  # = 1
    Dpi: int  # = 2
class VerticalAlignment:
    """.NET enum: System.Windows.Forms.VisualStyles.VerticalAlignment"""
    def __init__(self, *args) -> None: ...
    Top: int  # = 0
    Center: int  # = 1
    Bottom: int  # = 2
class VisualStyleElement(object):
    """ Identifies a control or user interface (UI) element that is drawn with visual styles. """
    @staticmethod
    def CreateElement(className, part, state):
        """
        CreateElement(className: str, part: int, state: int) -> VisualStyleElement

        

            Creates a new visual style element from the specified class, part, and state values.

        

            className: A string that represents the class name of the visual style element to be created.

            part: A value that represents the part of the visual style element to be created.

            state: A value that represents the state of the visual style element to be created.

            Returns: A System.Windows.Forms.VisualStyles.VisualStyleElement with the 

             System.Windows.Forms.VisualStyles.VisualStyleElement.ClassName, 

             System.Windows.Forms.VisualStyles.VisualStyleElement.Part, and 

             System.Windows.Forms.VisualStyles.VisualStyleElement.State properties initialized to the 

             className, part, and state parameters.
        """
        pass

    ClassName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the class name of the visual style element that this System.Windows.Forms.VisualStyles.VisualStyleElement represents.



Get: ClassName(self: VisualStyleElement) -> str



"""

    Part = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value indicating the part of the visual style element that this System.Windows.Forms.VisualStyles.VisualStyleElement represents.



Get: Part(self: VisualStyleElement) -> int



"""

    State = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value indicating the state of the visual style element that this System.Windows.Forms.VisualStyles.VisualStyleElement represents.



Get: State(self: VisualStyleElement) -> int



"""


    Button = None
    ComboBox = None
    ExplorerBar = None
    Header = None
    ListView = None
    Menu = None
    MenuBand = None
    Page = None
    ProgressBar = None
    Rebar = None
    ScrollBar = None
    Spin = None
    StartPanel = None
    Status = None
    Tab = None
    TaskBand = None
    Taskbar = None
    TaskbarClock = None
    TextBox = None
    ToolBar = None
    ToolTip = None
    TrackBar = None
    TrayNotify = None
    TreeView = None
    Window = None


class VisualStyleInformation(object):
    """ Provides information about the current visual style of the operating system. """
    Author = 'MSX'
    ColorScheme = 'NormalColor'
    Company = ''
    ControlHighlightHot = None
    Copyright = ''
    Description = ''
    DisplayName = 'Aero style'
    IsEnabledByUser = True
    IsSupportedByOS = True
    MinimumColorDepth = 0
    Size = 'NormalSize'
    SupportsFlatMenus = False
    TextControlBorder = None
    Url = ''
    Version = ''
    __all__ = []


class VisualStyleRenderer(object):
    """
    Provides methods for drawing and getting information about a System.Windows.Forms.VisualStyles.VisualStyleElement. This class cannot be inherited.

    

    VisualStyleRenderer(element: VisualStyleElement)

    VisualStyleRenderer(className: str, part: int, state: int)
    """
    def DrawBackground(self, dc, bounds, clipRectangle=None):
        """
        DrawBackground(self: VisualStyleRenderer, dc: IDeviceContext, bounds: Rectangle, clipRectangle: Rectangle)

            Draws the background image of the current visual style element within the specified bounding 

             rectangle and clipped to the specified clipping rectangle.

        

        

            dc: The System.Drawing.IDeviceContext used to draw the background image.

            bounds: A System.Drawing.Rectangle in which the background image is drawn.

            clipRectangle: A System.Drawing.Rectangle that defines a clipping rectangle for the drawing operation.

        DrawBackground(self: VisualStyleRenderer, dc: IDeviceContext, bounds: Rectangle)

            Draws the background image of the current visual style element within the specified bounding 

             rectangle.

        

        

            dc: The System.Drawing.IDeviceContext used to draw the background image.

            bounds: A System.Drawing.Rectangle in which the background image is drawn.
        """
        pass

    def DrawEdge(self, dc, bounds, edges, style, effects):
        """
        DrawEdge(self: VisualStyleRenderer, dc: IDeviceContext, bounds: Rectangle, edges: Edges, style: EdgeStyle, effects: EdgeEffects) -> Rectangle

        

            Draws one or more edges of the specified bounding rectangle.

        

            dc: The System.Drawing.IDeviceContext used to draw the edges.

            bounds: The System.Drawing.Rectangle whose bounds define the edges to draw.

            edges: A bitwise combination of the System.Windows.Forms.VisualStyles.Edges values.

            style: A bitwise combination of the System.Windows.Forms.VisualStyles.EdgeStyle values.

            effects: A bitwise combination of the System.Windows.Forms.VisualStyles.EdgeEffects values.

            Returns: A System.Drawing.Rectangle that represents the interior of the bounds parameter, minus the edges 

             that were drawn.
        """
        pass

    def DrawImage(self, g, bounds, *__args):
        """
        DrawImage(self: VisualStyleRenderer, g: Graphics, bounds: Rectangle, imageList: ImageList, imageIndex: int)

            Draws the image from the specified System.Windows.Forms.ImageList within the specified bounds.

        

            g: The System.Drawing.Graphics used to draw the image.

            bounds: A System.Drawing.Rectangle in which the image is drawn.

            imageList: An System.Windows.Forms.ImageList that contains the System.Drawing.Image to draw.

            imageIndex: The index of the System.Drawing.Image within imageList to draw.

        DrawImage(self: VisualStyleRenderer, g: Graphics, bounds: Rectangle, image: Image)

            Draws the specified image within the specified bounds.

        

            g: The System.Drawing.Graphics used to draw the image.

            bounds: A System.Drawing.Rectangle in which the image is drawn.

            image: The System.Drawing.Image to draw.
        """
        pass

    def DrawParentBackground(self, dc, bounds, childControl):
        """
        DrawParentBackground(self: VisualStyleRenderer, dc: IDeviceContext, bounds: Rectangle, childControl: Control)

            Draws the background of a control's parent in the specified area.

        

            dc: The System.Drawing.IDeviceContext used to draw the background of the parent of childControl. 

             This object typically belongs to the child control.

        

            bounds: A System.Drawing.Rectangle in which to draw the parent control's background. This rectangle 

                

            childControl: The control whose parent's background will be drawn.
        """
        pass

    def DrawText(self, dc, bounds, textToDraw, drawDisabled=None, flags=None):
        """
        DrawText(self: VisualStyleRenderer, dc: IDeviceContext, bounds: Rectangle, textToDraw: str, drawDisabled: bool, flags: TextFormatFlags)

            Draws text in the specified bounding rectangle with the option of displaying disabled text and 

             applying other text formatting.

        

        

            dc: The System.Drawing.IDeviceContext used to draw the text.

            bounds: A System.Drawing.Rectangle in which to draw the text.

            textToDraw: The text to draw.

            drawDisabled: true to draw grayed-out text; otherwise, false.

            flags: A bitwise combination of the System.Windows.Forms.TextFormatFlags values.

        DrawText(self: VisualStyleRenderer, dc: IDeviceContext, bounds: Rectangle, textToDraw: str, drawDisabled: bool)

            Draws text in the specified bounds with the option of displaying disabled text.

        

            dc: The System.Drawing.IDeviceContext used to draw the text.

            bounds: A System.Drawing.Rectangle in which to draw the text.

            textToDraw: The text to draw.

            drawDisabled: true to draw grayed-out text; otherwise, false.

        DrawText(self: VisualStyleRenderer, dc: IDeviceContext, bounds: Rectangle, textToDraw: str)

            Draws text in the specified bounds using default formatting.

        

            dc: The System.Drawing.IDeviceContext used to draw the text.

            bounds: A System.Drawing.Rectangle in which to draw the text.

            textToDraw: The text to draw.
        """
        pass

    def GetBackgroundContentRectangle(self, dc, bounds):
        """
        GetBackgroundContentRectangle(self: VisualStyleRenderer, dc: IDeviceContext, bounds: Rectangle) -> Rectangle

        

            Returns the content area for the background of the current visual style element.

        

            dc: The System.Drawing.IDeviceContext this operation will use.

            bounds: A System.Drawing.Rectangle that contains the entire background area of the current visual style 

             element.

        

            Returns: A System.Drawing.Rectangle that contains the content area for the background of the current 

             visual style element.
        """
        pass

    def GetBackgroundExtent(self, dc, contentBounds):
        """
        GetBackgroundExtent(self: VisualStyleRenderer, dc: IDeviceContext, contentBounds: Rectangle) -> Rectangle

        

            Returns the entire background area for the current visual style element.

        

            dc: The System.Drawing.IDeviceContext this operation will use.

            contentBounds: A System.Drawing.Rectangle that contains the content area of the current visual style element.

            Returns: A System.Drawing.Rectangle that contains the entire background area of the current visual style 

             element.
        """
        pass

    def GetBackgroundRegion(self, dc, bounds):
        """
        GetBackgroundRegion(self: VisualStyleRenderer, dc: IDeviceContext, bounds: Rectangle) -> Region

        

            Returns the region for the background of the current visual style element.

        

            dc: The System.Drawing.IDeviceContext this operation will use.

            bounds: A System.Drawing.Rectangle that contains the entire background area of the current visual style 

             element.

        

            Returns: The System.Drawing.Region that contains the background of the current visual style element.
        """
        pass

    def GetBoolean(self, prop):
        """
        GetBoolean(self: VisualStyleRenderer, prop: BooleanProperty) -> bool

        

            Returns the value of the specified Boolean property for the current visual style element.

        

            prop: One of the System.Windows.Forms.VisualStyles.BooleanProperty values that specifies which 

             property value to retrieve for the current visual style element.

        

            Returns: true if the property specified by the prop parameter is true for the current visual style 

             element; otherwise, false.
        """
        pass

    def GetColor(self, prop):
        """
        GetColor(self: VisualStyleRenderer, prop: ColorProperty) -> Color

        

            Returns the value of the specified color property for the current visual style element.

        

            prop: One of the System.Windows.Forms.VisualStyles.ColorProperty values that specifies which property 

             value to retrieve for the current visual style element.

        

            Returns: A System.Drawing.Color that contains the value of the property specified by the prop parameter 

             for the current visual style element.
        """
        pass

    def GetEnumValue(self, prop):
        """
        GetEnumValue(self: VisualStyleRenderer, prop: EnumProperty) -> int

        

            Returns the value of the specified enumerated type property for the current visual style element.

        

            prop: One of the System.Windows.Forms.VisualStyles.EnumProperty values that specifies which property 

             value to retrieve for the current visual style element.

        

            Returns: The integer value of the property specified by the prop parameter for the current visual style 

             element.
        """
        pass

    def GetFilename(self, prop):
        """
        GetFilename(self: VisualStyleRenderer, prop: FilenameProperty) -> str

        

            Returns the value of the specified file name property for the current visual style element.

        

            prop: One of the System.Windows.Forms.VisualStyles.FilenameProperty values that specifies which 

             property value to retrieve for the current visual style element.

        

            Returns: A System.String that contains the value of the property specified by the prop parameter for the 

             current visual style element.
        """
        pass

    def GetFont(self, dc, prop):
        """
        GetFont(self: VisualStyleRenderer, dc: IDeviceContext, prop: FontProperty) -> Font

        

            Returns the value of the specified font property for the current visual style element.

        

            dc: The System.Drawing.IDeviceContext this operation will use.

            prop: One of the System.Windows.Forms.VisualStyles.FontProperty values that specifies which property 

             value to retrieve for the current visual style element.

        

            Returns: A System.Drawing.Font that contains the value of the property specified by the prop parameter 

             for the current visual style element.
        """
        pass

    def GetInteger(self, prop):
        """
        GetInteger(self: VisualStyleRenderer, prop: IntegerProperty) -> int

        

            Returns the value of the specified integer property for the current visual style element.

        

            prop: One of the System.Windows.Forms.VisualStyles.IntegerProperty values that specifies which 

             property value to retrieve for the current visual style element.

        

            Returns: The integer value of the property specified by the prop parameter for the current visual style 

             element.
        """
        pass

    def GetMargins(self, dc, prop):
        """
        GetMargins(self: VisualStyleRenderer, dc: IDeviceContext, prop: MarginProperty) -> Padding

        

            Returns the value of the specified margins property for the current visual style element.

        

            dc: The System.Drawing.IDeviceContext this operation will use.

            prop: One of the System.Windows.Forms.VisualStyles.MarginProperty values that specifies which property 

             value to retrieve for the current visual style element.

        

            Returns: A System.Windows.Forms.Padding that contains the value of the property specified by the prop 

             parameter for the current visual style element.
        """
        pass

    def GetPartSize(self, dc, *__args):
        """
        GetPartSize(self: VisualStyleRenderer, dc: IDeviceContext, bounds: Rectangle, type: ThemeSizeType) -> Size

        

            Returns the value of the specified size property of the current visual style part using the 

             specified drawing bounds.

        

        

            dc: The System.Drawing.IDeviceContext this operation will use.

            bounds: A System.Drawing.Rectangle that contains the area in which the part will be drawn.

            type: One of the System.Windows.Forms.VisualStyles.ThemeSizeType values that specifies which size 

             value to retrieve for the part.

        

            Returns: A System.Drawing.Size that contains the size specified by the type parameter for the current 

             visual style part.

        

        GetPartSize(self: VisualStyleRenderer, dc: IDeviceContext, type: ThemeSizeType) -> Size

        

            Returns the value of the specified size property of the current visual style part.

        

            dc: The System.Drawing.IDeviceContext this operation will use.

            type: One of the System.Windows.Forms.VisualStyles.ThemeSizeType values that specifies which size 

             value to retrieve for the part.

        

            Returns: A System.Drawing.Size that contains the size specified by the type parameter for the current 

             visual style part.
        """
        pass

    def GetPoint(self, prop):
        """
        GetPoint(self: VisualStyleRenderer, prop: PointProperty) -> Point

        

            Returns the value of the specified point property for the current visual style element.

        

            prop: One of the System.Windows.Forms.VisualStyles.PointProperty values that specifies which property 

             value to retrieve for the current visual style element.

        

            Returns: A System.Drawing.Point that contains the value of the property specified by the prop parameter 

             for the current visual style element.
        """
        pass

    def GetString(self, prop):
        """
        GetString(self: VisualStyleRenderer, prop: StringProperty) -> str

        

            Returns the value of the specified string property for the current visual style element.

        

            prop: One of the System.Windows.Forms.VisualStyles.StringProperty values that specifies which property 

             value to retrieve for the current visual style element.

        

            Returns: A System.String that contains the value of the property specified by the prop parameter for the 

             current visual style element.
        """
        pass

    def GetTextExtent(self, dc, *__args):
        """
        GetTextExtent(self: VisualStyleRenderer, dc: IDeviceContext, bounds: Rectangle, textToDraw: str, flags: TextFormatFlags) -> Rectangle

        

            Returns the size and location of the specified string when drawn with the font of the current 

             visual style element within the specified initial bounding rectangle.

        

        

            dc: The System.Drawing.IDeviceContext this operation will use.

            bounds: A System.Drawing.Rectangle used to control the flow and wrapping of the text.

            textToDraw: The string to measure.

            flags: A bitwise combination of the System.Windows.Forms.TextFormatFlags values.

            Returns: A System.Drawing.Rectangle that contains the area required to fit the rendered text.

        GetTextExtent(self: VisualStyleRenderer, dc: IDeviceContext, textToDraw: str, flags: TextFormatFlags) -> Rectangle

        

            Returns the size and location of the specified string when drawn with the font of the current 

             visual style element.

        

        

            dc: The System.Drawing.IDeviceContext this operation will use.

            textToDraw: The string to measure.

            flags: A bitwise combination of the System.Windows.Forms.TextFormatFlags values.

            Returns: A System.Drawing.Rectangle that contains the area required to fit the rendered text.
        """
        pass

    def GetTextMetrics(self, dc):
        """
        GetTextMetrics(self: VisualStyleRenderer, dc: IDeviceContext) -> TextMetrics

        

            Retrieves information about the font specified by the current visual style element.

        

            dc: The System.Drawing.IDeviceContext this operation will use.

            Returns: A System.Windows.Forms.VisualStyles.TextMetrics that provides information about the font 

             specified by the current visual style element.
        """
        pass

    def HitTestBackground(self, *__args):
        """
        HitTestBackground(self: VisualStyleRenderer, dc: IDeviceContext, backgroundRectangle: Rectangle, hRgn: IntPtr, pt: Point, options: HitTestOptions) -> HitTestCode

        

            Returns a hit test code indicating whether the point is contained in the background of the 

             current visual style element and within the specified region.

        

        

            dc: The System.Drawing.IDeviceContext this operation will use.

            backgroundRectangle: A System.Drawing.Rectangle that contains the background of the current visual style element.

            hRgn: A Windows handle to a System.Drawing.Region that specifies the bounds of the hit test area 

             within the background.

        

            pt: The System.Drawing.Point to test.

            options: A bitwise combination of the System.Windows.Forms.VisualStyles.HitTestOptions values.

            Returns: A System.Windows.Forms.VisualStyles.HitTestCode that describes where pt is located in the 

             background of the current visual style element.

        

        HitTestBackground(self: VisualStyleRenderer, g: Graphics, backgroundRectangle: Rectangle, region: Region, pt: Point, options: HitTestOptions) -> HitTestCode

        

            Returns a hit test code indicating whether the point is contained in the background of the 

             current visual style element and within the specified bounds.

        

        

            g: The System.Drawing.Graphics this operation will use.

            backgroundRectangle: A System.Drawing.Rectangle that contains the background of the current visual style element.

            region: A System.Drawing.Region that specifies the bounds of the hit test area within the background.

            pt: The System.Drawing.Point to test.

            options: A bitwise combination of the System.Windows.Forms.VisualStyles.HitTestOptions values.

            Returns: A System.Windows.Forms.VisualStyles.HitTestCode that describes where pt is located in the 

             background of the current visual style element, if at all.

        

        HitTestBackground(self: VisualStyleRenderer, dc: IDeviceContext, backgroundRectangle: Rectangle, pt: Point, options: HitTestOptions) -> HitTestCode

        

            Returns a hit test code indicating whether a point is contained in the background of the current 

             visual style element.

        

        

            dc: The System.Drawing.IDeviceContext this operation will use.

            backgroundRectangle: A System.Drawing.Rectangle that contains the background of the current visual style element.

            pt: The System.Drawing.Point to test.

            options: A bitwise combination of the System.Windows.Forms.VisualStyles.HitTestOptions values.

            Returns: A System.Windows.Forms.VisualStyles.HitTestCode that describes where pt is located in the 

             background of the current visual style element.
        """
        pass

    def IsBackgroundPartiallyTransparent(self):
        """
        IsBackgroundPartiallyTransparent(self: VisualStyleRenderer) -> bool

        

            Indicates whether the background of the current visual style element has any semitransparent or 

             alpha-blended pieces.

        

            Returns: true if the background of the current visual style element has any semitransparent or 

             alpha-blended pieces; otherwise, false.
        """
        pass

    @staticmethod
    def IsElementDefined(element):
        """
        IsElementDefined(element: VisualStyleElement) -> bool

        

            Determines whether the specified visual style element is defined by the current visual style.

        

            element: A System.Windows.Forms.VisualStyles.VisualStyleElement whose class and part combination will be 

             verified.

        

            Returns: true if the combination of the System.Windows.Forms.VisualStyles.VisualStyleElement.ClassName 

             and System.Windows.Forms.VisualStyles.VisualStyleElement.Part properties of element are defined; 

             otherwise, false.
        """
        pass

    def SetParameters(self, *__args):
        """
        SetParameters(self: VisualStyleRenderer, className: str, part: int, state: int)

            Sets this System.Windows.Forms.VisualStyles.VisualStyleRenderer to the visual style element 

             represented by the specified class, part, and state values.

        

        

            className: The new value of the System.Windows.Forms.VisualStyles.VisualStyleRenderer.Class property.

            part: The new value of the System.Windows.Forms.VisualStyles.VisualStyleRenderer.Part property.

            state: The new value of the System.Windows.Forms.VisualStyles.VisualStyleRenderer.State property.

        SetParameters(self: VisualStyleRenderer, element: VisualStyleElement)

            Sets this System.Windows.Forms.VisualStyles.VisualStyleRenderer to the visual style element 

             represented by the specified System.Windows.Forms.VisualStyles.VisualStyleElement.

        

        

            element: A System.Windows.Forms.VisualStyles.VisualStyleElement that specifies the new values of the 

             System.Windows.Forms.VisualStyles.VisualStyleRenderer.Class, 

             System.Windows.Forms.VisualStyles.VisualStyleRenderer.Part, and 

             System.Windows.Forms.VisualStyles.VisualStyleRenderer.State properties.
        """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type, element: VisualStyleElement)

        __new__(cls: type, className: str, part: int, state: int)
        """
        pass

    Class = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the class name of the current visual style element.



Get: Class(self: VisualStyleRenderer) -> str



"""

    Handle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a unique identifier for the current class of visual style elements.



Get: Handle(self: VisualStyleRenderer) -> IntPtr



"""

    LastHResult = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the last error code returned by the native visual styles (UxTheme) API methods encapsulated by the System.Windows.Forms.VisualStyles.VisualStyleRenderer class.



Get: LastHResult(self: VisualStyleRenderer) -> int



"""

    Part = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the part of the current visual style element.



Get: Part(self: VisualStyleRenderer) -> int



"""

    State = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the state of the current visual style element.



Get: State(self: VisualStyleRenderer) -> int



"""


    IsSupported = True


class VisualStyleState:
    """.NET enum: System.Windows.Forms.VisualStyles.VisualStyleState"""
    def __init__(self, *args) -> None: ...
    NoneEnabled: int  # = 0
    NonClientAreaEnabled: int  # = 1
    ClientAreaEnabled: int  # = 2
    ClientAndNonClientAreasEnabled: int  # = 3
