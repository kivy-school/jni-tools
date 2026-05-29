from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Collator"]

class Collator(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/text/Collator"
    PRIMARY = JavaStaticField("I")
    SECONDARY = JavaStaticField("I")
    TERTIARY = JavaStaticField("I")
    IDENTICAL = JavaStaticField("I")
    NO_DECOMPOSITION = JavaStaticField("I")
    CANONICAL_DECOMPOSITION = JavaStaticField("I")
    FULL_DECOMPOSITION = JavaStaticField("I")
    getStrength = JavaMethod("()I")
    setDecomposition = JavaMethod("(I)V")
    setStrength = JavaMethod("(I)V")
    equals = JavaMultipleMethod([("(Ljava/lang/Object;)Z", False, False), ("(Ljava/lang/String;Ljava/lang/String;)Z", False, False)])
    hashCode = JavaMethod("()I")
    clone = JavaMethod("()Ljava/lang/Object;")
    compare = JavaMultipleMethod([("(Ljava/lang/String;Ljava/lang/String;)I", False, False), ("(Ljava/lang/Object;Ljava/lang/Object;)I", False, False)])
    getInstance = JavaMultipleMethod([("()Ljava/text/Collator;", True, False), ("(Ljava/util/Locale;)Ljava/text/Collator;", True, False)])
    getAvailableLocales = JavaStaticMethod("()[Ljava/util/Locale;")
    getDecomposition = JavaMethod("()I")
    getCollationKey = JavaMethod("(Ljava/lang/String;)Ljava/text/CollationKey;")