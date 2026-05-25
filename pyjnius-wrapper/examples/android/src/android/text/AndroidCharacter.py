from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["AndroidCharacter"]

class AndroidCharacter(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/text/AndroidCharacter"
    __javaconstructor__ = [("()V", False)]
    EAST_ASIAN_WIDTH_AMBIGUOUS = JavaStaticField("I")
    EAST_ASIAN_WIDTH_FULL_WIDTH = JavaStaticField("I")
    EAST_ASIAN_WIDTH_HALF_WIDTH = JavaStaticField("I")
    EAST_ASIAN_WIDTH_NARROW = JavaStaticField("I")
    EAST_ASIAN_WIDTH_NEUTRAL = JavaStaticField("I")
    EAST_ASIAN_WIDTH_WIDE = JavaStaticField("I")
    getDirectionalities = JavaStaticMethod("([C[BI)V")
    getEastAsianWidth = JavaStaticMethod("(C)I")
    getEastAsianWidths = JavaStaticMethod("([CII[B)V")
    mirror = JavaStaticMethod("([CII)Z")
    getMirror = JavaStaticMethod("(C)C")