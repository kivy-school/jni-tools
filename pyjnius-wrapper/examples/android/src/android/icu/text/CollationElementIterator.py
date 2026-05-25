from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["CollationElementIterator"]

class CollationElementIterator(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/icu/text/CollationElementIterator"
    IGNORABLE = JavaStaticField("I")
    NULLORDER = JavaStaticField("I")
    primaryOrder = JavaStaticMethod("(I)I")
    secondaryOrder = JavaStaticMethod("(I)I")
    tertiaryOrder = JavaStaticMethod("(I)I")
    getOffset = JavaMethod("()I")
    next = JavaMethod("()I")
    previous = JavaMethod("()I")
    reset = JavaMethod("()V")
    setOffset = JavaMethod("(I)V")
    setText = JavaMultipleMethod([("(Ljava/lang/String;)V", False, False), ("(Landroid/icu/text/UCharacterIterator;)V", False, False), ("(Ljava/text/CharacterIterator;)V", False, False)])
    getMaxExpansion = JavaMethod("(I)I")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")