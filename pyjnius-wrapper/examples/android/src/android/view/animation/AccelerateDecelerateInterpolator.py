from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["AccelerateDecelerateInterpolator"]

class AccelerateDecelerateInterpolator(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/view/animation/AccelerateDecelerateInterpolator"
    __javaconstructor__ = [("()V", False), ("(Landroid/content/Context;Landroid/util/AttributeSet;)V", False)]
    getInterpolation = JavaMethod("(F)F")