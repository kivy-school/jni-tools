from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["BlendModeColorFilter"]

class BlendModeColorFilter(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/graphics/BlendModeColorFilter"
    __javaconstructor__ = [("(ILandroid/graphics/BlendMode;)V", False)]
    getColor = JavaMethod("()I")
    getMode = JavaMethod("()Landroid/graphics/BlendMode;")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")