from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Map"]

class Map(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "java/util/Map"
    size = JavaMethod("()I")
    isEmpty = JavaMethod("()Z")
    containsKey = JavaMethod("(Ljava/lang/Object;)Z")
    containsValue = JavaMethod("(Ljava/lang/Object;)Z")
    get = JavaMethod("(Ljava/lang/Object;)Ljava/lang/Object;")
    put = JavaMethod("(Ljava/lang/Object;Ljava/lang/Object;)Ljava/lang/Object;")
    remove = JavaMultipleMethod([("(Ljava/lang/Object;)Ljava/lang/Object;", False, False), ("(Ljava/lang/Object;Ljava/lang/Object;)Z", False, False)])
    putAll = JavaMethod("(Ljava/util/Map;)V")
    clear = JavaMethod("()V")
    keySet = JavaMethod("()Ljava/util/Set;")
    values = JavaMethod("()Ljava/util/Collection;")
    entrySet = JavaMethod("()Ljava/util/Set;")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")
    getOrDefault = JavaMethod("(Ljava/lang/Object;Ljava/lang/Object;)Ljava/lang/Object;")
    forEach = JavaMethod("(Ljava/util/function/BiConsumer;)V")
    replaceAll = JavaMethod("(Ljava/util/function/BiFunction;)V")
    putIfAbsent = JavaMethod("(Ljava/lang/Object;Ljava/lang/Object;)Ljava/lang/Object;")
    replace = JavaMultipleMethod([("(Ljava/lang/Object;Ljava/lang/Object;Ljava/lang/Object;)Z", False, False), ("(Ljava/lang/Object;Ljava/lang/Object;)Ljava/lang/Object;", False, False)])
    computeIfAbsent = JavaMethod("(Ljava/lang/Object;Ljava/util/function/Function;)Ljava/lang/Object;")
    computeIfPresent = JavaMethod("(Ljava/lang/Object;Ljava/util/function/BiFunction;)Ljava/lang/Object;")
    compute = JavaMethod("(Ljava/lang/Object;Ljava/util/function/BiFunction;)Ljava/lang/Object;")
    merge = JavaMethod("(Ljava/lang/Object;Ljava/lang/Object;Ljava/util/function/BiFunction;)Ljava/lang/Object;")
    of = JavaMultipleMethod([("()Ljava/util/Map;", True, False), ("(Ljava/lang/Object;Ljava/lang/Object;)Ljava/util/Map;", True, False), ("(Ljava/lang/Object;Ljava/lang/Object;Ljava/lang/Object;Ljava/lang/Object;)Ljava/util/Map;", True, False), ("(Ljava/lang/Object;Ljava/lang/Object;Ljava/lang/Object;Ljava/lang/Object;Ljava/lang/Object;Ljava/lang/Object;)Ljava/util/Map;", True, False), ("(Ljava/lang/Object;Ljava/lang/Object;Ljava/lang/Object;Ljava/lang/Object;Ljava/lang/Object;Ljava/lang/Object;Ljava/lang/Object;Ljava/lang/Object;)Ljava/util/Map;", True, False), ("(Ljava/lang/Object;Ljava/lang/Object;Ljava/lang/Object;Ljava/lang/Object;Ljava/lang/Object;Ljava/lang/Object;Ljava/lang/Object;Ljava/lang/Object;Ljava/lang/Object;Ljava/lang/Object;)Ljava/util/Map;", True, False), ("(Ljava/lang/Object;Ljava/lang/Object;Ljava/lang/Object;Ljava/lang/Object;Ljava/lang/Object;Ljava/lang/Object;Ljava/lang/Object;Ljava/lang/Object;Ljava/lang/Object;Ljava/lang/Object;Ljava/lang/Object;Ljava/lang/Object;)Ljava/util/Map;", True, False), ("(Ljava/lang/Object;Ljava/lang/Object;Ljava/lang/Object;Ljava/lang/Object;Ljava/lang/Object;Ljava/lang/Object;Ljava/lang/Object;Ljava/lang/Object;Ljava/lang/Object;Ljava/lang/Object;Ljava/lang/Object;Ljava/lang/Object;Ljava/lang/Object;Ljava/lang/Object;)Ljava/util/Map;", True, False), ("(Ljava/lang/Object;Ljava/lang/Object;Ljava/lang/Object;Ljava/lang/Object;Ljava/lang/Object;Ljava/lang/Object;Ljava/lang/Object;Ljava/lang/Object;Ljava/lang/Object;Ljava/lang/Object;Ljava/lang/Object;Ljava/lang/Object;Ljava/lang/Object;Ljava/lang/Object;Ljava/lang/Object;Ljava/lang/Object;)Ljava/util/Map;", True, False), ("(Ljava/lang/Object;Ljava/lang/Object;Ljava/lang/Object;Ljava/lang/Object;Ljava/lang/Object;Ljava/lang/Object;Ljava/lang/Object;Ljava/lang/Object;Ljava/lang/Object;Ljava/lang/Object;Ljava/lang/Object;Ljava/lang/Object;Ljava/lang/Object;Ljava/lang/Object;Ljava/lang/Object;Ljava/lang/Object;Ljava/lang/Object;Ljava/lang/Object;)Ljava/util/Map;", True, False), ("(Ljava/lang/Object;Ljava/lang/Object;Ljava/lang/Object;Ljava/lang/Object;Ljava/lang/Object;Ljava/lang/Object;Ljava/lang/Object;Ljava/lang/Object;Ljava/lang/Object;Ljava/lang/Object;Ljava/lang/Object;Ljava/lang/Object;Ljava/lang/Object;Ljava/lang/Object;Ljava/lang/Object;Ljava/lang/Object;Ljava/lang/Object;Ljava/lang/Object;Ljava/lang/Object;Ljava/lang/Object;)Ljava/util/Map;", True, False)])
    ofEntries = JavaStaticMethod("([Ljava/util/Map$Entry;)Ljava/util/Map;", varargs=True)
    entry = JavaStaticMethod("(Ljava/lang/Object;Ljava/lang/Object;)Ljava/util/Map$Entry;")
    copyOf = JavaStaticMethod("(Ljava/util/Map;)Ljava/util/Map;")

    class Entry(JavaInterface, metaclass=MetaJavaClass):
        __javaclass__ = "java/util/Map/Entry"
        getKey = JavaMethod("()Ljava/lang/Object;")
        getValue = JavaMethod("()Ljava/lang/Object;")
        setValue = JavaMethod("(Ljava/lang/Object;)Ljava/lang/Object;")
        equals = JavaMethod("(Ljava/lang/Object;)Z")
        hashCode = JavaMethod("()I")
        comparingByKey = JavaMultipleMethod([("()Ljava/util/Comparator;", True, False), ("(Ljava/util/Comparator;)Ljava/util/Comparator;", True, False)])
        comparingByValue = JavaMultipleMethod([("()Ljava/util/Comparator;", True, False), ("(Ljava/util/Comparator;)Ljava/util/Comparator;", True, False)])
        copyOf = JavaStaticMethod("(Ljava/util/Map$Entry;)Ljava/util/Map$Entry;")