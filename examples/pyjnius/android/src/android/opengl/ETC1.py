from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ETC1"]

class ETC1(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/opengl/ETC1"
    __javaconstructor__ = [("()V", False)]
    DECODED_BLOCK_SIZE = JavaStaticField("I")
    ENCODED_BLOCK_SIZE = JavaStaticField("I")
    ETC1_RGB8_OES = JavaStaticField("I")
    ETC_PKM_HEADER_SIZE = JavaStaticField("I")
    encodeBlock = JavaStaticMethod("(Ljava/nio/Buffer;ILjava/nio/Buffer;)V")
    decodeBlock = JavaStaticMethod("(Ljava/nio/Buffer;Ljava/nio/Buffer;)V")
    getEncodedDataSize = JavaStaticMethod("(II)I")
    encodeImage = JavaStaticMethod("(Ljava/nio/Buffer;IIIILjava/nio/Buffer;)V")
    decodeImage = JavaStaticMethod("(Ljava/nio/Buffer;Ljava/nio/Buffer;IIII)V")
    formatHeader = JavaStaticMethod("(Ljava/nio/Buffer;II)V")
    isValid = JavaStaticMethod("(Ljava/nio/Buffer;)Z")
    getWidth = JavaStaticMethod("(Ljava/nio/Buffer;)I")
    getHeight = JavaStaticMethod("(Ljava/nio/Buffer;)I")