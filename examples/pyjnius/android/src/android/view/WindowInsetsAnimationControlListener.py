from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["WindowInsetsAnimationControlListener"]

class WindowInsetsAnimationControlListener(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/view/WindowInsetsAnimationControlListener"
    onReady = JavaMethod("(Landroid/view/WindowInsetsAnimationController;I)V")
    onFinished = JavaMethod("(Landroid/view/WindowInsetsAnimationController;)V")
    onCancelled = JavaMethod("(Landroid/view/WindowInsetsAnimationController;)V")