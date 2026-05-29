from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ArrayMap"]

class ArrayMap(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/util/ArrayMap"
    __javaconstructor__ = [("(I)V", False), ("(Landroid/util/ArrayMap;)V", False), ("()V", False)]
    remove = JavaMethod("(Ljava/lang/Object;)Ljava/lang/Object;")
    size = JavaMethod("()I")
    put = JavaMethod("(Ljava/lang/Object;Ljava/lang/Object;)Ljava/lang/Object;")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    toString = JavaMethod("()Ljava/lang/String;")
    values = JavaMethod("()Ljava/util/Collection;")
    hashCode = JavaMethod("()I")
    clear = JavaMethod("()V")
    isEmpty = JavaMethod("()Z")
    replaceAll = JavaMethod("(Ljava/util/function/BiFunction;)V")
    get = JavaMethod("(Ljava/lang/Object;)Ljava/lang/Object;")
    entrySet = JavaMethod("()Ljava/util/Set;")
    putAll = JavaMultipleMethod([("(Landroid/util/ArrayMap;)V", False, False), ("(Ljava/util/Map;)V", False, False)])
    keySet = JavaMethod("()Ljava/util/Set;")
    forEach = JavaMethod("(Ljava/util/function/BiConsumer;)V")
    containsValue = JavaMethod("(Ljava/lang/Object;)Z")
    containsKey = JavaMethod("(Ljava/lang/Object;)Z")
    ensureCapacity = JavaMethod("(I)V")
    setValueAt = JavaMethod("(ILjava/lang/Object;)Ljava/lang/Object;")
    keyAt = JavaMethod("(I)Ljava/lang/Object;")
    valueAt = JavaMethod("(I)Ljava/lang/Object;")
    indexOfKey = JavaMethod("(Ljava/lang/Object;)I")
    removeAt = JavaMethod("(I)Ljava/lang/Object;")
    indexOfValue = JavaMethod("(Ljava/lang/Object;)I")
    removeAll = JavaMethod("(Ljava/util/Collection;)Z")
    retainAll = JavaMethod("(Ljava/util/Collection;)Z")
    containsAll = JavaMethod("(Ljava/util/Collection;)Z")