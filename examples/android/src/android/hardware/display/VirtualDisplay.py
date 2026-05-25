from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["VirtualDisplay"]

class VirtualDisplay(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/hardware/display/VirtualDisplay"
    getDisplay = JavaMethod("()Landroid/view/Display;")
    getSurface = JavaMethod("()Landroid/view/Surface;")
    setSurface = JavaMethod("(Landroid/view/Surface;)V")
    resize = JavaMethod("(III)V")
    release = JavaMethod("()V")
    toString = JavaMethod("()Ljava/lang/String;")

    class Callback(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/hardware/display/VirtualDisplay/Callback"
        __javaconstructor__ = [("()V", False)]
        onPaused = JavaMethod("()V")
        onResumed = JavaMethod("()V")
        onStopped = JavaMethod("()V")