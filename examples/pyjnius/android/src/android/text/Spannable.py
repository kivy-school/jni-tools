from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Spannable"]

class Spannable(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/text/Spannable"
    SPAN_COMPOSING = JavaStaticField("I")
    SPAN_EXCLUSIVE_EXCLUSIVE = JavaStaticField("I")
    SPAN_EXCLUSIVE_INCLUSIVE = JavaStaticField("I")
    SPAN_INCLUSIVE_EXCLUSIVE = JavaStaticField("I")
    SPAN_INCLUSIVE_INCLUSIVE = JavaStaticField("I")
    SPAN_INTERMEDIATE = JavaStaticField("I")
    SPAN_MARK_MARK = JavaStaticField("I")
    SPAN_MARK_POINT = JavaStaticField("I")
    SPAN_PARAGRAPH = JavaStaticField("I")
    SPAN_POINT_MARK = JavaStaticField("I")
    SPAN_POINT_MARK_MASK = JavaStaticField("I")
    SPAN_POINT_POINT = JavaStaticField("I")
    SPAN_PRIORITY = JavaStaticField("I")
    SPAN_PRIORITY_SHIFT = JavaStaticField("I")
    SPAN_USER = JavaStaticField("I")
    SPAN_USER_SHIFT = JavaStaticField("I")
    removeSpan = JavaMethod("(Ljava/lang/Object;)V")
    setSpan = JavaMethod("(Ljava/lang/Object;III)V")

    class Factory(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/text/Spannable$Factory"
        __javaconstructor__ = [("()V", False)]
        getInstance = JavaStaticMethod("()Landroid/text/Spannable$Factory;")
        newSpannable = JavaMethod("(Ljava/lang/CharSequence;)Landroid/text/Spannable;")