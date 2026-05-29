from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["FontStyle"]

class FontStyle(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/graphics/fonts/FontStyle"
    __javaconstructor__ = [("()V", False), ("(II)V", False)]
    FONT_SLANT_ITALIC = JavaStaticField("I")
    FONT_SLANT_UPRIGHT = JavaStaticField("I")
    FONT_WEIGHT_BLACK = JavaStaticField("I")
    FONT_WEIGHT_BOLD = JavaStaticField("I")
    FONT_WEIGHT_EXTRA_BOLD = JavaStaticField("I")
    FONT_WEIGHT_EXTRA_LIGHT = JavaStaticField("I")
    FONT_WEIGHT_LIGHT = JavaStaticField("I")
    FONT_WEIGHT_MAX = JavaStaticField("I")
    FONT_WEIGHT_MEDIUM = JavaStaticField("I")
    FONT_WEIGHT_MIN = JavaStaticField("I")
    FONT_WEIGHT_NORMAL = JavaStaticField("I")
    FONT_WEIGHT_SEMI_BOLD = JavaStaticField("I")
    FONT_WEIGHT_THIN = JavaStaticField("I")
    FONT_WEIGHT_UNSPECIFIED = JavaStaticField("I")
    getSlant = JavaMethod("()I")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    toString = JavaMethod("()Ljava/lang/String;")
    hashCode = JavaMethod("()I")
    getWeight = JavaMethod("()I")