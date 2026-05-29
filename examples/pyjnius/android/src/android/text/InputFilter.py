from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["InputFilter"]

class InputFilter(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/text/InputFilter"
    filter = JavaMethod("(Ljava/lang/CharSequence;IILandroid/text/Spanned;II)Ljava/lang/CharSequence;")

    class LengthFilter(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/text/InputFilter$LengthFilter"
        __javaconstructor__ = [("(I)V", False)]
        filter = JavaMethod("(Ljava/lang/CharSequence;IILandroid/text/Spanned;II)Ljava/lang/CharSequence;")
        getMax = JavaMethod("()I")

    class AllCaps(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/text/InputFilter$AllCaps"
        __javaconstructor__ = [("()V", False), ("(Ljava/util/Locale;)V", False)]
        filter = JavaMethod("(Ljava/lang/CharSequence;IILandroid/text/Spanned;II)Ljava/lang/CharSequence;")