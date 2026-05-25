from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Replaceable"]

class Replaceable(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "android/icu/text/Replaceable"
    length = JavaMethod("()I")
    charAt = JavaMethod("(I)C")
    char32At = JavaMethod("(I)I")
    getChars = JavaMethod("(II[CI)V")
    replace = JavaMultipleMethod([("(IILjava/lang/String;)V", False, False), ("(II[CII)V", False, False)])
    copy = JavaMethod("(III)V")
    hasMetaData = JavaMethod("()Z")