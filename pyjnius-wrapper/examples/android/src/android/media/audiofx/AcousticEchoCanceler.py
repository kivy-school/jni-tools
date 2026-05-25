from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["AcousticEchoCanceler"]

class AcousticEchoCanceler(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/media/audiofx/AcousticEchoCanceler"
    isAvailable = JavaStaticMethod("()Z")
    create = JavaStaticMethod("(I)Landroid/media/audiofx/AcousticEchoCanceler;")