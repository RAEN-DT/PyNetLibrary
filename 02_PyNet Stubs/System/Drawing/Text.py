# encoding: utf-8
# module System.Drawing.Text calls itself Text
# from System.Drawing, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b03f5f7f11d50a3a
# by generator 1.145
""" NamespaceTracker represent a CLS namespace. """
# no imports

# no functions
# classes

class FontCollection(object, IDisposable):
    """ Provides a base class for installed and private font collections. """
    def Dispose(self):
        """
        Dispose(self: FontCollection)

            Releases all resources used by this System.Drawing.Text.FontCollection.
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

    Families = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the array of System.Drawing.FontFamily objects associated with this System.Drawing.Text.FontCollection.



Get: Families(self: FontCollection) -> Array[FontFamily]



"""



class GenericFontFamilies:
    """.NET enum: System.Drawing.Text.GenericFontFamilies"""
    def __init__(self, *args) -> None: ...
    Serif: int  # = 0
    SansSerif: int  # = 1
    Monospace: int  # = 2
class HotkeyPrefix:
    """.NET enum: System.Drawing.Text.HotkeyPrefix"""
    def __init__(self, *args) -> None: ...
    None_: int  # = 0
    Show: int  # = 1
    Hide: int  # = 2
class InstalledFontCollection(FontCollection, IDisposable):
    """
    Represents the fonts installed on the system. This class cannot be inherited.

    

    InstalledFontCollection()
    """
    def Dispose(self):
        """
        Dispose(self: FontCollection, disposing: bool)

            Releases the unmanaged resources used by the System.Drawing.Text.FontCollection and optionally 

             releases the managed resources.

        

        

            disposing: true to release both managed and unmanaged resources; false to release only unmanaged resources.
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


class PrivateFontCollection(FontCollection, IDisposable):
    """
    Provides a collection of font families built from font files that are provided by the client application.

    

    PrivateFontCollection()
    """
    def AddFontFile(self, filename):
        """
        AddFontFile(self: PrivateFontCollection, filename: str)

            Adds a font from the specified file to this System.Drawing.Text.PrivateFontCollection.

        

            filename: A System.String that contains the file name of the font to add.
        """
        pass

    def AddMemoryFont(self, memory, length):
        """
        AddMemoryFont(self: PrivateFontCollection, memory: IntPtr, length: int)

            Adds a font contained in system memory to this System.Drawing.Text.PrivateFontCollection.

        

            memory: The memory address of the font to add.

            length: The memory length of the font to add.
        """
        pass

    def Dispose(self):
        """ Dispose(self: PrivateFontCollection, disposing: bool) """
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


class TextRenderingHint:
    """.NET enum: System.Drawing.Text.TextRenderingHint"""
    def __init__(self, *args) -> None: ...
    SystemDefault: int  # = 0
    SingleBitPerPixelGridFit: int  # = 1
    SingleBitPerPixel: int  # = 2
    AntiAliasGridFit: int  # = 3
    AntiAlias: int  # = 4
    ClearTypeGridFit: int  # = 5
