from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["AlteredCharSequence"]

class AlteredCharSequence(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/text/AlteredCharSequence"
    make = JavaStaticMethod("(Ljava/lang/CharSequence;[CII)Landroid/text/AlteredCharSequence;")
    charAt = JavaMethod("(I)C")
    length = JavaMethod("()I")
    subSequence = JavaMethod("(II)Ljava/lang/CharSequence;")
    getChars = JavaMethod("(II[CI)V")
    toString = JavaMethod("()Ljava/lang/String;")