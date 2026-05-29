from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ETC1Util"]

class ETC1Util(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/opengl/ETC1Util"
    __javaconstructor__ = [("()V", False)]
    loadTexture = JavaMultipleMethod([("(IIIIILjava/io/InputStream;)V", True, False), ("(IIIIILandroid/opengl/ETC1Util$ETC1Texture;)V", True, False)])
    isETC1Supported = JavaStaticMethod("()Z")
    createTexture = JavaStaticMethod("(Ljava/io/InputStream;)Landroid/opengl/ETC1Util$ETC1Texture;")
    compressTexture = JavaStaticMethod("(Ljava/nio/Buffer;IIII)Landroid/opengl/ETC1Util$ETC1Texture;")
    writeTexture = JavaStaticMethod("(Landroid/opengl/ETC1Util$ETC1Texture;Ljava/io/OutputStream;)V")

    class ETC1Texture(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/opengl/ETC1Util/ETC1Texture"
        __javaconstructor__ = [("(IILjava/nio/ByteBuffer;)V", False)]
        getWidth = JavaMethod("()I")
        getHeight = JavaMethod("()I")
        getData = JavaMethod("()Ljava/nio/ByteBuffer;")