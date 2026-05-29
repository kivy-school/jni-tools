from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["TextShaper"]

class TextShaper(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/text/TextShaper"
    shapeText = JavaStaticMethod("(Ljava/lang/CharSequence;IILandroid/text/TextDirectionHeuristic;Landroid/text/TextPaint;Landroid/text/TextShaper$GlyphsConsumer;)V")

    class GlyphsConsumer(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/text/TextShaper$GlyphsConsumer"
        accept = JavaMethod("(IILandroid/graphics/text/PositionedGlyphs;Landroid/text/TextPaint;)V")