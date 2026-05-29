from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["SpanWatcher"]

class SpanWatcher(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/text/SpanWatcher"
    onSpanChanged = JavaMethod("(Landroid/text/Spannable;Ljava/lang/Object;IIII)V")
    onSpanRemoved = JavaMethod("(Landroid/text/Spannable;Ljava/lang/Object;II)V")
    onSpanAdded = JavaMethod("(Landroid/text/Spannable;Ljava/lang/Object;II)V")