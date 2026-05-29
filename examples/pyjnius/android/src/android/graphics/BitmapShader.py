from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["BitmapShader"]

class BitmapShader(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/graphics/BitmapShader"
    __javaconstructor__ = [("(Landroid/graphics/Bitmap;Landroid/graphics/Shader$TileMode;Landroid/graphics/Shader$TileMode;)V", False)]
    FILTER_MODE_DEFAULT = JavaStaticField("I")
    FILTER_MODE_LINEAR = JavaStaticField("I")
    FILTER_MODE_NEAREST = JavaStaticField("I")
    setFilterMode = JavaMethod("(I)V")
    setMaxAnisotropy = JavaMethod("(I)V")
    setOverrideGainmap = JavaMethod("(Landroid/graphics/Gainmap;)V")
    getFilterMode = JavaMethod("()I")
    getMaxAnisotropy = JavaMethod("()I")