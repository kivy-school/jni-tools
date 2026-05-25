from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["FontScaleConverter"]

class FontScaleConverter(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "android/content/res/FontScaleConverter"
    convertSpToDp = JavaMethod("(F)F")
    convertDpToSp = JavaMethod("(F)F")
    isNonLinearFontScalingActive = JavaStaticMethod("(F)Z")
    forScale = JavaStaticMethod("(F)Landroid/content/res/FontScaleConverter;")