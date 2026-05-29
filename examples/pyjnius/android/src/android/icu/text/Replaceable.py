from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Replaceable"]

class Replaceable(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/icu/text/Replaceable"
    char32At = JavaMethod("(I)I")
    hasMetaData = JavaMethod("()Z")
    length = JavaMethod("()I")
    getChars = JavaMethod("(II[CI)V")
    charAt = JavaMethod("(I)C")
    copy = JavaMethod("(III)V")
    replace = JavaMultipleMethod([("(II[CII)V", False, False), ("(IILjava/lang/String;)V", False, False)])