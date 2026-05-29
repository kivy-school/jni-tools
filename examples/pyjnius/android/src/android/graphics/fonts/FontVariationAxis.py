from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["FontVariationAxis"]

class FontVariationAxis(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/graphics/fonts/FontVariationAxis"
    __javaconstructor__ = [("(Ljava/lang/String;F)V", False)]
    getTag = JavaMethod("()Ljava/lang/String;")
    getStyleValue = JavaMethod("()F")
    toString = JavaMethod("()Ljava/lang/String;")
    fromFontVariationSettings = JavaStaticMethod("(Ljava/lang/String;)[Landroid/graphics/fonts/FontVariationAxis;")
    toFontVariationSettings = JavaStaticMethod("([Landroid/graphics/fonts/FontVariationAxis;)Ljava/lang/String;")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")