from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["AutomaticGainControl"]

class AutomaticGainControl(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/media/audiofx/AutomaticGainControl"
    isAvailable = JavaStaticMethod("()Z")
    create = JavaStaticMethod("(I)Landroid/media/audiofx/AutomaticGainControl;")