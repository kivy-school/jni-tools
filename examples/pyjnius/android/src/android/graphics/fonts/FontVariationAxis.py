from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["FontVariationAxis"]

class FontVariationAxis(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/graphics/fonts/FontVariationAxis"
    __javaconstructor__ = [("(Ljava/lang/String;F)V", False)]
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    toString = JavaMethod("()Ljava/lang/String;")
    hashCode = JavaMethod("()I")
    getTag = JavaMethod("()Ljava/lang/String;")
    getStyleValue = JavaMethod("()F")
    toFontVariationSettings = JavaStaticMethod("([Landroid/graphics/fonts/FontVariationAxis;)Ljava/lang/String;")
    fromFontVariationSettings = JavaStaticMethod("(Ljava/lang/String;)[Landroid/graphics/fonts/FontVariationAxis;")