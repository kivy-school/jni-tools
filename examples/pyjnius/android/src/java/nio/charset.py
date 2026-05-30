from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

class CodingErrorAction(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/nio/charset/CodingErrorAction"
    IGNORE = JavaStaticField("Ljava/nio/charset/CodingErrorAction;")
    REPLACE = JavaStaticField("Ljava/nio/charset/CodingErrorAction;")
    REPORT = JavaStaticField("Ljava/nio/charset/CodingErrorAction;")
    toString = JavaMethod("()Ljava/lang/String;")

class CharacterCodingException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/nio/charset/CharacterCodingException"
    __javaconstructor__ = [("()V", False)]

class CoderMalfunctionError(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/nio/charset/CoderMalfunctionError"
    __javaconstructor__ = [("(Ljava/lang/Exception;)V", False)]

class CharsetEncoder(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/nio/charset/CharsetEncoder"
    isLegalReplacement = JavaMethod("([B)Z")
    malformedInputAction = JavaMethod("()Ljava/nio/charset/CodingErrorAction;")
    unmappableCharacterAction = JavaMethod("()Ljava/nio/charset/CodingErrorAction;")
    averageBytesPerChar = JavaMethod("()F")
    replaceWith = JavaMethod("([B)Ljava/nio/charset/CharsetEncoder;")
    reset = JavaMethod("()Ljava/nio/charset/CharsetEncoder;")
    onMalformedInput = JavaMethod("(Ljava/nio/charset/CodingErrorAction;)Ljava/nio/charset/CharsetEncoder;")
    onUnmappableCharacter = JavaMethod("(Ljava/nio/charset/CodingErrorAction;)Ljava/nio/charset/CharsetEncoder;")
    maxBytesPerChar = JavaMethod("()F")
    encode = JavaMultipleMethod([("(Ljava/nio/CharBuffer;)Ljava/nio/ByteBuffer;", False, False), ("(Ljava/nio/CharBuffer;Ljava/nio/ByteBuffer;Z)Ljava/nio/charset/CoderResult;", False, False)])
    flush = JavaMethod("(Ljava/nio/ByteBuffer;)Ljava/nio/charset/CoderResult;")
    canEncode = JavaMultipleMethod([("(Ljava/lang/CharSequence;)Z", False, False), ("(C)Z", False, False)])
    charset = JavaMethod("()Ljava/nio/charset/Charset;")
    replacement = JavaMethod("()[B")

class UnsupportedCharsetException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/nio/charset/UnsupportedCharsetException"
    __javaconstructor__ = [("(Ljava/lang/String;)V", False)]
    getCharsetName = JavaMethod("()Ljava/lang/String;")

class IllegalCharsetNameException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/nio/charset/IllegalCharsetNameException"
    __javaconstructor__ = [("(Ljava/lang/String;)V", False)]
    getCharsetName = JavaMethod("()Ljava/lang/String;")

class UnmappableCharacterException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/nio/charset/UnmappableCharacterException"
    __javaconstructor__ = [("(I)V", False)]
    getMessage = JavaMethod("()Ljava/lang/String;")
    getInputLength = JavaMethod("()I")

class CharsetDecoder(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/nio/charset/CharsetDecoder"
    malformedInputAction = JavaMethod("()Ljava/nio/charset/CodingErrorAction;")
    unmappableCharacterAction = JavaMethod("()Ljava/nio/charset/CodingErrorAction;")
    replaceWith = JavaMethod("(Ljava/lang/String;)Ljava/nio/charset/CharsetDecoder;")
    averageCharsPerByte = JavaMethod("()F")
    isAutoDetecting = JavaMethod("()Z")
    isCharsetDetected = JavaMethod("()Z")
    detectedCharset = JavaMethod("()Ljava/nio/charset/Charset;")
    reset = JavaMethod("()Ljava/nio/charset/CharsetDecoder;")
    maxCharsPerByte = JavaMethod("()F")
    onMalformedInput = JavaMethod("(Ljava/nio/charset/CodingErrorAction;)Ljava/nio/charset/CharsetDecoder;")
    onUnmappableCharacter = JavaMethod("(Ljava/nio/charset/CodingErrorAction;)Ljava/nio/charset/CharsetDecoder;")
    decode = JavaMultipleMethod([("(Ljava/nio/ByteBuffer;)Ljava/nio/CharBuffer;", False, False), ("(Ljava/nio/ByteBuffer;Ljava/nio/CharBuffer;Z)Ljava/nio/charset/CoderResult;", False, False)])
    flush = JavaMethod("(Ljava/nio/CharBuffer;)Ljava/nio/charset/CoderResult;")
    charset = JavaMethod("()Ljava/nio/charset/Charset;")
    replacement = JavaMethod("()Ljava/lang/String;")

class Charset(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/nio/charset/Charset"
    name = JavaMethod("()Ljava/lang/String;")
    forName = JavaMultipleMethod([("(Ljava/lang/String;Ljava/nio/charset/Charset;)Ljava/nio/charset/Charset;", True, False), ("(Ljava/lang/String;)Ljava/nio/charset/Charset;", True, False)])
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    toString = JavaMethod("()Ljava/lang/String;")
    hashCode = JavaMethod("()I")
    compareTo = JavaMultipleMethod([("(Ljava/lang/Object;)I", False, False), ("(Ljava/nio/charset/Charset;)I", False, False)])
    newDecoder = JavaMethod("()Ljava/nio/charset/CharsetDecoder;")
    decode = JavaMethod("(Ljava/nio/ByteBuffer;)Ljava/nio/CharBuffer;")
    newEncoder = JavaMethod("()Ljava/nio/charset/CharsetEncoder;")
    encode = JavaMultipleMethod([("(Ljava/nio/CharBuffer;)Ljava/nio/ByteBuffer;", False, False), ("(Ljava/lang/String;)Ljava/nio/ByteBuffer;", False, False)])
    defaultCharset = JavaStaticMethod("()Ljava/nio/charset/Charset;")
    canEncode = JavaMethod("()Z")
    contains = JavaMethod("(Ljava/nio/charset/Charset;)Z")
    isRegistered = JavaMethod("()Z")
    isSupported = JavaStaticMethod("(Ljava/lang/String;)Z")
    aliases = JavaMethod("()Ljava/util/Set;")
    availableCharsets = JavaStaticMethod("()Ljava/util/SortedMap;")
    displayName = JavaMultipleMethod([("(Ljava/util/Locale;)Ljava/lang/String;", False, False), ("()Ljava/lang/String;", False, False)])

class MalformedInputException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/nio/charset/MalformedInputException"
    __javaconstructor__ = [("(I)V", False)]
    getMessage = JavaMethod("()Ljava/lang/String;")
    getInputLength = JavaMethod("()I")

class StandardCharsets(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/nio/charset/StandardCharsets"
    US_ASCII = JavaStaticField("Ljava/nio/charset/Charset;")
    ISO_8859_1 = JavaStaticField("Ljava/nio/charset/Charset;")
    UTF_8 = JavaStaticField("Ljava/nio/charset/Charset;")
    UTF_16BE = JavaStaticField("Ljava/nio/charset/Charset;")
    UTF_16LE = JavaStaticField("Ljava/nio/charset/Charset;")
    UTF_16 = JavaStaticField("Ljava/nio/charset/Charset;")

class CoderResult(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/nio/charset/CoderResult"
    UNDERFLOW = JavaStaticField("Ljava/nio/charset/CoderResult;")
    OVERFLOW = JavaStaticField("Ljava/nio/charset/CoderResult;")
    isOverflow = JavaMethod("()Z")
    isError = JavaMethod("()Z")
    malformedForLength = JavaStaticMethod("(I)Ljava/nio/charset/CoderResult;")
    isMalformed = JavaMethod("()Z")
    isUnmappable = JavaMethod("()Z")
    length = JavaMethod("()I")
    toString = JavaMethod("()Ljava/lang/String;")
    isUnderflow = JavaMethod("()Z")
    throwException = JavaMethod("()V")
    unmappableForLength = JavaStaticMethod("(I)Ljava/nio/charset/CoderResult;")