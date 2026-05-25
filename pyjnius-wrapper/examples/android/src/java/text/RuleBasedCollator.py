from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["RuleBasedCollator"]

class RuleBasedCollator(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/text/RuleBasedCollator"
    __javaconstructor__ = [("(Ljava/lang/String;)V", False)]
    getRules = JavaMethod("()Ljava/lang/String;")
    getCollationElementIterator = JavaMultipleMethod([("(Ljava/lang/String;)Ljava/text/CollationElementIterator;", False, False), ("(Ljava/text/CharacterIterator;)Ljava/text/CollationElementIterator;", False, False)])
    compare = JavaMethod("(Ljava/lang/String;Ljava/lang/String;)I")
    getCollationKey = JavaMethod("(Ljava/lang/String;)Ljava/text/CollationKey;")
    clone = JavaMethod("()Ljava/lang/Object;")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")