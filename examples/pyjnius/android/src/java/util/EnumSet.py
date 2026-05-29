from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["EnumSet"]

class EnumSet(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/util/EnumSet"
    clone = JavaMultipleMethod([("()Ljava/util/EnumSet;", False, False), ("()Ljava/lang/Object;", False, False)])
    copyOf = JavaMultipleMethod([("(Ljava/util/EnumSet;)Ljava/util/EnumSet;", True, False), ("(Ljava/util/Collection;)Ljava/util/EnumSet;", True, False)])
    of = JavaMultipleMethod([("(Ljava/lang/Enum;Ljava/lang/Enum;Ljava/lang/Enum;Ljava/lang/Enum;)Ljava/util/EnumSet;", True, False), ("(Ljava/lang/Enum;Ljava/lang/Enum;Ljava/lang/Enum;)Ljava/util/EnumSet;", True, False), ("(Ljava/lang/Enum;[Ljava/lang/Enum;)Ljava/util/EnumSet;", True, True), ("(Ljava/lang/Enum;Ljava/lang/Enum;Ljava/lang/Enum;Ljava/lang/Enum;Ljava/lang/Enum;)Ljava/util/EnumSet;", True, False), ("(Ljava/lang/Enum;)Ljava/util/EnumSet;", True, False), ("(Ljava/lang/Enum;Ljava/lang/Enum;)Ljava/util/EnumSet;", True, False)])
    noneOf = JavaStaticMethod("(Ljava/lang/Class;)Ljava/util/EnumSet;")
    range = JavaStaticMethod("(Ljava/lang/Enum;Ljava/lang/Enum;)Ljava/util/EnumSet;")
    allOf = JavaStaticMethod("(Ljava/lang/Class;)Ljava/util/EnumSet;")
    complementOf = JavaStaticMethod("(Ljava/util/EnumSet;)Ljava/util/EnumSet;")