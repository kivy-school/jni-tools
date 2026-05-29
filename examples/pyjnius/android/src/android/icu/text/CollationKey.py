from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["CollationKey"]

class CollationKey(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/icu/text/CollationKey"
    __javaconstructor__ = [("(Ljava/lang/String;[B)V", False)]
    getSourceString = JavaMethod("()Ljava/lang/String;")
    getBound = JavaMethod("(II)Landroid/icu/text/CollationKey;")
    equals = JavaMultipleMethod([("(Ljava/lang/Object;)Z", False, False), ("(Landroid/icu/text/CollationKey;)Z", False, False)])
    hashCode = JavaMethod("()I")
    compareTo = JavaMultipleMethod([("(Ljava/lang/Object;)I", False, False), ("(Landroid/icu/text/CollationKey;)I", False, False)])
    merge = JavaMethod("(Landroid/icu/text/CollationKey;)Landroid/icu/text/CollationKey;")
    toByteArray = JavaMethod("()[B")

    class BoundMode(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/icu/text/CollationKey$BoundMode"
        LOWER = JavaStaticField("I")
        UPPER = JavaStaticField("I")
        UPPER_LONG = JavaStaticField("I")