from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["TextDirectionHeuristic"]

class TextDirectionHeuristic(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/text/TextDirectionHeuristic"
    isRtl = JavaMultipleMethod([("([CII)Z", False, False), ("(Ljava/lang/CharSequence;II)Z", False, False)])