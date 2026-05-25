from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["PathInterpolator"]

class PathInterpolator(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/view/animation/PathInterpolator"
    __javaconstructor__ = [("(Landroid/graphics/Path;)V", False), ("(FF)V", False), ("(FFFF)V", False), ("(Landroid/content/Context;Landroid/util/AttributeSet;)V", False)]
    getInterpolation = JavaMethod("(F)F")