from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["UCharacterIterator"]

class UCharacterIterator(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/icu/text/UCharacterIterator"
    __javaconstructor__ = [("()V", False)]
    DONE = JavaStaticField("I")
    getInstance = JavaMultipleMethod([("(Landroid/icu/text/Replaceable;)Landroid/icu/text/UCharacterIterator;", True, False), ("(Ljava/lang/String;)Landroid/icu/text/UCharacterIterator;", True, False), ("([C)Landroid/icu/text/UCharacterIterator;", True, False), ("([CII)Landroid/icu/text/UCharacterIterator;", True, False), ("(Ljava/lang/StringBuffer;)Landroid/icu/text/UCharacterIterator;", True, False), ("(Ljava/text/CharacterIterator;)Landroid/icu/text/UCharacterIterator;", True, False)])
    getCharacterIterator = JavaMethod("()Ljava/text/CharacterIterator;")
    current = JavaMethod("()I")
    currentCodePoint = JavaMethod("()I")
    getLength = JavaMethod("()I")
    getIndex = JavaMethod("()I")
    next = JavaMethod("()I")
    nextCodePoint = JavaMethod("()I")
    previous = JavaMethod("()I")
    previousCodePoint = JavaMethod("()I")
    setIndex = JavaMethod("(I)V")
    setToLimit = JavaMethod("()V")
    setToStart = JavaMethod("()V")
    getText = JavaMultipleMethod([("([CI)I", False, False), ("([C)I", False, False), ("()Ljava/lang/String;", False, False)])
    moveIndex = JavaMethod("(I)I")
    moveCodePointIndex = JavaMethod("(I)I")
    clone = JavaMethod("()Ljava/lang/Object;")