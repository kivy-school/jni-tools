from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["AbstractMap"]

class AbstractMap(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/util/AbstractMap"
    remove = JavaMethod("(Ljava/lang/Object;)Ljava/lang/Object;")
    size = JavaMethod("()I")
    put = JavaMethod("(Ljava/lang/Object;Ljava/lang/Object;)Ljava/lang/Object;")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    toString = JavaMethod("()Ljava/lang/String;")
    values = JavaMethod("()Ljava/util/Collection;")
    hashCode = JavaMethod("()I")
    clear = JavaMethod("()V")
    isEmpty = JavaMethod("()Z")
    get = JavaMethod("(Ljava/lang/Object;)Ljava/lang/Object;")
    entrySet = JavaMethod("()Ljava/util/Set;")
    putAll = JavaMethod("(Ljava/util/Map;)V")
    keySet = JavaMethod("()Ljava/util/Set;")
    containsValue = JavaMethod("(Ljava/lang/Object;)Z")
    containsKey = JavaMethod("(Ljava/lang/Object;)Z")

    class SimpleImmutableEntry(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "java/util/AbstractMap$SimpleImmutableEntry"
        __javaconstructor__ = [("(Ljava/lang/Object;Ljava/lang/Object;)V", False), ("(Ljava/util/Map$Entry;)V", False)]
        equals = JavaMethod("(Ljava/lang/Object;)Z")
        toString = JavaMethod("()Ljava/lang/String;")
        hashCode = JavaMethod("()I")
        getValue = JavaMethod("()Ljava/lang/Object;")
        getKey = JavaMethod("()Ljava/lang/Object;")
        setValue = JavaMethod("(Ljava/lang/Object;)Ljava/lang/Object;")

    class SimpleEntry(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "java/util/AbstractMap$SimpleEntry"
        __javaconstructor__ = [("(Ljava/lang/Object;Ljava/lang/Object;)V", False), ("(Ljava/util/Map$Entry;)V", False)]
        equals = JavaMethod("(Ljava/lang/Object;)Z")
        toString = JavaMethod("()Ljava/lang/String;")
        hashCode = JavaMethod("()I")
        getValue = JavaMethod("()Ljava/lang/Object;")
        getKey = JavaMethod("()Ljava/lang/Object;")
        setValue = JavaMethod("(Ljava/lang/Object;)Ljava/lang/Object;")