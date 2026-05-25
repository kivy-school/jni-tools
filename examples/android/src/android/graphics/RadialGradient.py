from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["RadialGradient"]

class RadialGradient(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/graphics/RadialGradient"
    __javaconstructor__ = [("(FFF[I[FLandroid/graphics/Shader$TileMode;)V", False), ("(FFF[J[FLandroid/graphics/Shader$TileMode;)V", False), ("(FFFFFF[J[FLandroid/graphics/Shader$TileMode;)V", False), ("(FFFIILandroid/graphics/Shader$TileMode;)V", False), ("(FFFJJLandroid/graphics/Shader$TileMode;)V", False)]