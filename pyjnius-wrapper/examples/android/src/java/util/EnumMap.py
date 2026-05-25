from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["EnumMap"]

class EnumMap(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/util/EnumMap"
    __javaconstructor__ = [("(Ljava/lang/Class;)V", False), ("(Ljava/util/EnumMap;)V", False), ("(Ljava/util/Map;)V", False)]
    size = JavaMethod("()I")
    containsValue = JavaMethod("(Ljava/lang/Object;)Z")
    containsKey = JavaMethod("(Ljava/lang/Object;)Z")
    get = JavaMethod("(Ljava/lang/Object;)Ljava/lang/Object;")
    put = JavaMethod("(Ljava/lang/Enum;Ljava/lang/Object;)Ljava/lang/Object;")
    remove = JavaMethod("(Ljava/lang/Object;)Ljava/lang/Object;")
    putAll = JavaMethod("(Ljava/util/Map;)V")
    clear = JavaMethod("()V")
    keySet = JavaMethod("()Ljava/util/Set;")
    values = JavaMethod("()Ljava/util/Collection;")
    entrySet = JavaMethod("()Ljava/util/Set;")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")
    clone = JavaMethod("()Ljava/util/EnumMap;")