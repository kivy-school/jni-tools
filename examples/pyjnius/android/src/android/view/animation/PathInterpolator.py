from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["PathInterpolator"]

class PathInterpolator(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/view/animation/PathInterpolator"
    __javaconstructor__ = [("(FFFF)V", False), ("(FF)V", False), ("(Landroid/graphics/Path;)V", False), ("(Landroid/content/Context;Landroid/util/AttributeSet;)V", False)]
    getInterpolation = JavaMethod("(F)F")