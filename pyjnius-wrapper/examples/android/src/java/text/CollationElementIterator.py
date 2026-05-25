from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["CollationElementIterator"]

class CollationElementIterator(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/text/CollationElementIterator"
    NULLORDER = JavaStaticField("I")
    reset = JavaMethod("()V")
    next = JavaMethod("()I")
    previous = JavaMethod("()I")
    primaryOrder = JavaStaticMethod("(I)I")
    secondaryOrder = JavaStaticMethod("(I)S")
    tertiaryOrder = JavaStaticMethod("(I)S")
    setOffset = JavaMethod("(I)V")
    getOffset = JavaMethod("()I")
    getMaxExpansion = JavaMethod("(I)I")
    setText = JavaMultipleMethod([("(Ljava/lang/String;)V", False, False), ("(Ljava/text/CharacterIterator;)V", False, False)])