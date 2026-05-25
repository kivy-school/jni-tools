from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["SortedMap"]

class SortedMap(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "java/util/SortedMap"
    comparator = JavaMethod("()Ljava/util/Comparator;")
    subMap = JavaMethod("(Ljava/lang/Object;Ljava/lang/Object;)Ljava/util/SortedMap;")
    headMap = JavaMethod("(Ljava/lang/Object;)Ljava/util/SortedMap;")
    tailMap = JavaMethod("(Ljava/lang/Object;)Ljava/util/SortedMap;")
    firstKey = JavaMethod("()Ljava/lang/Object;")
    lastKey = JavaMethod("()Ljava/lang/Object;")
    keySet = JavaMethod("()Ljava/util/Set;")
    values = JavaMethod("()Ljava/util/Collection;")
    entrySet = JavaMethod("()Ljava/util/Set;")
    putFirst = JavaMethod("(Ljava/lang/Object;Ljava/lang/Object;)Ljava/lang/Object;")
    putLast = JavaMethod("(Ljava/lang/Object;Ljava/lang/Object;)Ljava/lang/Object;")
    reversed = JavaMethod("()Ljava/util/SortedMap;")