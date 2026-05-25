from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["SpannableStringBuilder"]

class SpannableStringBuilder(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/text/SpannableStringBuilder"
    __javaconstructor__ = [("()V", False), ("(Ljava/lang/CharSequence;)V", False), ("(Ljava/lang/CharSequence;II)V", False)]
    valueOf = JavaStaticMethod("(Ljava/lang/CharSequence;)Landroid/text/SpannableStringBuilder;")
    charAt = JavaMethod("(I)C")
    length = JavaMethod("()I")
    insert = JavaMultipleMethod([("(ILjava/lang/CharSequence;II)Landroid/text/SpannableStringBuilder;", False, False), ("(ILjava/lang/CharSequence;)Landroid/text/SpannableStringBuilder;", False, False)])
    delete = JavaMethod("(II)Landroid/text/SpannableStringBuilder;")
    clear = JavaMethod("()V")
    clearSpans = JavaMethod("()V")
    append = JavaMultipleMethod([("(Ljava/lang/CharSequence;)Landroid/text/SpannableStringBuilder;", False, False), ("(Ljava/lang/CharSequence;Ljava/lang/Object;I)Landroid/text/SpannableStringBuilder;", False, False), ("(Ljava/lang/CharSequence;II)Landroid/text/SpannableStringBuilder;", False, False), ("(C)Landroid/text/SpannableStringBuilder;", False, False)])
    replace = JavaMultipleMethod([("(IILjava/lang/CharSequence;)Landroid/text/SpannableStringBuilder;", False, False), ("(IILjava/lang/CharSequence;II)Landroid/text/SpannableStringBuilder;", False, False)])
    setSpan = JavaMethod("(Ljava/lang/Object;III)V")
    removeSpan = JavaMethod("(Ljava/lang/Object;)V")
    getSpanStart = JavaMethod("(Ljava/lang/Object;)I")
    getSpanEnd = JavaMethod("(Ljava/lang/Object;)I")
    getSpanFlags = JavaMethod("(Ljava/lang/Object;)I")
    getSpans = JavaMethod("(IILjava/lang/Class;)[Ljava/lang/Object;")
    nextSpanTransition = JavaMethod("(IILjava/lang/Class;)I")
    subSequence = JavaMethod("(II)Ljava/lang/CharSequence;")
    getChars = JavaMethod("(II[CI)V")
    toString = JavaMethod("()Ljava/lang/String;")
    getTextWatcherDepth = JavaMethod("()I")
    getTextRunCursor = JavaMethod("(IIIIILandroid/graphics/Paint;)I")
    setFilters = JavaMethod("([Landroid/text/InputFilter;)V")
    getFilters = JavaMethod("()[Landroid/text/InputFilter;")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")