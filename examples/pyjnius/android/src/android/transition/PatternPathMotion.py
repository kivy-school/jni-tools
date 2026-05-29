from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["PatternPathMotion"]

class PatternPathMotion(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/transition/PatternPathMotion"
    __javaconstructor__ = [("()V", False), ("(Landroid/content/Context;Landroid/util/AttributeSet;)V", False), ("(Landroid/graphics/Path;)V", False)]
    getPatternPath = JavaMethod("()Landroid/graphics/Path;")
    setPatternPath = JavaMethod("(Landroid/graphics/Path;)V")
    getPath = JavaMethod("(FFFF)Landroid/graphics/Path;")