from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["WeakHashMap"]

class WeakHashMap(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/util/WeakHashMap"
    __javaconstructor__ = [("(Ljava/util/Map;)V", False), ("(I)V", False), ("(IF)V", False), ("()V", False)]
    remove = JavaMethod("(Ljava/lang/Object;)Ljava/lang/Object;")
    size = JavaMethod("()I")
    put = JavaMethod("(Ljava/lang/Object;Ljava/lang/Object;)Ljava/lang/Object;")
    values = JavaMethod("()Ljava/util/Collection;")
    clear = JavaMethod("()V")
    isEmpty = JavaMethod("()Z")
    replaceAll = JavaMethod("(Ljava/util/function/BiFunction;)V")
    get = JavaMethod("(Ljava/lang/Object;)Ljava/lang/Object;")
    entrySet = JavaMethod("()Ljava/util/Set;")
    putAll = JavaMethod("(Ljava/util/Map;)V")
    keySet = JavaMethod("()Ljava/util/Set;")
    forEach = JavaMethod("(Ljava/util/function/BiConsumer;)V")
    containsValue = JavaMethod("(Ljava/lang/Object;)Z")
    containsKey = JavaMethod("(Ljava/lang/Object;)Z")
    newWeakHashMap = JavaStaticMethod("(I)Ljava/util/WeakHashMap;")