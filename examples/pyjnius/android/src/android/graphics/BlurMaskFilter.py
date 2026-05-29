from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["BlurMaskFilter"]

class BlurMaskFilter(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/graphics/BlurMaskFilter"
    __javaconstructor__ = [("(FLandroid/graphics/BlurMaskFilter$Blur;)V", False)]

    class Blur(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/graphics/BlurMaskFilter$Blur"
        INNER = JavaStaticField("Landroid/graphics/BlurMaskFilter$Blur;")
        NORMAL = JavaStaticField("Landroid/graphics/BlurMaskFilter$Blur;")
        OUTER = JavaStaticField("Landroid/graphics/BlurMaskFilter$Blur;")
        SOLID = JavaStaticField("Landroid/graphics/BlurMaskFilter$Blur;")
        values = JavaStaticMethod("()[Landroid/graphics/BlurMaskFilter$Blur;")
        valueOf = JavaStaticMethod("(Ljava/lang/String;)Landroid/graphics/BlurMaskFilter$Blur;")
        INNER = JavaStaticField("Landroid/graphics/BlurMaskFilter$Blur;")
        NORMAL = JavaStaticField("Landroid/graphics/BlurMaskFilter$Blur;")
        OUTER = JavaStaticField("Landroid/graphics/BlurMaskFilter$Blur;")
        SOLID = JavaStaticField("Landroid/graphics/BlurMaskFilter$Blur;")