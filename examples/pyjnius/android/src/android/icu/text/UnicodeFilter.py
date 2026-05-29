from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["UnicodeFilter"]

class UnicodeFilter(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/icu/text/UnicodeFilter"
    ETHER = JavaStaticField("C")
    U_MATCH = JavaStaticField("I")
    U_MISMATCH = JavaStaticField("I")
    U_PARTIAL_MATCH = JavaStaticField("I")
    matches = JavaMethod("(Landroid/icu/text/Replaceable;[IIZ)I")
    contains = JavaMethod("(I)Z")