from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["CollationElementIterator"]

class CollationElementIterator(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/icu/text/CollationElementIterator"
    IGNORABLE = JavaStaticField("I")
    NULLORDER = JavaStaticField("I")
    reset = JavaMethod("()V")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")
    next = JavaMethod("()I")
    getOffset = JavaMethod("()I")
    setOffset = JavaMethod("(I)V")
    getMaxExpansion = JavaMethod("(I)I")
    primaryOrder = JavaStaticMethod("(I)I")
    secondaryOrder = JavaStaticMethod("(I)I")
    tertiaryOrder = JavaStaticMethod("(I)I")
    setText = JavaMultipleMethod([("(Landroid/icu/text/UCharacterIterator;)V", False, False), ("(Ljava/lang/String;)V", False, False), ("(Ljava/text/CharacterIterator;)V", False, False)])
    previous = JavaMethod("()I")