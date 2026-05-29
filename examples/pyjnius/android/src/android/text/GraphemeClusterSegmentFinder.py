from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["GraphemeClusterSegmentFinder"]

class GraphemeClusterSegmentFinder(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/text/GraphemeClusterSegmentFinder"
    __javaconstructor__ = [("(Ljava/lang/CharSequence;Landroid/text/TextPaint;)V", False)]
    previousStartBoundary = JavaMethod("(I)I")
    previousEndBoundary = JavaMethod("(I)I")
    nextStartBoundary = JavaMethod("(I)I")
    nextEndBoundary = JavaMethod("(I)I")