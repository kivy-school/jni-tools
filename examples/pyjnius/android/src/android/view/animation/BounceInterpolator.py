from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["BounceInterpolator"]

class BounceInterpolator(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/view/animation/BounceInterpolator"
    __javaconstructor__ = [("()V", False), ("(Landroid/content/Context;Landroid/util/AttributeSet;)V", False)]
    getInterpolation = JavaMethod("(F)F")