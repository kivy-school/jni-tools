from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["CycleInterpolator"]

class CycleInterpolator(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/view/animation/CycleInterpolator"
    __javaconstructor__ = [("(F)V", False), ("(Landroid/content/Context;Landroid/util/AttributeSet;)V", False)]
    getInterpolation = JavaMethod("(F)F")