from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["BlendModeColorFilter"]

class BlendModeColorFilter(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/graphics/BlendModeColorFilter"
    __javaconstructor__ = [("(ILandroid/graphics/BlendMode;)V", False)]
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")
    getMode = JavaMethod("()Landroid/graphics/BlendMode;")
    getColor = JavaMethod("()I")