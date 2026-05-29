from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["RuleBasedCollator"]

class RuleBasedCollator(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/text/RuleBasedCollator"
    __javaconstructor__ = [("(Ljava/lang/String;)V", False)]
    PRIMARY = JavaStaticField("I")
    SECONDARY = JavaStaticField("I")
    TERTIARY = JavaStaticField("I")
    IDENTICAL = JavaStaticField("I")
    NO_DECOMPOSITION = JavaStaticField("I")
    CANONICAL_DECOMPOSITION = JavaStaticField("I")
    FULL_DECOMPOSITION = JavaStaticField("I")
    getCollationElementIterator = JavaMultipleMethod([("(Ljava/lang/String;)Ljava/text/CollationElementIterator;", False, False), ("(Ljava/text/CharacterIterator;)Ljava/text/CollationElementIterator;", False, False)])
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")
    clone = JavaMethod("()Ljava/lang/Object;")
    compare = JavaMethod("(Ljava/lang/String;Ljava/lang/String;)I")
    getCollationKey = JavaMethod("(Ljava/lang/String;)Ljava/text/CollationKey;")
    getRules = JavaMethod("()Ljava/lang/String;")