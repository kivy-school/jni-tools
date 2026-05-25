from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Charset"]

class Charset(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/nio/charset/Charset"
    __javaconstructor__ = [("(Ljava/lang/String;[Ljava/lang/String;)V", False)]
    isSupported = JavaStaticMethod("(Ljava/lang/String;)Z")
    forName = JavaStaticMethod("(Ljava/lang/String;)Ljava/nio/charset/Charset;")
    availableCharsets = JavaStaticMethod("()Ljava/util/SortedMap;")
    defaultCharset = JavaStaticMethod("()Ljava/nio/charset/Charset;")
    name = JavaMethod("()Ljava/lang/String;")
    aliases = JavaMethod("()Ljava/util/Set;")
    displayName = JavaMultipleMethod([("()Ljava/lang/String;", False, False), ("(Ljava/util/Locale;)Ljava/lang/String;", False, False)])
    isRegistered = JavaMethod("()Z")
    contains = JavaMethod("(Ljava/nio/charset/Charset;)Z")
    newDecoder = JavaMethod("()Ljava/nio/charset/CharsetDecoder;")
    newEncoder = JavaMethod("()Ljava/nio/charset/CharsetEncoder;")
    canEncode = JavaMethod("()Z")
    decode = JavaMethod("(Ljava/nio/ByteBuffer;)Ljava/nio/CharBuffer;")
    encode = JavaMultipleMethod([("(Ljava/nio/CharBuffer;)Ljava/nio/ByteBuffer;", False, False), ("(Ljava/lang/String;)Ljava/nio/ByteBuffer;", False, False)])
    compareTo = JavaMethod("(Ljava/nio/charset/Charset;)I")
    hashCode = JavaMethod("()I")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    toString = JavaMethod("()Ljava/lang/String;")