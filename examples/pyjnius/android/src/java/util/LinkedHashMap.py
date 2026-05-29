from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["LinkedHashMap"]

class LinkedHashMap(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/util/LinkedHashMap"
    __javaconstructor__ = [("(Ljava/util/Map;)V", False), ("(I)V", False), ("(IF)V", False), ("(IFZ)V", False), ("()V", False)]
    values = JavaMethod("()Ljava/util/Collection;")
    clear = JavaMethod("()V")
    replaceAll = JavaMethod("(Ljava/util/function/BiFunction;)V")
    get = JavaMethod("(Ljava/lang/Object;)Ljava/lang/Object;")
    entrySet = JavaMethod("()Ljava/util/Set;")
    newLinkedHashMap = JavaStaticMethod("(I)Ljava/util/LinkedHashMap;")
    keySet = JavaMethod("()Ljava/util/Set;")
    forEach = JavaMethod("(Ljava/util/function/BiConsumer;)V")
    containsValue = JavaMethod("(Ljava/lang/Object;)Z")
    getOrDefault = JavaMethod("(Ljava/lang/Object;Ljava/lang/Object;)Ljava/lang/Object;")
    sequencedKeySet = JavaMethod("()Ljava/util/SequencedSet;")
    sequencedValues = JavaMethod("()Ljava/util/SequencedCollection;")
    sequencedEntrySet = JavaMethod("()Ljava/util/SequencedSet;")
    putFirst = JavaMethod("(Ljava/lang/Object;Ljava/lang/Object;)Ljava/lang/Object;")
    putLast = JavaMethod("(Ljava/lang/Object;Ljava/lang/Object;)Ljava/lang/Object;")
    reversed = JavaMethod("()Ljava/util/SequencedMap;")