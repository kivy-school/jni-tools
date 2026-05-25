from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["LinearGradient"]

class LinearGradient(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/graphics/LinearGradient"
    __javaconstructor__ = [("(FFFF[I[FLandroid/graphics/Shader$TileMode;)V", False), ("(FFFF[J[FLandroid/graphics/Shader$TileMode;)V", False), ("(FFFFIILandroid/graphics/Shader$TileMode;)V", False), ("(FFFFJJLandroid/graphics/Shader$TileMode;)V", False)]