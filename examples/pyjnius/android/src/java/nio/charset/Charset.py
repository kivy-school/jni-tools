from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Charset"]

class Charset(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/nio/charset/Charset"
    name = JavaMethod("()Ljava/lang/String;")
    forName = JavaMultipleMethod([("(Ljava/lang/String;)Ljava/nio/charset/Charset;", True, False), ("(Ljava/lang/String;Ljava/nio/charset/Charset;)Ljava/nio/charset/Charset;", True, False)])
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    toString = JavaMethod("()Ljava/lang/String;")
    hashCode = JavaMethod("()I")
    compareTo = JavaMultipleMethod([("(Ljava/lang/Object;)I", False, False), ("(Ljava/nio/charset/Charset;)I", False, False)])
    decode = JavaMethod("(Ljava/nio/ByteBuffer;)Ljava/nio/CharBuffer;")
    newDecoder = JavaMethod("()Ljava/nio/charset/CharsetDecoder;")
    newEncoder = JavaMethod("()Ljava/nio/charset/CharsetEncoder;")
    encode = JavaMultipleMethod([("(Ljava/nio/CharBuffer;)Ljava/nio/ByteBuffer;", False, False), ("(Ljava/lang/String;)Ljava/nio/ByteBuffer;", False, False)])
    defaultCharset = JavaStaticMethod("()Ljava/nio/charset/Charset;")
    canEncode = JavaMethod("()Z")
    contains = JavaMethod("(Ljava/nio/charset/Charset;)Z")
    isRegistered = JavaMethod("()Z")
    isSupported = JavaStaticMethod("(Ljava/lang/String;)Z")
    aliases = JavaMethod("()Ljava/util/Set;")
    availableCharsets = JavaStaticMethod("()Ljava/util/SortedMap;")
    displayName = JavaMultipleMethod([("()Ljava/lang/String;", False, False), ("(Ljava/util/Locale;)Ljava/lang/String;", False, False)])