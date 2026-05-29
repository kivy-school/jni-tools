from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["OSWebView"]

class OSWebView(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/OSWebView"
    __javaconstructor__ = [("(Landroid/content/Context;)V", False)]
    overScrollBy = JavaMethod("(IIIIIIIIZ)Z")
    scrollTo = JavaMethod("(II)V")
    computeScroll = JavaMethod("()V")