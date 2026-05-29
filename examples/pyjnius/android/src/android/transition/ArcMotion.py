from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ArcMotion"]

class ArcMotion(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/transition/ArcMotion"
    __javaconstructor__ = [("()V", False), ("(Landroid/content/Context;Landroid/util/AttributeSet;)V", False)]
    setMinimumHorizontalAngle = JavaMethod("(F)V")
    getMinimumHorizontalAngle = JavaMethod("()F")
    setMinimumVerticalAngle = JavaMethod("(F)V")
    getMinimumVerticalAngle = JavaMethod("()F")
    setMaximumAngle = JavaMethod("(F)V")
    getMaximumAngle = JavaMethod("()F")
    getPath = JavaMethod("(FFFF)Landroid/graphics/Path;")