from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["OvershootInterpolator"]

class OvershootInterpolator(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/view/animation/OvershootInterpolator"
    __javaconstructor__ = [("()V", False), ("(F)V", False), ("(Landroid/content/Context;Landroid/util/AttributeSet;)V", False)]
    getInterpolation = JavaMethod("(F)F")