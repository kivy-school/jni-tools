from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Bidi"]

class Bidi(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/text/Bidi"
    __javaconstructor__ = [("(Ljava/lang/String;I)V", False), ("(Ljava/text/AttributedCharacterIterator;)V", False), ("([CI[BIII)V", False)]
    DIRECTION_DEFAULT_LEFT_TO_RIGHT = JavaStaticField("I")
    DIRECTION_DEFAULT_RIGHT_TO_LEFT = JavaStaticField("I")
    DIRECTION_LEFT_TO_RIGHT = JavaStaticField("I")
    DIRECTION_RIGHT_TO_LEFT = JavaStaticField("I")
    createLineBidi = JavaMethod("(II)Ljava/text/Bidi;")
    isMixed = JavaMethod("()Z")
    isLeftToRight = JavaMethod("()Z")
    isRightToLeft = JavaMethod("()Z")
    getLength = JavaMethod("()I")
    baseIsLeftToRight = JavaMethod("()Z")
    getBaseLevel = JavaMethod("()I")
    getLevelAt = JavaMethod("(I)I")
    getRunCount = JavaMethod("()I")
    getRunLevel = JavaMethod("(I)I")
    getRunStart = JavaMethod("(I)I")
    getRunLimit = JavaMethod("(I)I")
    requiresBidi = JavaStaticMethod("([CII)Z")
    reorderVisually = JavaStaticMethod("([BI[Ljava/lang/Object;II)V")
    toString = JavaMethod("()Ljava/lang/String;")