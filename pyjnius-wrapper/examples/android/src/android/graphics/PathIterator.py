from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["PathIterator"]

class PathIterator(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/graphics/PathIterator"
    VERB_CLOSE = JavaStaticField("I")
    VERB_CONIC = JavaStaticField("I")
    VERB_CUBIC = JavaStaticField("I")
    VERB_DONE = JavaStaticField("I")
    VERB_LINE = JavaStaticField("I")
    VERB_MOVE = JavaStaticField("I")
    VERB_QUAD = JavaStaticField("I")
    next = JavaMultipleMethod([("([FI)I", False, False), ("()Landroid/graphics/PathIterator$Segment;", False, False)])
    hasNext = JavaMethod("()Z")
    peek = JavaMethod("()I")

    class Segment(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/graphics/PathIterator/Segment"
        getVerb = JavaMethod("()I")
        getPoints = JavaMethod("()[F")
        getConicWeight = JavaMethod("()F")