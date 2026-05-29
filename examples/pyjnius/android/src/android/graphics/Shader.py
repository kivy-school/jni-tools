from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Shader"]

class Shader(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/graphics/Shader"
    __javaconstructor__ = [("()V", False)]
    getLocalMatrix = JavaMethod("(Landroid/graphics/Matrix;)Z")
    setLocalMatrix = JavaMethod("(Landroid/graphics/Matrix;)V")

    class TileMode(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/graphics/Shader$TileMode"
        CLAMP = JavaStaticField("Landroid/graphics/Shader$TileMode;")
        DECAL = JavaStaticField("Landroid/graphics/Shader$TileMode;")
        MIRROR = JavaStaticField("Landroid/graphics/Shader$TileMode;")
        REPEAT = JavaStaticField("Landroid/graphics/Shader$TileMode;")
        values = JavaStaticMethod("()[Landroid/graphics/Shader$TileMode;")
        valueOf = JavaStaticMethod("(Ljava/lang/String;)Landroid/graphics/Shader$TileMode;")
        CLAMP = JavaStaticField("Landroid/graphics/Shader$TileMode;")
        DECAL = JavaStaticField("Landroid/graphics/Shader$TileMode;")
        MIRROR = JavaStaticField("Landroid/graphics/Shader$TileMode;")
        REPEAT = JavaStaticField("Landroid/graphics/Shader$TileMode;")