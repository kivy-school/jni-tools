from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["CharSequence"]

class CharSequence(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "java/lang/CharSequence"
    length = JavaMethod("()I")
    charAt = JavaMethod("(I)C")
    isEmpty = JavaMethod("()Z")
    subSequence = JavaMethod("(II)Ljava/lang/CharSequence;")
    toString = JavaMethod("()Ljava/lang/String;")
    chars = JavaMethod("()Ljava/util/stream/IntStream;")
    codePoints = JavaMethod("()Ljava/util/stream/IntStream;")
    compare = JavaStaticMethod("(Ljava/lang/CharSequence;Ljava/lang/CharSequence;)I")