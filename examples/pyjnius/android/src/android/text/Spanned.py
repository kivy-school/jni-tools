from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Spanned"]

class Spanned(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/text/Spanned"
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
    getSpanEnd = JavaMethod("(Ljava/lang/Object;)I")
    getSpanFlags = JavaMethod("(Ljava/lang/Object;)I")
    getSpanStart = JavaMethod("(Ljava/lang/Object;)I")
    nextSpanTransition = JavaMethod("(IILjava/lang/Class;)I")
    getSpans = JavaMethod("(IILjava/lang/Class;)[Ljava/lang/Object;")