from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ArrayMap"]

class ArrayMap(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/util/ArrayMap"
    __javaconstructor__ = [("()V", False), ("(I)V", False), ("(Landroid/util/ArrayMap;)V", False)]
    clear = JavaMethod("()V")
    ensureCapacity = JavaMethod("(I)V")
    containsKey = JavaMethod("(Ljava/lang/Object;)Z")
    indexOfKey = JavaMethod("(Ljava/lang/Object;)I")
    indexOfValue = JavaMethod("(Ljava/lang/Object;)I")
    containsValue = JavaMethod("(Ljava/lang/Object;)Z")
    get = JavaMethod("(Ljava/lang/Object;)Ljava/lang/Object;")
    keyAt = JavaMethod("(I)Ljava/lang/Object;")
    valueAt = JavaMethod("(I)Ljava/lang/Object;")
    setValueAt = JavaMethod("(ILjava/lang/Object;)Ljava/lang/Object;")
    isEmpty = JavaMethod("()Z")
    put = JavaMethod("(Ljava/lang/Object;Ljava/lang/Object;)Ljava/lang/Object;")
    putAll = JavaMultipleMethod([("(Landroid/util/ArrayMap;)V", False, False), ("(Ljava/util/Map;)V", False, False)])
    remove = JavaMethod("(Ljava/lang/Object;)Ljava/lang/Object;")
    removeAt = JavaMethod("(I)Ljava/lang/Object;")
    size = JavaMethod("()I")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")
    toString = JavaMethod("()Ljava/lang/String;")
    containsAll = JavaMethod("(Ljava/util/Collection;)Z")
    forEach = JavaMethod("(Ljava/util/function/BiConsumer;)V")
    removeAll = JavaMethod("(Ljava/util/Collection;)Z")
    replaceAll = JavaMethod("(Ljava/util/function/BiFunction;)V")
    retainAll = JavaMethod("(Ljava/util/Collection;)Z")
    entrySet = JavaMethod("()Ljava/util/Set;")
    keySet = JavaMethod("()Ljava/util/Set;")
    values = JavaMethod("()Ljava/util/Collection;")