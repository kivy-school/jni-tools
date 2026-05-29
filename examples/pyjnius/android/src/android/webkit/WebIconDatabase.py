from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["WebIconDatabase"]

class WebIconDatabase(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/webkit/WebIconDatabase"
    __javaconstructor__ = [("()V", False)]
    removeAllIcons = JavaMethod("()V")
    releaseIconForPageUrl = JavaMethod("(Ljava/lang/String;)V")
    requestIconForPageUrl = JavaMethod("(Ljava/lang/String;Landroid/webkit/WebIconDatabase$IconListener;)V")
    retainIconForPageUrl = JavaMethod("(Ljava/lang/String;)V")
    getInstance = JavaStaticMethod("()Landroid/webkit/WebIconDatabase;")
    close = JavaMethod("()V")
    open = JavaMethod("(Ljava/lang/String;)V")

    class IconListener(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/webkit/WebIconDatabase$IconListener"
        onReceivedIcon = JavaMethod("(Ljava/lang/String;Landroid/graphics/Bitmap;)V")