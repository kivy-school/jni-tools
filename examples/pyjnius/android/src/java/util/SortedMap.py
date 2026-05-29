from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["SortedMap"]

class SortedMap(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/util/SortedMap"
    values = JavaMethod("()Ljava/util/Collection;")
    entrySet = JavaMethod("()Ljava/util/Set;")
    keySet = JavaMethod("()Ljava/util/Set;")
    comparator = JavaMethod("()Ljava/util/Comparator;")
    putFirst = JavaMethod("(Ljava/lang/Object;Ljava/lang/Object;)Ljava/lang/Object;")
    putLast = JavaMethod("(Ljava/lang/Object;Ljava/lang/Object;)Ljava/lang/Object;")
    subMap = JavaMethod("(Ljava/lang/Object;Ljava/lang/Object;)Ljava/util/SortedMap;")
    headMap = JavaMethod("(Ljava/lang/Object;)Ljava/util/SortedMap;")
    tailMap = JavaMethod("(Ljava/lang/Object;)Ljava/util/SortedMap;")
    lastKey = JavaMethod("()Ljava/lang/Object;")
    reversed = JavaMultipleMethod([("()Ljava/util/SortedMap;", False, False), ("()Ljava/util/SequencedMap;", False, False)])
    firstKey = JavaMethod("()Ljava/lang/Object;")