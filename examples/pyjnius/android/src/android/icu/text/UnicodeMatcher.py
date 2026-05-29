from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["UnicodeMatcher"]

class UnicodeMatcher(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/icu/text/UnicodeMatcher"
    ETHER = JavaStaticField("C")
    U_MATCH = JavaStaticField("I")
    U_MISMATCH = JavaStaticField("I")
    U_PARTIAL_MATCH = JavaStaticField("I")
    toPattern = JavaMethod("(Z)Ljava/lang/String;")
    matchesIndexValue = JavaMethod("(I)Z")
    addMatchSetTo = JavaMethod("(Landroid/icu/text/UnicodeSet;)V")
    matches = JavaMethod("(Landroid/icu/text/Replaceable;[IIZ)I")