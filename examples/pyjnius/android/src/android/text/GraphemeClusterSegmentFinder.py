from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["GraphemeClusterSegmentFinder"]

class GraphemeClusterSegmentFinder(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/text/GraphemeClusterSegmentFinder"
    __javaconstructor__ = [("(Ljava/lang/CharSequence;Landroid/text/TextPaint;)V", False)]
    DONE = JavaStaticField("I")
    nextEndBoundary = JavaMethod("(I)I")
    nextStartBoundary = JavaMethod("(I)I")
    previousEndBoundary = JavaMethod("(I)I")
    previousStartBoundary = JavaMethod("(I)I")