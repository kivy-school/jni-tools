from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Base64"]

class Base64(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/util/Base64"
    getMimeDecoder = JavaStaticMethod("()Ljava/util/Base64$Decoder;")
    getEncoder = JavaStaticMethod("()Ljava/util/Base64$Encoder;")
    getUrlEncoder = JavaStaticMethod("()Ljava/util/Base64$Encoder;")
    getMimeEncoder = JavaMultipleMethod([("(I[B)Ljava/util/Base64$Encoder;", True, False), ("()Ljava/util/Base64$Encoder;", True, False)])
    getDecoder = JavaStaticMethod("()Ljava/util/Base64$Decoder;")
    getUrlDecoder = JavaStaticMethod("()Ljava/util/Base64$Decoder;")

    class Encoder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "java/util/Base64$Encoder"
        wrap = JavaMethod("(Ljava/io/OutputStream;)Ljava/io/OutputStream;")
        encode = JavaMultipleMethod([("(Ljava/nio/ByteBuffer;)Ljava/nio/ByteBuffer;", False, False), ("([B)[B", False, False), ("([B[B)I", False, False)])
        withoutPadding = JavaMethod("()Ljava/util/Base64$Encoder;")
        encodeToString = JavaMethod("([B)Ljava/lang/String;")

    class Decoder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "java/util/Base64$Decoder"
        decode = JavaMultipleMethod([("(Ljava/lang/String;)[B", False, False), ("([B)[B", False, False), ("(Ljava/nio/ByteBuffer;)Ljava/nio/ByteBuffer;", False, False), ("([B[B)I", False, False)])
        wrap = JavaMethod("(Ljava/io/InputStream;)Ljava/io/InputStream;")