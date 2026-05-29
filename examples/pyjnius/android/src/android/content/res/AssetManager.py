from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["AssetManager"]

class AssetManager(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/content/res/AssetManager"
    ACCESS_BUFFER = JavaStaticField("I")
    ACCESS_RANDOM = JavaStaticField("I")
    ACCESS_STREAMING = JavaStaticField("I")
    ACCESS_UNKNOWN = JavaStaticField("I")
    openFd = JavaMethod("(Ljava/lang/String;)Landroid/content/res/AssetFileDescriptor;")
    openNonAssetFd = JavaMultipleMethod([("(Ljava/lang/String;)Landroid/content/res/AssetFileDescriptor;", False, False), ("(ILjava/lang/String;)Landroid/content/res/AssetFileDescriptor;", False, False)])
    openXmlResourceParser = JavaMultipleMethod([("(Ljava/lang/String;)Landroid/content/res/XmlResourceParser;", False, False), ("(ILjava/lang/String;)Landroid/content/res/XmlResourceParser;", False, False)])
    list = JavaMethod("(Ljava/lang/String;)[Ljava/lang/String;")
    close = JavaMethod("()V")
    open = JavaMultipleMethod([("(Ljava/lang/String;I)Ljava/io/InputStream;", False, False), ("(Ljava/lang/String;)Ljava/io/InputStream;", False, False)])
    getLocales = JavaMethod("()[Ljava/lang/String;")

    class AssetInputStream(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/content/res/AssetManager$AssetInputStream"
        reset = JavaMethod("()V")
        close = JavaMethod("()V")
        mark = JavaMethod("(I)V")
        read = JavaMultipleMethod([("([BII)I", False, False), ("()I", False, False), ("([B)I", False, False)])
        skip = JavaMethod("(J)J")
        available = JavaMethod("()I")
        markSupported = JavaMethod("()Z")