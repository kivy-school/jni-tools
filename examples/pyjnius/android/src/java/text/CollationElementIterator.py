from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["CollationElementIterator"]

class CollationElementIterator(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/text/CollationElementIterator"
    NULLORDER = JavaStaticField("I")
    reset = JavaMethod("()V")
    next = JavaMethod("()I")
    getOffset = JavaMethod("()I")
    setOffset = JavaMethod("(I)V")
    getMaxExpansion = JavaMethod("(I)I")
    primaryOrder = JavaStaticMethod("(I)I")
    secondaryOrder = JavaStaticMethod("(I)S")
    tertiaryOrder = JavaStaticMethod("(I)S")
    setText = JavaMultipleMethod([("(Ljava/text/CharacterIterator;)V", False, False), ("(Ljava/lang/String;)V", False, False)])
    previous = JavaMethod("()I")