from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["SpannableString"]

class SpannableString(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/text/SpannableString"
    __javaconstructor__ = [("(Ljava/lang/CharSequence;)V", False)]
    valueOf = JavaStaticMethod("(Ljava/lang/CharSequence;)Landroid/text/SpannableString;")
    setSpan = JavaMethod("(Ljava/lang/Object;III)V")
    removeSpan = JavaMethod("(Ljava/lang/Object;)V")
    subSequence = JavaMethod("(II)Ljava/lang/CharSequence;")
    getChars = JavaMethod("(II[CI)V")
    length = JavaMethod("()I")
    getSpanStart = JavaMethod("(Ljava/lang/Object;)I")
    getSpanFlags = JavaMethod("(Ljava/lang/Object;)I")
    nextSpanTransition = JavaMethod("(IILjava/lang/Class;)I")
    getSpans = JavaMethod("(IILjava/lang/Class;)[Ljava/lang/Object;")
    hashCode = JavaMethod("()I")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    getSpanEnd = JavaMethod("(Ljava/lang/Object;)I")
    toString = JavaMethod("()Ljava/lang/String;")
    charAt = JavaMethod("(I)C")