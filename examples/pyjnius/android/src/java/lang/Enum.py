from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Enum"]

class Enum(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/lang/Enum"
    name = JavaMethod("()Ljava/lang/String;")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    toString = JavaMethod("()Ljava/lang/String;")
    hashCode = JavaMethod("()I")
    compareTo = JavaMultipleMethod([("(Ljava/lang/Object;)I", False, False), ("(Ljava/lang/Enum;)I", False, False)])
    valueOf = JavaStaticMethod("(Ljava/lang/Class;Ljava/lang/String;)Ljava/lang/Enum;")
    describeConstable = JavaMethod("()Ljava/util/Optional;")
    getDeclaringClass = JavaMethod("()Ljava/lang/Class;")
    ordinal = JavaMethod("()I")

    class EnumDesc(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "java/lang/Enum$EnumDesc"
        toString = JavaMethod("()Ljava/lang/String;")
        of = JavaStaticMethod("(Ljava/lang/constant/ClassDesc;Ljava/lang/String;)Ljava/lang/Enum$EnumDesc;")
        resolveConstantDesc = JavaMultipleMethod([("(Ljava/lang/invoke/MethodHandles$Lookup;)Ljava/lang/Object;", False, False), ("(Ljava/lang/invoke/MethodHandles$Lookup;)Ljava/lang/Enum;", False, False)])