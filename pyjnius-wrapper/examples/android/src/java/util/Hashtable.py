from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Hashtable"]

class Hashtable(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/util/Hashtable"
    __javaconstructor__ = [("(IF)V", False), ("(I)V", False), ("()V", False), ("(Ljava/util/Map;)V", False)]
    size = JavaMethod("()I")
    isEmpty = JavaMethod("()Z")
    keys = JavaMethod("()Ljava/util/Enumeration;")
    elements = JavaMethod("()Ljava/util/Enumeration;")
    contains = JavaMethod("(Ljava/lang/Object;)Z")
    containsValue = JavaMethod("(Ljava/lang/Object;)Z")
    containsKey = JavaMethod("(Ljava/lang/Object;)Z")
    get = JavaMethod("(Ljava/lang/Object;)Ljava/lang/Object;")
    rehash = JavaMethod("()V")
    put = JavaMethod("(Ljava/lang/Object;Ljava/lang/Object;)Ljava/lang/Object;")
    remove = JavaMultipleMethod([("(Ljava/lang/Object;)Ljava/lang/Object;", False, False), ("(Ljava/lang/Object;Ljava/lang/Object;)Z", False, False)])
    putAll = JavaMethod("(Ljava/util/Map;)V")
    clear = JavaMethod("()V")
    clone = JavaMethod("()Ljava/lang/Object;")
    toString = JavaMethod("()Ljava/lang/String;")
    keySet = JavaMethod("()Ljava/util/Set;")
    entrySet = JavaMethod("()Ljava/util/Set;")
    values = JavaMethod("()Ljava/util/Collection;")
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