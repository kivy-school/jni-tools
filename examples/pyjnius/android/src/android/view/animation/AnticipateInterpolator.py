from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["AnticipateInterpolator"]

class AnticipateInterpolator(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/view/animation/AnticipateInterpolator"
    __javaconstructor__ = [("(F)V", False), ("(Landroid/content/Context;Landroid/util/AttributeSet;)V", False), ("()V", False)]
    getInterpolation = JavaMethod("(F)F")