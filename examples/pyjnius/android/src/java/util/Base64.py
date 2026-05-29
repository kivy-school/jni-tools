from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Base64"]

class Base64(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/util/Base64"
    getEncoder = JavaStaticMethod("()Ljava/util/Base64$Encoder;")
    getUrlEncoder = JavaStaticMethod("()Ljava/util/Base64$Encoder;")
    getMimeEncoder = JavaMultipleMethod([("()Ljava/util/Base64$Encoder;", True, False), ("(I[B)Ljava/util/Base64$Encoder;", True, False)])
    getDecoder = JavaStaticMethod("()Ljava/util/Base64$Decoder;")
    getUrlDecoder = JavaStaticMethod("()Ljava/util/Base64$Decoder;")
    getMimeDecoder = JavaStaticMethod("()Ljava/util/Base64$Decoder;")

    class Decoder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "java/util/Base64/Decoder"
        decode = JavaMultipleMethod([("([B)[B", False, False), ("(Ljava/lang/String;)[B", False, False), ("([B[B)I", False, False), ("(Ljava/nio/ByteBuffer;)Ljava/nio/ByteBuffer;", False, False)])
        wrap = JavaMethod("(Ljava/io/InputStream;)Ljava/io/InputStream;")

    class Encoder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "java/util/Base64/Encoder"
        encode = JavaMultipleMethod([("([B)[B", False, False), ("([B[B)I", False, False), ("(Ljava/nio/ByteBuffer;)Ljava/nio/ByteBuffer;", False, False)])
        encodeToString = JavaMethod("([B)Ljava/lang/String;")
        wrap = JavaMethod("(Ljava/io/OutputStream;)Ljava/io/OutputStream;")
        withoutPadding = JavaMethod("()Ljava/util/Base64$Encoder;")