from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["AlteredCharSequence"]

class AlteredCharSequence(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/text/AlteredCharSequence"
    length = JavaMethod("()I")
    toString = JavaMethod("()Ljava/lang/String;")
    getChars = JavaMethod("(II[CI)V")
    charAt = JavaMethod("(I)C")
    subSequence = JavaMethod("(II)Ljava/lang/CharSequence;")
    make = JavaStaticMethod("(Ljava/lang/CharSequence;[CII)Landroid/text/AlteredCharSequence;")