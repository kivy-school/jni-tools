from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["HapticGenerator"]

class HapticGenerator(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/media/audiofx/HapticGenerator"
    isAvailable = JavaStaticMethod("()Z")
    create = JavaStaticMethod("(I)Landroid/media/audiofx/HapticGenerator;")
    setEnabled = JavaMethod("(Z)I")
    release = JavaMethod("()V")
    close = JavaMethod("()V")