from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["CharacterIterator"]

class CharacterIterator(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "java/text/CharacterIterator"
    DONE = JavaStaticField("C")
    first = JavaMethod("()C")
    last = JavaMethod("()C")
    current = JavaMethod("()C")
    next = JavaMethod("()C")
    previous = JavaMethod("()C")
    setIndex = JavaMethod("(I)C")
    getBeginIndex = JavaMethod("()I")
    getEndIndex = JavaMethod("()I")
    getIndex = JavaMethod("()I")
    clone = JavaMethod("()Ljava/lang/Object;")