from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ArcMotion"]

class ArcMotion(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/transition/ArcMotion"
    __javaconstructor__ = [("()V", False), ("(Landroid/content/Context;Landroid/util/AttributeSet;)V", False)]
    getPath = JavaMethod("(FFFF)Landroid/graphics/Path;")
    getMaximumAngle = JavaMethod("()F")
    getMinimumHorizontalAngle = JavaMethod("()F")
    setMaximumAngle = JavaMethod("(F)V")
    getMinimumVerticalAngle = JavaMethod("()F")
    setMinimumHorizontalAngle = JavaMethod("(F)V")
    setMinimumVerticalAngle = JavaMethod("(F)V")