from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Boolean"]

class Boolean(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/lang/Boolean"
    __javaconstructor__ = [("(Z)V", False), ("(Ljava/lang/String;)V", False)]
    TRUE = JavaStaticField("Ljava/lang/Boolean;")
    FALSE = JavaStaticField("Ljava/lang/Boolean;")
    TYPE = JavaStaticField("Ljava/lang/Class;")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    toString = JavaMultipleMethod([("()Ljava/lang/String;", False, False), ("(Z)Ljava/lang/String;", True, False)])
    hashCode = JavaMultipleMethod([("()I", False, False), ("(Z)I", True, False)])
    compareTo = JavaMultipleMethod([("(Ljava/lang/Boolean;)I", False, False), ("(Ljava/lang/Object;)I", False, False)])
    getBoolean = JavaStaticMethod("(Ljava/lang/String;)Z")
    compare = JavaStaticMethod("(ZZ)I")
    booleanValue = JavaMethod("()Z")
    valueOf = JavaMultipleMethod([("(Ljava/lang/String;)Ljava/lang/Boolean;", True, False), ("(Z)Ljava/lang/Boolean;", True, False)])
    describeConstable = JavaMethod("()Ljava/util/Optional;")
    parseBoolean = JavaStaticMethod("(Ljava/lang/String;)Z")
    logicalAnd = JavaStaticMethod("(ZZ)Z")
    logicalOr = JavaStaticMethod("(ZZ)Z")
    logicalXor = JavaStaticMethod("(ZZ)Z")