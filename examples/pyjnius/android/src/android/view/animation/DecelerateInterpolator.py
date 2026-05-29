from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["DecelerateInterpolator"]

class DecelerateInterpolator(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/view/animation/DecelerateInterpolator"
    __javaconstructor__ = [("(F)V", False), ("(Landroid/content/Context;Landroid/util/AttributeSet;)V", False), ("()V", False)]
    getInterpolation = JavaMethod("(F)F")