from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Hashtable"]

class Hashtable(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/util/Hashtable"
    __javaconstructor__ = [("(Ljava/util/Map;)V", False), ("()V", False), ("(I)V", False), ("(IF)V", False)]
    remove = JavaMultipleMethod([("(Ljava/lang/Object;Ljava/lang/Object;)Z", False, False), ("(Ljava/lang/Object;)Ljava/lang/Object;", False, False)])
    size = JavaMethod("()I")
    put = JavaMethod("(Ljava/lang/Object;Ljava/lang/Object;)Ljava/lang/Object;")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    toString = JavaMethod("()Ljava/lang/String;")
    values = JavaMethod("()Ljava/util/Collection;")
    hashCode = JavaMethod("()I")
    clone = JavaMethod("()Ljava/lang/Object;")
    clear = JavaMethod("()V")
    isEmpty = JavaMethod("()Z")
    replace = JavaMultipleMethod([("(Ljava/lang/Object;Ljava/lang/Object;Ljava/lang/Object;)Z", False, False), ("(Ljava/lang/Object;Ljava/lang/Object;)Ljava/lang/Object;", False, False)])
    replaceAll = JavaMethod("(Ljava/util/function/BiFunction;)V")
    get = JavaMethod("(Ljava/lang/Object;)Ljava/lang/Object;")
    contains = JavaMethod("(Ljava/lang/Object;)Z")
    elements = JavaMethod("()Ljava/util/Enumeration;")
    merge = JavaMethod("(Ljava/lang/Object;Ljava/lang/Object;Ljava/util/function/BiFunction;)Ljava/lang/Object;")
    entrySet = JavaMethod("()Ljava/util/Set;")
    putAll = JavaMethod("(Ljava/util/Map;)V")
    putIfAbsent = JavaMethod("(Ljava/lang/Object;Ljava/lang/Object;)Ljava/lang/Object;")
    compute = JavaMethod("(Ljava/lang/Object;Ljava/util/function/BiFunction;)Ljava/lang/Object;")
    computeIfAbsent = JavaMethod("(Ljava/lang/Object;Ljava/util/function/Function;)Ljava/lang/Object;")
    keySet = JavaMethod("()Ljava/util/Set;")
    forEach = JavaMethod("(Ljava/util/function/BiConsumer;)V")
    keys = JavaMethod("()Ljava/util/Enumeration;")
    containsValue = JavaMethod("(Ljava/lang/Object;)Z")
    containsKey = JavaMethod("(Ljava/lang/Object;)Z")
    getOrDefault = JavaMethod("(Ljava/lang/Object;Ljava/lang/Object;)Ljava/lang/Object;")
    computeIfPresent = JavaMethod("(Ljava/lang/Object;Ljava/util/function/BiFunction;)Ljava/lang/Object;")