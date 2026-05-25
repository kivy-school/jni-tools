from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["CharsetDecoder"]

class CharsetDecoder(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/nio/charset/CharsetDecoder"
    __javaconstructor__ = [("(Ljava/nio/charset/Charset;FF)V", False)]
    charset = JavaMethod("()Ljava/nio/charset/Charset;")
    replacement = JavaMethod("()Ljava/lang/String;")
    replaceWith = JavaMethod("(Ljava/lang/String;)Ljava/nio/charset/CharsetDecoder;")
    implReplaceWith = JavaMethod("(Ljava/lang/String;)V")
    malformedInputAction = JavaMethod("()Ljava/nio/charset/CodingErrorAction;")
    onMalformedInput = JavaMethod("(Ljava/nio/charset/CodingErrorAction;)Ljava/nio/charset/CharsetDecoder;")
    implOnMalformedInput = JavaMethod("(Ljava/nio/charset/CodingErrorAction;)V")
    unmappableCharacterAction = JavaMethod("()Ljava/nio/charset/CodingErrorAction;")
    onUnmappableCharacter = JavaMethod("(Ljava/nio/charset/CodingErrorAction;)Ljava/nio/charset/CharsetDecoder;")
    implOnUnmappableCharacter = JavaMethod("(Ljava/nio/charset/CodingErrorAction;)V")
    averageCharsPerByte = JavaMethod("()F")
    maxCharsPerByte = JavaMethod("()F")
    decode = JavaMultipleMethod([("(Ljava/nio/ByteBuffer;Ljava/nio/CharBuffer;Z)Ljava/nio/charset/CoderResult;", False, False), ("(Ljava/nio/ByteBuffer;)Ljava/nio/CharBuffer;", False, False)])
    flush = JavaMethod("(Ljava/nio/CharBuffer;)Ljava/nio/charset/CoderResult;")
    implFlush = JavaMethod("(Ljava/nio/CharBuffer;)Ljava/nio/charset/CoderResult;")
    reset = JavaMethod("()Ljava/nio/charset/CharsetDecoder;")
    implReset = JavaMethod("()V")
    decodeLoop = JavaMethod("(Ljava/nio/ByteBuffer;Ljava/nio/CharBuffer;)Ljava/nio/charset/CoderResult;")
    isAutoDetecting = JavaMethod("()Z")
    isCharsetDetected = JavaMethod("()Z")
    detectedCharset = JavaMethod("()Ljava/nio/charset/Charset;")