from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["StringCharacterIterator"]

class StringCharacterIterator(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/text/StringCharacterIterator"
    __javaconstructor__ = [("(Ljava/lang/String;III)V", False), ("(Ljava/lang/String;I)V", False), ("(Ljava/lang/String;)V", False)]
    DONE = JavaStaticField("C")
    getEndIndex = JavaMethod("()I")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")
    clone = JavaMethod("()Ljava/lang/Object;")
    next = JavaMethod("()C")
    last = JavaMethod("()C")
    first = JavaMethod("()C")
    current = JavaMethod("()C")
    setText = JavaMethod("(Ljava/lang/String;)V")
    setIndex = JavaMethod("(I)C")
    getBeginIndex = JavaMethod("()I")
    getIndex = JavaMethod("()I")
    previous = JavaMethod("()C")