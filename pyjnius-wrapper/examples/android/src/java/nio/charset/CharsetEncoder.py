from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["CharsetEncoder"]

class CharsetEncoder(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/nio/charset/CharsetEncoder"
    __javaconstructor__ = [("(Ljava/nio/charset/Charset;FF[B)V", False), ("(Ljava/nio/charset/Charset;FF)V", False)]
    charset = JavaMethod("()Ljava/nio/charset/Charset;")
    replacement = JavaMethod("()[B")
    replaceWith = JavaMethod("([B)Ljava/nio/charset/CharsetEncoder;")
    implReplaceWith = JavaMethod("([B)V")
    isLegalReplacement = JavaMethod("([B)Z")
    malformedInputAction = JavaMethod("()Ljava/nio/charset/CodingErrorAction;")
    onMalformedInput = JavaMethod("(Ljava/nio/charset/CodingErrorAction;)Ljava/nio/charset/CharsetEncoder;")
    implOnMalformedInput = JavaMethod("(Ljava/nio/charset/CodingErrorAction;)V")
    unmappableCharacterAction = JavaMethod("()Ljava/nio/charset/CodingErrorAction;")
    onUnmappableCharacter = JavaMethod("(Ljava/nio/charset/CodingErrorAction;)Ljava/nio/charset/CharsetEncoder;")
    implOnUnmappableCharacter = JavaMethod("(Ljava/nio/charset/CodingErrorAction;)V")
    averageBytesPerChar = JavaMethod("()F")
    maxBytesPerChar = JavaMethod("()F")
    encode = JavaMultipleMethod([("(Ljava/nio/CharBuffer;Ljava/nio/ByteBuffer;Z)Ljava/nio/charset/CoderResult;", False, False), ("(Ljava/nio/CharBuffer;)Ljava/nio/ByteBuffer;", False, False)])
    flush = JavaMethod("(Ljava/nio/ByteBuffer;)Ljava/nio/charset/CoderResult;")
    implFlush = JavaMethod("(Ljava/nio/ByteBuffer;)Ljava/nio/charset/CoderResult;")
    reset = JavaMethod("()Ljava/nio/charset/CharsetEncoder;")
    implReset = JavaMethod("()V")
    encodeLoop = JavaMethod("(Ljava/nio/CharBuffer;Ljava/nio/ByteBuffer;)Ljava/nio/charset/CoderResult;")
    canEncode = JavaMultipleMethod([("(C)Z", False, False), ("(Ljava/lang/CharSequence;)Z", False, False)])