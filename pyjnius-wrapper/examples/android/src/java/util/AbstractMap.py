from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["AbstractMap"]

class AbstractMap(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/util/AbstractMap"
    __javaconstructor__ = [("()V", False)]
    size = JavaMethod("()I")
    isEmpty = JavaMethod("()Z")
    containsValue = JavaMethod("(Ljava/lang/Object;)Z")
    containsKey = JavaMethod("(Ljava/lang/Object;)Z")
    get = JavaMethod("(Ljava/lang/Object;)Ljava/lang/Object;")
    put = JavaMethod("(Ljava/lang/Object;Ljava/lang/Object;)Ljava/lang/Object;")
    remove = JavaMethod("(Ljava/lang/Object;)Ljava/lang/Object;")
    putAll = JavaMethod("(Ljava/util/Map;)V")
    clear = JavaMethod("()V")
    keySet = JavaMethod("()Ljava/util/Set;")
    values = JavaMethod("()Ljava/util/Collection;")
    entrySet = JavaMethod("()Ljava/util/Set;")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")
    toString = JavaMethod("()Ljava/lang/String;")
    clone = JavaMethod("()Ljava/lang/Object;")

    class SimpleEntry(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "java/util/AbstractMap/SimpleEntry"
        __javaconstructor__ = [("(Ljava/lang/Object;Ljava/lang/Object;)V", False), ("(Ljava/util/Map$Entry;)V", False)]
        getKey = JavaMethod("()Ljava/lang/Object;")
        getValue = JavaMethod("()Ljava/lang/Object;")
        setValue = JavaMethod("(Ljava/lang/Object;)Ljava/lang/Object;")
        equals = JavaMethod("(Ljava/lang/Object;)Z")
        hashCode = JavaMethod("()I")
        toString = JavaMethod("()Ljava/lang/String;")

    class SimpleImmutableEntry(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "java/util/AbstractMap/SimpleImmutableEntry"
        __javaconstructor__ = [("(Ljava/lang/Object;Ljava/lang/Object;)V", False), ("(Ljava/util/Map$Entry;)V", False)]
        getKey = JavaMethod("()Ljava/lang/Object;")
        getValue = JavaMethod("()Ljava/lang/Object;")
        setValue = JavaMethod("(Ljava/lang/Object;)Ljava/lang/Object;")
        equals = JavaMethod("(Ljava/lang/Object;)Z")
        hashCode = JavaMethod("()I")
        toString = JavaMethod("()Ljava/lang/String;")