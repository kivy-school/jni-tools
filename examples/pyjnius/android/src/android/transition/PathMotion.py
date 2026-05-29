from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["PathMotion"]

class PathMotion(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/transition/PathMotion"
    __javaconstructor__ = [("()V", False), ("(Landroid/content/Context;Landroid/util/AttributeSet;)V", False)]
    getPath = JavaMethod("(FFFF)Landroid/graphics/Path;")