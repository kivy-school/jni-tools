from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Freezable"]

class Freezable(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/icu/util/Freezable"
    cloneAsThawed = JavaMethod("()Ljava/lang/Object;")
    isFrozen = JavaMethod("()Z")
    freeze = JavaMethod("()Ljava/lang/Object;")