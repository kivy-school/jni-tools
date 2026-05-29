from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["IDN"]

class IDN(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/net/IDN"
    ALLOW_UNASSIGNED = JavaStaticField("I")
    USE_STD3_ASCII_RULES = JavaStaticField("I")
    toASCII = JavaMultipleMethod([("(Ljava/lang/String;)Ljava/lang/String;", True, False), ("(Ljava/lang/String;I)Ljava/lang/String;", True, False)])
    toUnicode = JavaMultipleMethod([("(Ljava/lang/String;)Ljava/lang/String;", True, False), ("(Ljava/lang/String;I)Ljava/lang/String;", True, False)])