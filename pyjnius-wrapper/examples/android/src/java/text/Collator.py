from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Collator"]

class Collator(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/text/Collator"
    __javaconstructor__ = [("()V", False)]
    CANONICAL_DECOMPOSITION = JavaStaticField("I")
    FULL_DECOMPOSITION = JavaStaticField("I")
    IDENTICAL = JavaStaticField("I")
    NO_DECOMPOSITION = JavaStaticField("I")
    PRIMARY = JavaStaticField("I")
    SECONDARY = JavaStaticField("I")
    TERTIARY = JavaStaticField("I")
    getInstance = JavaMultipleMethod([("()Ljava/text/Collator;", True, False), ("(Ljava/util/Locale;)Ljava/text/Collator;", True, False)])
    compare = JavaMultipleMethod([("(Ljava/lang/String;Ljava/lang/String;)I", False, False), ("(Ljava/lang/Object;Ljava/lang/Object;)I", False, False)])
    getCollationKey = JavaMethod("(Ljava/lang/String;)Ljava/text/CollationKey;")
    equals = JavaMultipleMethod([("(Ljava/lang/String;Ljava/lang/String;)Z", False, False), ("(Ljava/lang/Object;)Z", False, False)])
    getStrength = JavaMethod("()I")
    setStrength = JavaMethod("(I)V")
    getDecomposition = JavaMethod("()I")
    setDecomposition = JavaMethod("(I)V")
    getAvailableLocales = JavaStaticMethod("()[Ljava/util/Locale;")
    clone = JavaMethod("()Ljava/lang/Object;")
    hashCode = JavaMethod("()I")