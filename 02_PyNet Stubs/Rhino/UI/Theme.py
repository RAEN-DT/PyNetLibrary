# Auto-generated — Rhino 8 — Rhino.UI.Theme

class ButtonThemeElement(CheckedThemeElement):
    """.NET: Rhino.UI.Theme.ButtonThemeElement"""
    def __init__(self, *args) -> None: ...
    Default: ButtonThemeState
    DefaultHover: ButtonThemeState
    DefaultPressed: ButtonThemeState
    Unchecked: ButtonThemeState
    UncheckedtHover: ButtonThemeState
    UncheckedPressed: ButtonThemeState
    Checked: ButtonThemeState
    CheckedHover: ButtonThemeState
    CheckedPressed: ButtonThemeState
    Enabled: ButtonThemeState
    EnabledHover: ButtonThemeState
    EnabledPressed: ButtonThemeState
    Disabled: ButtonThemeState
    Id: str
    def Enumerate(self, ) -> IEnumerable: ...

class ButtonThemeState(CheckedThemeState):
    """.NET: Rhino.UI.Theme.ButtonThemeState"""
    def __init__(self, *args) -> None: ...
    Border: Color
    Background: Color
    Text: Color
    Id: str

class CheckedThemeElement(ThemeElement):
    """.NET: Rhino.UI.Theme.CheckedThemeElement`1"""
    def __init__(self, *args) -> None: ...
    Checked: T
    CheckedHover: T
    CheckedPressed: T
    Enabled: T
    EnabledHover: T
    EnabledPressed: T
    Disabled: T
    Id: str
    def Enumerate(self, ) -> IEnumerable: ...

class CheckedThemeState(ThemeState):
    """.NET: Rhino.UI.Theme.CheckedThemeState"""
    def __init__(self, *args) -> None: ...
    Border: Color
    Background: Color
    Text: Color
    Id: str

class ContentThemeZone(ThemeZone):
    """.NET: Rhino.UI.Theme.ContentThemeZone"""
    def __init__(self, *args) -> None: ...
    MessageBoxBackground: Color
    GripperDot: Color
    Background: Color
    Highlight: Color
    HighlightHover: Color
    Divider: Color
    Button: ButtonThemeElement
    Tab: ButtonThemeElement
    Entry: EntryThemeElement
    List: ListThemeElement
    Text: TextThemeElement
    Link: LinkThemeElement
    Scrollbar: ScrollbarThemeElement
    Id: str
    def Enumerate(self, ) -> IEnumerable: ...

class EntryThemeElement(ThemeElement):
    """.NET: Rhino.UI.Theme.EntryThemeElement"""
    def __init__(self, *args) -> None: ...
    Enabled: EntryThemeState
    EnabledHover: EntryThemeState
    EnabledPressed: EntryThemeState
    Disabled: EntryThemeState
    Id: str

class EntryThemeState(ThemeState):
    """.NET: Rhino.UI.Theme.EntryThemeState"""
    def __init__(self, *args) -> None: ...
    PlaceholderText: Color
    Border: Color
    Background: Color
    Text: Color
    Id: str
    def Enumerate(self, ) -> IEnumerable: ...

class FrameThemeZone(ThemeZone):
    """.NET: Rhino.UI.Theme.FrameThemeZone"""
    def __init__(self, *args) -> None: ...
    Edge: Color
    GripperDot: Color
    Background: Color
    Highlight: Color
    HighlightHover: Color
    Divider: Color
    Button: ButtonThemeElement
    Tab: ButtonThemeElement
    Entry: EntryThemeElement
    List: ListThemeElement
    Text: TextThemeElement
    Link: LinkThemeElement
    Scrollbar: ScrollbarThemeElement
    Id: str
    def Enumerate(self, ) -> IEnumerable: ...

class IThemeEntry:
    """.NET: Rhino.UI.Theme.IThemeEntry"""
    def __init__(self, *args) -> None: ...
    Id: str
    Value: object

class LinkThemeElement(ThemeElement):
    """.NET: Rhino.UI.Theme.LinkThemeElement"""
    def __init__(self, *args) -> None: ...
    Enabled: LinkThemeState
    EnabledHover: LinkThemeState
    EnabledPressed: LinkThemeState
    Disabled: LinkThemeState
    Id: str

class LinkThemeState(ThemeState):
    """.NET: Rhino.UI.Theme.LinkThemeState"""
    def __init__(self, *args) -> None: ...
    Border: Color
    Background: Color
    Text: Color
    Id: str

class ListThemeElement(CheckedThemeElement):
    """.NET: Rhino.UI.Theme.ListThemeElement"""
    def __init__(self, *args) -> None: ...
    Focus: ListThemeState
    FocusHover: ListThemeState
    Checked: ListThemeState
    CheckedHover: ListThemeState
    CheckedPressed: ListThemeState
    Enabled: ListThemeState
    EnabledHover: ListThemeState
    EnabledPressed: ListThemeState
    Disabled: ListThemeState
    Id: str
    def Enumerate(self, ) -> IEnumerable: ...

class ListThemeState(CheckedThemeState):
    """.NET: Rhino.UI.Theme.ListThemeState"""
    def __init__(self, *args) -> None: ...
    Border: Color
    Background: Color
    Text: Color
    Id: str

class ScrollbarThemeElement(ThemeElement):
    """.NET: Rhino.UI.Theme.ScrollbarThemeElement"""
    def __init__(self, *args) -> None: ...
    Size: float
    ArrowSize: float
    Radius: float
    Enabled: ScrollbarThemeState
    EnabledHover: ScrollbarThemeState
    EnabledPressed: ScrollbarThemeState
    Disabled: ScrollbarThemeState
    Id: str
    def Enumerate(self, ) -> IEnumerable: ...

class ScrollbarThemeState(ThemeStateBase):
    """.NET: Rhino.UI.Theme.ScrollbarThemeState"""
    def __init__(self, *args) -> None: ...
    Background: Color
    Border: Color
    Glyph: Color
    Thumb: Color
    Id: str
    def Enumerate(self, ) -> IEnumerable: ...

class TextThemeElement(ThemeElementBase):
    """.NET: Rhino.UI.Theme.TextThemeElement"""
    def __init__(self, *args) -> None: ...
    Enabled: Color
    Disabled: Color
    Highlight: Color
    HighlightHover: Color
    Id: str
    def Enumerate(self, ) -> IEnumerable: ...

class ThemeBase:
    """.NET: Rhino.UI.Theme.ThemeBase"""
    def __init__(self, *args) -> None: ...
    Id: str
    def Enumerate(self, ) -> IEnumerable: ...

class ThemeElement(ThemeElementBase):
    """.NET: Rhino.UI.Theme.ThemeElement`1"""
    def __init__(self, *args) -> None: ...
    Enabled: T
    EnabledHover: T
    EnabledPressed: T
    Disabled: T
    Id: str
    def Enumerate(self, ) -> IEnumerable: ...

class ThemeElementBase(ThemeBase):
    """.NET: Rhino.UI.Theme.ThemeElementBase"""
    def __init__(self, *args) -> None: ...
    Id: str

class ThemeState(ThemeStateBase):
    """.NET: Rhino.UI.Theme.ThemeState"""
    def __init__(self, *args) -> None: ...
    Border: Color
    Background: Color
    Text: Color
    Id: str
    def Enumerate(self, ) -> IEnumerable: ...

class ThemeStateBase(ThemeBase):
    """.NET: Rhino.UI.Theme.ThemeStateBase"""
    def __init__(self, *args) -> None: ...
    Id: str

class ThemeZone(ThemeBase):
    """.NET: Rhino.UI.Theme.ThemeZone"""
    def __init__(self, *args) -> None: ...
    GripperDot: Color
    Background: Color
    Highlight: Color
    HighlightHover: Color
    Divider: Color
    Button: ButtonThemeElement
    Tab: ButtonThemeElement
    Entry: EntryThemeElement
    List: ListThemeElement
    Text: TextThemeElement
    Link: LinkThemeElement
    Scrollbar: ScrollbarThemeElement
    Id: str
    def Enumerate(self, ) -> IEnumerable: ...
