from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["TextDirectionHeuristic"]

class TextDirectionHeuristic(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "android/text/TextDirectionHeuristic"
    isRtl = JavaMultipleMethod([("([CII)Z", False, False), ("(Ljava/lang/CharSequence;II)Z", False, False)])