from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["WordSegmentFinder"]

class WordSegmentFinder(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/text/WordSegmentFinder"
    __javaconstructor__ = [("(Ljava/lang/CharSequence;Landroid/icu/util/ULocale;)V", False)]
    DONE = JavaStaticField("I")
    nextEndBoundary = JavaMethod("(I)I")
    nextStartBoundary = JavaMethod("(I)I")
    previousEndBoundary = JavaMethod("(I)I")
    previousStartBoundary = JavaMethod("(I)I")