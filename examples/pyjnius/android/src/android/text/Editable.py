from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Editable"]

class Editable(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/text/Editable"
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
    append = JavaMultipleMethod([("(Ljava/lang/CharSequence;)Ljava/lang/Appendable;", False, False), ("(Ljava/lang/CharSequence;II)Ljava/lang/Appendable;", False, False), ("(C)Ljava/lang/Appendable;", False, False), ("(Ljava/lang/CharSequence;)Landroid/text/Editable;", False, False), ("(C)Landroid/text/Editable;", False, False), ("(Ljava/lang/CharSequence;II)Landroid/text/Editable;", False, False)])
    insert = JavaMultipleMethod([("(ILjava/lang/CharSequence;II)Landroid/text/Editable;", False, False), ("(ILjava/lang/CharSequence;)Landroid/text/Editable;", False, False)])
    clear = JavaMethod("()V")
    replace = JavaMultipleMethod([("(IILjava/lang/CharSequence;)Landroid/text/Editable;", False, False), ("(IILjava/lang/CharSequence;II)Landroid/text/Editable;", False, False)])
    delete = JavaMethod("(II)Landroid/text/Editable;")
    getFilters = JavaMethod("()[Landroid/text/InputFilter;")
    clearSpans = JavaMethod("()V")
    setFilters = JavaMethod("([Landroid/text/InputFilter;)V")

    class Factory(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/text/Editable$Factory"
        __javaconstructor__ = [("()V", False)]
        getInstance = JavaStaticMethod("()Landroid/text/Editable$Factory;")
        newEditable = JavaMethod("(Ljava/lang/CharSequence;)Landroid/text/Editable;")