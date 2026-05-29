from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["IdentityHashMap"]

class IdentityHashMap(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/util/IdentityHashMap"
    __javaconstructor__ = [("(Ljava/util/Map;)V", False), ("()V", False), ("(I)V", False)]
    remove = JavaMultipleMethod([("(Ljava/lang/Object;Ljava/lang/Object;)Z", False, False), ("(Ljava/lang/Object;)Ljava/lang/Object;", False, False)])
    size = JavaMethod("()I")
    put = JavaMethod("(Ljava/lang/Object;Ljava/lang/Object;)Ljava/lang/Object;")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    values = JavaMethod("()Ljava/util/Collection;")
    hashCode = JavaMethod("()I")
    clone = JavaMethod("()Ljava/lang/Object;")
    clear = JavaMethod("()V")
    isEmpty = JavaMethod("()Z")
    replace = JavaMethod("(Ljava/lang/Object;Ljava/lang/Object;Ljava/lang/Object;)Z")
    replaceAll = JavaMethod("(Ljava/util/function/BiFunction;)V")
    get = JavaMethod("(Ljava/lang/Object;)Ljava/lang/Object;")
    entrySet = JavaMethod("()Ljava/util/Set;")
    putAll = JavaMethod("(Ljava/util/Map;)V")
    keySet = JavaMethod("()Ljava/util/Set;")
    forEach = JavaMethod("(Ljava/util/function/BiConsumer;)V")
    containsValue = JavaMethod("(Ljava/lang/Object;)Z")
    containsKey = JavaMethod("(Ljava/lang/Object;)Z")