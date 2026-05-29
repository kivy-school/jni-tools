from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["OnBackAnimationCallback"]

class OnBackAnimationCallback(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/window/OnBackAnimationCallback"
    onBackStarted = JavaMethod("(Landroid/window/BackEvent;)V")
    onBackCancelled = JavaMethod("()V")
    onBackProgressed = JavaMethod("(Landroid/window/BackEvent;)V")