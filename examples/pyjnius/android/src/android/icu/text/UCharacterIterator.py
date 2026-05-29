from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["UCharacterIterator"]

class UCharacterIterator(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/icu/text/UCharacterIterator"
    DONE = JavaStaticField("I")
    moveCodePointIndex = JavaMethod("(I)I")
    currentCodePoint = JavaMethod("()I")
    setToLimit = JavaMethod("()V")
    moveIndex = JavaMethod("(I)I")
    previousCodePoint = JavaMethod("()I")
    setToStart = JavaMethod("()V")
    nextCodePoint = JavaMethod("()I")
    getCharacterIterator = JavaMethod("()Ljava/text/CharacterIterator;")
    clone = JavaMethod("()Ljava/lang/Object;")
    getLength = JavaMethod("()I")
    next = JavaMethod("()I")
    getInstance = JavaMultipleMethod([("(Ljava/lang/String;)Landroid/icu/text/UCharacterIterator;", True, False), ("(Landroid/icu/text/Replaceable;)Landroid/icu/text/UCharacterIterator;", True, False), ("([C)Landroid/icu/text/UCharacterIterator;", True, False), ("(Ljava/lang/StringBuffer;)Landroid/icu/text/UCharacterIterator;", True, False), ("(Ljava/text/CharacterIterator;)Landroid/icu/text/UCharacterIterator;", True, False), ("([CII)Landroid/icu/text/UCharacterIterator;", True, False)])
    current = JavaMethod("()I")
    getText = JavaMultipleMethod([("([CI)I", False, False), ("()Ljava/lang/String;", False, False), ("([C)I", False, False)])
    setIndex = JavaMethod("(I)V")
    getIndex = JavaMethod("()I")
    previous = JavaMethod("()I")