from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["PositionedGlyphs"]

class PositionedGlyphs(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/graphics/text/PositionedGlyphs"
    NO_OVERRIDE = JavaStaticField("F")
    getGlyphId = JavaMethod("(I)I")
    getOffsetX = JavaMethod("()F")
    getGlyphY = JavaMethod("(I)F")
    getFakeItalic = JavaMethod("(I)Z")
    getOffsetY = JavaMethod("()F")
    getAdvance = JavaMethod("()F")
    getAscent = JavaMethod("()F")
    getFakeBold = JavaMethod("(I)Z")
    getGlyphX = JavaMethod("(I)F")
    getItalicOverride = JavaMethod("(I)F")
    getDescent = JavaMethod("()F")
    getWeightOverride = JavaMethod("(I)F")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    toString = JavaMethod("()Ljava/lang/String;")
    hashCode = JavaMethod("()I")
    glyphCount = JavaMethod("()I")
    getFont = JavaMethod("(I)Landroid/graphics/fonts/Font;")