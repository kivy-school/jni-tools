from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Freezable"]

class Freezable(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "android/icu/util/Freezable"
    isFrozen = JavaMethod("()Z")
    freeze = JavaMethod("()Ljava/lang/Object;")
    cloneAsThawed = JavaMethod("()Ljava/lang/Object;")