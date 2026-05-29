from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["CharsetDecoder"]

class CharsetDecoder(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/nio/charset/CharsetDecoder"
    reset = JavaMethod("()Ljava/nio/charset/CharsetDecoder;")
    decode = JavaMultipleMethod([("(Ljava/nio/ByteBuffer;Ljava/nio/CharBuffer;Z)Ljava/nio/charset/CoderResult;", False, False), ("(Ljava/nio/ByteBuffer;)Ljava/nio/CharBuffer;", False, False)])
    maxCharsPerByte = JavaMethod("()F")
    onMalformedInput = JavaMethod("(Ljava/nio/charset/CodingErrorAction;)Ljava/nio/charset/CharsetDecoder;")
    onUnmappableCharacter = JavaMethod("(Ljava/nio/charset/CodingErrorAction;)Ljava/nio/charset/CharsetDecoder;")
    flush = JavaMethod("(Ljava/nio/CharBuffer;)Ljava/nio/charset/CoderResult;")
    charset = JavaMethod("()Ljava/nio/charset/Charset;")
    replacement = JavaMethod("()Ljava/lang/String;")
    malformedInputAction = JavaMethod("()Ljava/nio/charset/CodingErrorAction;")
    unmappableCharacterAction = JavaMethod("()Ljava/nio/charset/CodingErrorAction;")
    replaceWith = JavaMethod("(Ljava/lang/String;)Ljava/nio/charset/CharsetDecoder;")
    averageCharsPerByte = JavaMethod("()F")
    isAutoDetecting = JavaMethod("()Z")
    isCharsetDetected = JavaMethod("()Z")
    detectedCharset = JavaMethod("()Ljava/nio/charset/Charset;")