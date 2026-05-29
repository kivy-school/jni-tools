from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["CycleInterpolator"]

class CycleInterpolator(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/view/animation/CycleInterpolator"
    __javaconstructor__ = [("(Landroid/content/Context;Landroid/util/AttributeSet;)V", False), ("(F)V", False)]
    getInterpolation = JavaMethod("(F)F")