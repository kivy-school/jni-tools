from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["NoiseSuppressor"]

class NoiseSuppressor(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/media/audiofx/NoiseSuppressor"
    isAvailable = JavaStaticMethod("()Z")
    create = JavaStaticMethod("(I)Landroid/media/audiofx/NoiseSuppressor;")