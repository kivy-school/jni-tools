from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["EnumSet"]

class EnumSet(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/util/EnumSet"
    noneOf = JavaStaticMethod("(Ljava/lang/Class;)Ljava/util/EnumSet;")
    allOf = JavaStaticMethod("(Ljava/lang/Class;)Ljava/util/EnumSet;")
    copyOf = JavaMultipleMethod([("(Ljava/util/EnumSet;)Ljava/util/EnumSet;", True, False), ("(Ljava/util/Collection;)Ljava/util/EnumSet;", True, False)])
    complementOf = JavaStaticMethod("(Ljava/util/EnumSet;)Ljava/util/EnumSet;")
    of = JavaMultipleMethod([("(Ljava/lang/Enum;)Ljava/util/EnumSet;", True, False), ("(Ljava/lang/Enum;Ljava/lang/Enum;)Ljava/util/EnumSet;", True, False), ("(Ljava/lang/Enum;Ljava/lang/Enum;Ljava/lang/Enum;)Ljava/util/EnumSet;", True, False), ("(Ljava/lang/Enum;Ljava/lang/Enum;Ljava/lang/Enum;Ljava/lang/Enum;)Ljava/util/EnumSet;", True, False), ("(Ljava/lang/Enum;Ljava/lang/Enum;Ljava/lang/Enum;Ljava/lang/Enum;Ljava/lang/Enum;)Ljava/util/EnumSet;", True, False), ("(Ljava/lang/Enum;[Ljava/lang/Enum;)Ljava/util/EnumSet;", True, True)])
    range = JavaStaticMethod("(Ljava/lang/Enum;Ljava/lang/Enum;)Ljava/util/EnumSet;")
    clone = JavaMethod("()Ljava/util/EnumSet;")