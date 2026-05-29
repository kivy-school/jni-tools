from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["TextDirectionHeuristics"]

class TextDirectionHeuristics(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/text/TextDirectionHeuristics"
    __javaconstructor__ = [("()V", False)]
    ANYRTL_LTR = JavaStaticField("Landroid/text/TextDirectionHeuristic;")
    FIRSTSTRONG_LTR = JavaStaticField("Landroid/text/TextDirectionHeuristic;")
    FIRSTSTRONG_RTL = JavaStaticField("Landroid/text/TextDirectionHeuristic;")
    LOCALE = JavaStaticField("Landroid/text/TextDirectionHeuristic;")
    LTR = JavaStaticField("Landroid/text/TextDirectionHeuristic;")
    RTL = JavaStaticField("Landroid/text/TextDirectionHeuristic;")