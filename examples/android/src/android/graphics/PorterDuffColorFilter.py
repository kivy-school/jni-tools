from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["PorterDuffColorFilter"]

class PorterDuffColorFilter(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/graphics/PorterDuffColorFilter"
    __javaconstructor__ = [("(ILandroid/graphics/PorterDuff$Mode;)V", False)]
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")