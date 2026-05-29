from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

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
    hasNext = JavaMethod("()Z")
    next = JavaMultipleMethod([("([FI)I", False, False), ("()Ljava/lang/Object;", False, False), ("()Landroid/graphics/PathIterator$Segment;", False, False)])
    peek = JavaMethod("()I")

    class Segment(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/graphics/PathIterator$Segment"
        getVerb = JavaMethod("()I")
        getConicWeight = JavaMethod("()F")
        getPoints = JavaMethod("()[F")