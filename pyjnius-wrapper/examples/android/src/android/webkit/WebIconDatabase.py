from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["WebIconDatabase"]

class WebIconDatabase(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/webkit/WebIconDatabase"
    __javaconstructor__ = [("()V", False)]
    open = JavaMethod("(Ljava/lang/String;)V")
    close = JavaMethod("()V")
    removeAllIcons = JavaMethod("()V")
    requestIconForPageUrl = JavaMethod("(Ljava/lang/String;Landroid/webkit/WebIconDatabase$IconListener;)V")
    retainIconForPageUrl = JavaMethod("(Ljava/lang/String;)V")
    releaseIconForPageUrl = JavaMethod("(Ljava/lang/String;)V")
    getInstance = JavaStaticMethod("()Landroid/webkit/WebIconDatabase;")

    class IconListener(JavaInterface, metaclass=MetaJavaClass):
        __javaclass__ = "android/webkit/WebIconDatabase/IconListener"
        onReceivedIcon = JavaMethod("(Ljava/lang/String;Landroid/graphics/Bitmap;)V")