from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["TextRunShaper"]

class TextRunShaper(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/graphics/text/TextRunShaper"
    shapeTextRun = JavaMultipleMethod([("([CIIIIFFZLandroid/graphics/Paint;)Landroid/graphics/text/PositionedGlyphs;", True, False), ("(Ljava/lang/CharSequence;IIIIFFZLandroid/graphics/Paint;)Landroid/graphics/text/PositionedGlyphs;", True, False)])