from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["StringCharacterIterator"]

class StringCharacterIterator(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/text/StringCharacterIterator"
    __javaconstructor__ = [("(Ljava/lang/String;)V", False), ("(Ljava/lang/String;I)V", False), ("(Ljava/lang/String;III)V", False)]
    setText = JavaMethod("(Ljava/lang/String;)V")
    first = JavaMethod("()C")
    last = JavaMethod("()C")
    setIndex = JavaMethod("(I)C")
    current = JavaMethod("()C")
    next = JavaMethod("()C")
    previous = JavaMethod("()C")
    getBeginIndex = JavaMethod("()I")
    getEndIndex = JavaMethod("()I")
    getIndex = JavaMethod("()I")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")
    clone = JavaMethod("()Ljava/lang/Object;")