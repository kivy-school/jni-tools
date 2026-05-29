from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Picture"]

class Picture(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/graphics/Picture"
    __javaconstructor__ = [("()V", False), ("(Landroid/graphics/Picture;)V", False)]
    draw = JavaMethod("(Landroid/graphics/Canvas;)V")
    getHeight = JavaMethod("()I")
    getWidth = JavaMethod("()I")
    beginRecording = JavaMethod("(II)Landroid/graphics/Canvas;")
    endRecording = JavaMethod("()V")
    requiresHardwareAcceleration = JavaMethod("()Z")