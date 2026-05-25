from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["WeakHashMap"]

class WeakHashMap(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/util/WeakHashMap"
    __javaconstructor__ = [("(IF)V", False), ("(I)V", False), ("()V", False), ("(Ljava/util/Map;)V", False)]
    size = JavaMethod("()I")
    isEmpty = JavaMethod("()Z")
    get = JavaMethod("(Ljava/lang/Object;)Ljava/lang/Object;")
    containsKey = JavaMethod("(Ljava/lang/Object;)Z")
    put = JavaMethod("(Ljava/lang/Object;Ljava/lang/Object;)Ljava/lang/Object;")
    putAll = JavaMethod("(Ljava/util/Map;)V")
    remove = JavaMethod("(Ljava/lang/Object;)Ljava/lang/Object;")
    clear = JavaMethod("()V")
    containsValue = JavaMethod("(Ljava/lang/Object;)Z")
    keySet = JavaMethod("()Ljava/util/Set;")
    values = JavaMethod("()Ljava/util/Collection;")
    entrySet = JavaMethod("()Ljava/util/Set;")
    forEach = JavaMethod("(Ljava/util/function/BiConsumer;)V")
    replaceAll = JavaMethod("(Ljava/util/function/BiFunction;)V")