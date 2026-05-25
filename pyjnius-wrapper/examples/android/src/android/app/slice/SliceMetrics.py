from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["SliceMetrics"]

class SliceMetrics(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/app/slice/SliceMetrics"
    __javaconstructor__ = [("(Landroid/content/Context;Landroid/net/Uri;)V", False)]
    logVisible = JavaMethod("()V")
    logHidden = JavaMethod("()V")
    logTouch = JavaMethod("(ILandroid/net/Uri;)V")