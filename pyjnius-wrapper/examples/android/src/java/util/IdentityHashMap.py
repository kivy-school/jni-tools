from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["IdentityHashMap"]

class IdentityHashMap(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/util/IdentityHashMap"
    __javaconstructor__ = [("()V", False), ("(I)V", False), ("(Ljava/util/Map;)V", False)]
    size = JavaMethod("()I")
    isEmpty = JavaMethod("()Z")
    get = JavaMethod("(Ljava/lang/Object;)Ljava/lang/Object;")
    containsKey = JavaMethod("(Ljava/lang/Object;)Z")
    containsValue = JavaMethod("(Ljava/lang/Object;)Z")
    put = JavaMethod("(Ljava/lang/Object;Ljava/lang/Object;)Ljava/lang/Object;")
    putAll = JavaMethod("(Ljava/util/Map;)V")
    remove = JavaMethod("(Ljava/lang/Object;)Ljava/lang/Object;")
    clear = JavaMethod("()V")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")
    clone = JavaMethod("()Ljava/lang/Object;")
    keySet = JavaMethod("()Ljava/util/Set;")
    values = JavaMethod("()Ljava/util/Collection;")
    entrySet = JavaMethod("()Ljava/util/Set;")
    forEach = JavaMethod("(Ljava/util/function/BiConsumer;)V")
    replaceAll = JavaMethod("(Ljava/util/function/BiFunction;)V")