from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["CoderResult"]

class CoderResult(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/nio/charset/CoderResult"
    OVERFLOW = JavaStaticField("Ljava/nio/charset/CoderResult;")
    UNDERFLOW = JavaStaticField("Ljava/nio/charset/CoderResult;")
    toString = JavaMethod("()Ljava/lang/String;")
    isUnderflow = JavaMethod("()Z")
    isOverflow = JavaMethod("()Z")
    isError = JavaMethod("()Z")
    isMalformed = JavaMethod("()Z")
    isUnmappable = JavaMethod("()Z")
    length = JavaMethod("()I")
    malformedForLength = JavaStaticMethod("(I)Ljava/nio/charset/CoderResult;")
    unmappableForLength = JavaStaticMethod("(I)Ljava/nio/charset/CoderResult;")
    throwException = JavaMethod("()V")