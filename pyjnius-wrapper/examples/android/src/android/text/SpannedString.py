from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["SpannedString"]

class SpannedString(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/text/SpannedString"
    __javaconstructor__ = [("(Ljava/lang/CharSequence;)V", False)]
    subSequence = JavaMethod("(II)Ljava/lang/CharSequence;")
    valueOf = JavaStaticMethod("(Ljava/lang/CharSequence;)Landroid/text/SpannedString;")
    getSpans = JavaMethod("(IILjava/lang/Class;)[Ljava/lang/Object;")
    getChars = JavaMethod("(II[CI)V")
    hashCode = JavaMethod("()I")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    length = JavaMethod("()I")
    getSpanEnd = JavaMethod("(Ljava/lang/Object;)I")
    toString = JavaMethod("()Ljava/lang/String;")
    getSpanStart = JavaMethod("(Ljava/lang/Object;)I")
    getSpanFlags = JavaMethod("(Ljava/lang/Object;)I")
    charAt = JavaMethod("(I)C")
    nextSpanTransition = JavaMethod("(IILjava/lang/Class;)I")