from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["AssetManager"]

class AssetManager(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/content/res/AssetManager"
    ACCESS_BUFFER = JavaStaticField("I")
    ACCESS_RANDOM = JavaStaticField("I")
    ACCESS_STREAMING = JavaStaticField("I")
    ACCESS_UNKNOWN = JavaStaticField("I")
    close = JavaMethod("()V")
    open = JavaMultipleMethod([("(Ljava/lang/String;)Ljava/io/InputStream;", False, False), ("(Ljava/lang/String;I)Ljava/io/InputStream;", False, False)])
    openFd = JavaMethod("(Ljava/lang/String;)Landroid/content/res/AssetFileDescriptor;")
    list = JavaMethod("(Ljava/lang/String;)[Ljava/lang/String;")
    openNonAssetFd = JavaMultipleMethod([("(Ljava/lang/String;)Landroid/content/res/AssetFileDescriptor;", False, False), ("(ILjava/lang/String;)Landroid/content/res/AssetFileDescriptor;", False, False)])
    openXmlResourceParser = JavaMultipleMethod([("(Ljava/lang/String;)Landroid/content/res/XmlResourceParser;", False, False), ("(ILjava/lang/String;)Landroid/content/res/XmlResourceParser;", False, False)])
    finalize = JavaMethod("()V")
    getLocales = JavaMethod("()[Ljava/lang/String;")

    class AssetInputStream(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/content/res/AssetManager/AssetInputStream"
        read = JavaMultipleMethod([("()I", False, False), ("([B)I", False, False), ("([BII)I", False, False)])
        skip = JavaMethod("(J)J")
        available = JavaMethod("()I")
        markSupported = JavaMethod("()Z")
        mark = JavaMethod("(I)V")
        reset = JavaMethod("()V")
        close = JavaMethod("()V")
        finalize = JavaMethod("()V")