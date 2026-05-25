from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["CollationKey"]

class CollationKey(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/icu/text/CollationKey"
    __javaconstructor__ = [("(Ljava/lang/String;[B)V", False)]
    getSourceString = JavaMethod("()Ljava/lang/String;")
    toByteArray = JavaMethod("()[B")
    compareTo = JavaMethod("(Landroid/icu/text/CollationKey;)I")
    equals = JavaMultipleMethod([("(Ljava/lang/Object;)Z", False, False), ("(Landroid/icu/text/CollationKey;)Z", False, False)])
    hashCode = JavaMethod("()I")
    getBound = JavaMethod("(II)Landroid/icu/text/CollationKey;")
    merge = JavaMethod("(Landroid/icu/text/CollationKey;)Landroid/icu/text/CollationKey;")

    class BoundMode(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/icu/text/CollationKey/BoundMode"
        LOWER = JavaStaticField("I")
        UPPER = JavaStaticField("I")
        UPPER_LONG = JavaStaticField("I")