from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["PatternPathMotion"]

class PatternPathMotion(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/transition/PatternPathMotion"
    __javaconstructor__ = [("()V", False), ("(Landroid/graphics/Path;)V", False), ("(Landroid/content/Context;Landroid/util/AttributeSet;)V", False)]
    setPatternPath = JavaMethod("(Landroid/graphics/Path;)V")
    getPatternPath = JavaMethod("()Landroid/graphics/Path;")
    getPath = JavaMethod("(FFFF)Landroid/graphics/Path;")