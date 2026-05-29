from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["CharacterIterator"]

class CharacterIterator(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/text/CharacterIterator"
    DONE = JavaStaticField("C")
    getEndIndex = JavaMethod("()I")
    clone = JavaMethod("()Ljava/lang/Object;")
    next = JavaMethod("()C")
    last = JavaMethod("()C")
    first = JavaMethod("()C")
    current = JavaMethod("()C")
    setIndex = JavaMethod("(I)C")
    getBeginIndex = JavaMethod("()I")
    getIndex = JavaMethod("()I")
    previous = JavaMethod("()C")