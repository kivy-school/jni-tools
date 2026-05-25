from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["SpanWatcher"]

class SpanWatcher(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "android/text/SpanWatcher"
    onSpanAdded = JavaMethod("(Landroid/text/Spannable;Ljava/lang/Object;II)V")
    onSpanRemoved = JavaMethod("(Landroid/text/Spannable;Ljava/lang/Object;II)V")
    onSpanChanged = JavaMethod("(Landroid/text/Spannable;Ljava/lang/Object;IIII)V")