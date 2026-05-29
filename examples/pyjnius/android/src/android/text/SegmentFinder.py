from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["SegmentFinder"]

class SegmentFinder(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/text/SegmentFinder"
    __javaconstructor__ = [("()V", False)]
    DONE = JavaStaticField("I")
    nextEndBoundary = JavaMethod("(I)I")
    nextStartBoundary = JavaMethod("(I)I")
    previousEndBoundary = JavaMethod("(I)I")
    previousStartBoundary = JavaMethod("(I)I")

    class PrescribedSegmentFinder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/text/SegmentFinder$PrescribedSegmentFinder"
        __javaconstructor__ = [("([I)V", False)]
        DONE = JavaStaticField("I")
        nextEndBoundary = JavaMethod("(I)I")
        nextStartBoundary = JavaMethod("(I)I")
        previousEndBoundary = JavaMethod("(I)I")
        previousStartBoundary = JavaMethod("(I)I")