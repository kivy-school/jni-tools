from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["LinkedHashMap"]

class LinkedHashMap(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/util/LinkedHashMap"
    __javaconstructor__ = [("(IF)V", False), ("(I)V", False), ("()V", False), ("(Ljava/util/Map;)V", False), ("(IFZ)V", False)]
    putFirst = JavaMethod("(Ljava/lang/Object;Ljava/lang/Object;)Ljava/lang/Object;")
    putLast = JavaMethod("(Ljava/lang/Object;Ljava/lang/Object;)Ljava/lang/Object;")
    containsValue = JavaMethod("(Ljava/lang/Object;)Z")
    get = JavaMethod("(Ljava/lang/Object;)Ljava/lang/Object;")
    getOrDefault = JavaMethod("(Ljava/lang/Object;Ljava/lang/Object;)Ljava/lang/Object;")
    clear = JavaMethod("()V")
    removeEldestEntry = JavaMethod("(Ljava/util/Map$Entry;)Z")
    keySet = JavaMethod("()Ljava/util/Set;")
    sequencedKeySet = JavaMethod("()Ljava/util/SequencedSet;")
    values = JavaMethod("()Ljava/util/Collection;")
    sequencedValues = JavaMethod("()Ljava/util/SequencedCollection;")
    entrySet = JavaMethod("()Ljava/util/Set;")
    sequencedEntrySet = JavaMethod("()Ljava/util/SequencedSet;")
    forEach = JavaMethod("(Ljava/util/function/BiConsumer;)V")
    replaceAll = JavaMethod("(Ljava/util/function/BiFunction;)V")
    newLinkedHashMap = JavaStaticMethod("(I)Ljava/util/LinkedHashMap;")
    reversed = JavaMethod("()Ljava/util/SequencedMap;")