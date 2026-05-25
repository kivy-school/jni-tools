from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["UnicodeFilter"]

class UnicodeFilter(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/icu/text/UnicodeFilter"
    contains = JavaMethod("(I)Z")
    matches = JavaMethod("(Landroid/icu/text/Replaceable;[IIZ)I")