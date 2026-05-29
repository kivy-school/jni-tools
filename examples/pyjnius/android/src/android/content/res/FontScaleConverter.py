from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["FontScaleConverter"]

class FontScaleConverter(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/content/res/FontScaleConverter"
    convertDpToSp = JavaMethod("(F)F")
    convertSpToDp = JavaMethod("(F)F")
    forScale = JavaStaticMethod("(F)Landroid/content/res/FontScaleConverter;")
    isNonLinearFontScalingActive = JavaStaticMethod("(F)Z")