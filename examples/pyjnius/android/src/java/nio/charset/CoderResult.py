from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["CoderResult"]

class CoderResult(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/nio/charset/CoderResult"
    UNDERFLOW = JavaStaticField("Ljava/nio/charset/CoderResult;")
    OVERFLOW = JavaStaticField("Ljava/nio/charset/CoderResult;")
    length = JavaMethod("()I")
    toString = JavaMethod("()Ljava/lang/String;")
    isUnderflow = JavaMethod("()Z")
    throwException = JavaMethod("()V")
    isOverflow = JavaMethod("()Z")
    isError = JavaMethod("()Z")
    malformedForLength = JavaStaticMethod("(I)Ljava/nio/charset/CoderResult;")
    isMalformed = JavaMethod("()Z")
    isUnmappable = JavaMethod("()Z")
    unmappableForLength = JavaStaticMethod("(I)Ljava/nio/charset/CoderResult;")