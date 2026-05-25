from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Picture"]

class Picture(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/graphics/Picture"
    __javaconstructor__ = [("()V", False), ("(Landroid/graphics/Picture;)V", False)]
    finalize = JavaMethod("()V")
    beginRecording = JavaMethod("(II)Landroid/graphics/Canvas;")
    endRecording = JavaMethod("()V")
    getWidth = JavaMethod("()I")
    getHeight = JavaMethod("()I")
    requiresHardwareAcceleration = JavaMethod("()Z")
    draw = JavaMethod("(Landroid/graphics/Canvas;)V")