from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Animatable"]

class Animatable(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "android/graphics/drawable/Animatable"
    start = JavaMethod("()V")
    stop = JavaMethod("()V")
    isRunning = JavaMethod("()Z")