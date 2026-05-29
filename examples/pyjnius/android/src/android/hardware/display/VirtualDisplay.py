from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["VirtualDisplay"]

class VirtualDisplay(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/hardware/display/VirtualDisplay"
    toString = JavaMethod("()Ljava/lang/String;")
    release = JavaMethod("()V")
    setRotation = JavaMethod("(I)V")
    setSurface = JavaMethod("(Landroid/view/Surface;)V")
    getSurface = JavaMethod("()Landroid/view/Surface;")
    getDisplay = JavaMethod("()Landroid/view/Display;")
    resize = JavaMethod("(III)V")

    class Callback(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/hardware/display/VirtualDisplay$Callback"
        __javaconstructor__ = [("()V", False)]
        onPaused = JavaMethod("()V")
        onResumed = JavaMethod("()V")
        onStopped = JavaMethod("()V")