from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["EnumMap"]

class EnumMap(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/util/EnumMap"
    __javaconstructor__ = [("(Ljava/util/EnumMap;)V", False), ("(Ljava/util/Map;)V", False), ("(Ljava/lang/Class;)V", False)]
    remove = JavaMethod("(Ljava/lang/Object;)Ljava/lang/Object;")
    size = JavaMethod("()I")
    put = JavaMultipleMethod([("(Ljava/lang/Enum;Ljava/lang/Object;)Ljava/lang/Object;", False, False), ("(Ljava/lang/Object;Ljava/lang/Object;)Ljava/lang/Object;", False, False)])
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    values = JavaMethod("()Ljava/util/Collection;")
    hashCode = JavaMethod("()I")
    clone = JavaMultipleMethod([("()Ljava/util/EnumMap;", False, False), ("()Ljava/lang/Object;", False, False)])
    clear = JavaMethod("()V")
    get = JavaMethod("(Ljava/lang/Object;)Ljava/lang/Object;")
    entrySet = JavaMethod("()Ljava/util/Set;")
    putAll = JavaMethod("(Ljava/util/Map;)V")
    keySet = JavaMethod("()Ljava/util/Set;")
    containsValue = JavaMethod("(Ljava/lang/Object;)Z")
    containsKey = JavaMethod("(Ljava/lang/Object;)Z")