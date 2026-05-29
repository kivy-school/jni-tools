from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["AnticipateOvershootInterpolator"]

class AnticipateOvershootInterpolator(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/view/animation/AnticipateOvershootInterpolator"
    __javaconstructor__ = [("(FF)V", False), ("(F)V", False), ("(Landroid/content/Context;Landroid/util/AttributeSet;)V", False), ("()V", False)]
    getInterpolation = JavaMethod("(F)F")