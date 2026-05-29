from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["CharsetEncoder"]

class CharsetEncoder(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/nio/charset/CharsetEncoder"
    reset = JavaMethod("()Ljava/nio/charset/CharsetEncoder;")
    onMalformedInput = JavaMethod("(Ljava/nio/charset/CodingErrorAction;)Ljava/nio/charset/CharsetEncoder;")
    onUnmappableCharacter = JavaMethod("(Ljava/nio/charset/CodingErrorAction;)Ljava/nio/charset/CharsetEncoder;")
    maxBytesPerChar = JavaMethod("()F")
    encode = JavaMultipleMethod([("(Ljava/nio/CharBuffer;Ljava/nio/ByteBuffer;Z)Ljava/nio/charset/CoderResult;", False, False), ("(Ljava/nio/CharBuffer;)Ljava/nio/ByteBuffer;", False, False)])
    flush = JavaMethod("(Ljava/nio/ByteBuffer;)Ljava/nio/charset/CoderResult;")
    canEncode = JavaMultipleMethod([("(Ljava/lang/CharSequence;)Z", False, False), ("(C)Z", False, False)])
    charset = JavaMethod("()Ljava/nio/charset/Charset;")
    replacement = JavaMethod("()[B")
    isLegalReplacement = JavaMethod("([B)Z")
    malformedInputAction = JavaMethod("()Ljava/nio/charset/CodingErrorAction;")
    unmappableCharacterAction = JavaMethod("()Ljava/nio/charset/CodingErrorAction;")
    averageBytesPerChar = JavaMethod("()F")
    replaceWith = JavaMethod("([B)Ljava/nio/charset/CharsetEncoder;")