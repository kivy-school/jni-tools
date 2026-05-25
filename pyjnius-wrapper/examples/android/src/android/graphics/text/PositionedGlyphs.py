from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["PositionedGlyphs"]

class PositionedGlyphs(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/graphics/text/PositionedGlyphs"
    NO_OVERRIDE = JavaStaticField("F")
    getAdvance = JavaMethod("()F")
    getAscent = JavaMethod("()F")
    getDescent = JavaMethod("()F")
    getOffsetX = JavaMethod("()F")
    getOffsetY = JavaMethod("()F")
    glyphCount = JavaMethod("()I")
    getFont = JavaMethod("(I)Landroid/graphics/fonts/Font;")
    getGlyphId = JavaMethod("(I)I")
    getGlyphX = JavaMethod("(I)F")
    getGlyphY = JavaMethod("(I)F")
    getFakeBold = JavaMethod("(I)Z")
    getFakeItalic = JavaMethod("(I)Z")
    getWeightOverride = JavaMethod("(I)F")
    getItalicOverride = JavaMethod("(I)F")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")
    toString = JavaMethod("()Ljava/lang/String;")