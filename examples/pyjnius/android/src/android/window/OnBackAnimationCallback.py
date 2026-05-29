from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["OnBackAnimationCallback"]

class OnBackAnimationCallback(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "android/window/OnBackAnimationCallback"
    onBackStarted = JavaMethod("(Landroid/window/BackEvent;)V")
    onBackProgressed = JavaMethod("(Landroid/window/BackEvent;)V")
    onBackCancelled = JavaMethod("()V")