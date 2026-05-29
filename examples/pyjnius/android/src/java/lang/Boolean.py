from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Boolean"]

class Boolean(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/lang/Boolean"
    __javaconstructor__ = [("(Z)V", False), ("(Ljava/lang/String;)V", False)]
    FALSE = JavaStaticField("Ljava/lang/Boolean;")
    TRUE = JavaStaticField("Ljava/lang/Boolean;")
    TYPE = JavaStaticField("Ljava/lang/Class;")
    parseBoolean = JavaStaticMethod("(Ljava/lang/String;)Z")
    booleanValue = JavaMethod("()Z")
    valueOf = JavaMultipleMethod([("(Z)Ljava/lang/Boolean;", True, False), ("(Ljava/lang/String;)Ljava/lang/Boolean;", True, False)])
    toString = JavaMultipleMethod([("(Z)Ljava/lang/String;", True, False), ("()Ljava/lang/String;", False, False)])
    hashCode = JavaMultipleMethod([("()I", False, False), ("(Z)I", True, False)])
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    getBoolean = JavaStaticMethod("(Ljava/lang/String;)Z")
    compareTo = JavaMethod("(Ljava/lang/Boolean;)I")
    compare = JavaStaticMethod("(ZZ)I")
    logicalAnd = JavaStaticMethod("(ZZ)Z")
    logicalOr = JavaStaticMethod("(ZZ)Z")
    logicalXor = JavaStaticMethod("(ZZ)Z")