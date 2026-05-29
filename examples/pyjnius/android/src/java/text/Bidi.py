from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Bidi"]

class Bidi(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/text/Bidi"
    __javaconstructor__ = [("([CI[BIII)V", False), ("(Ljava/text/AttributedCharacterIterator;)V", False), ("(Ljava/lang/String;I)V", False)]
    DIRECTION_LEFT_TO_RIGHT = JavaStaticField("I")
    DIRECTION_RIGHT_TO_LEFT = JavaStaticField("I")
    DIRECTION_DEFAULT_LEFT_TO_RIGHT = JavaStaticField("I")
    DIRECTION_DEFAULT_RIGHT_TO_LEFT = JavaStaticField("I")
    baseIsLeftToRight = JavaMethod("()Z")
    createLineBidi = JavaMethod("(II)Ljava/text/Bidi;")
    getBaseLevel = JavaMethod("()I")
    getLevelAt = JavaMethod("(I)I")
    getRunCount = JavaMethod("()I")
    getRunLevel = JavaMethod("(I)I")
    isLeftToRight = JavaMethod("()Z")
    isMixed = JavaMethod("()Z")
    reorderVisually = JavaStaticMethod("([BI[Ljava/lang/Object;II)V")
    requiresBidi = JavaStaticMethod("([CII)Z")
    toString = JavaMethod("()Ljava/lang/String;")
    getLength = JavaMethod("()I")
    isRightToLeft = JavaMethod("()Z")
    getRunStart = JavaMethod("(I)I")
    getRunLimit = JavaMethod("(I)I")