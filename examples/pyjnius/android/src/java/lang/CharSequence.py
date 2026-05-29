from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["CharSequence"]

class CharSequence(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/lang/CharSequence"
    length = JavaMethod("()I")
    toString = JavaMethod("()Ljava/lang/String;")
    getChars = JavaMethod("(II[CI)V")
    compare = JavaStaticMethod("(Ljava/lang/CharSequence;Ljava/lang/CharSequence;)I")
    charAt = JavaMethod("(I)C")
    isEmpty = JavaMethod("()Z")
    codePoints = JavaMethod("()Ljava/util/stream/IntStream;")
    subSequence = JavaMethod("(II)Ljava/lang/CharSequence;")
    chars = JavaMethod("()Ljava/util/stream/IntStream;")