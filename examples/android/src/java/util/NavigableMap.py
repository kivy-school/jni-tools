from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["NavigableMap"]

class NavigableMap(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "java/util/NavigableMap"
    lowerEntry = JavaMethod("(Ljava/lang/Object;)Ljava/util/Map$Entry;")
    lowerKey = JavaMethod("(Ljava/lang/Object;)Ljava/lang/Object;")
    floorEntry = JavaMethod("(Ljava/lang/Object;)Ljava/util/Map$Entry;")
    floorKey = JavaMethod("(Ljava/lang/Object;)Ljava/lang/Object;")
    ceilingEntry = JavaMethod("(Ljava/lang/Object;)Ljava/util/Map$Entry;")
    ceilingKey = JavaMethod("(Ljava/lang/Object;)Ljava/lang/Object;")
    higherEntry = JavaMethod("(Ljava/lang/Object;)Ljava/util/Map$Entry;")
    higherKey = JavaMethod("(Ljava/lang/Object;)Ljava/lang/Object;")
    firstEntry = JavaMethod("()Ljava/util/Map$Entry;")
    lastEntry = JavaMethod("()Ljava/util/Map$Entry;")
    pollFirstEntry = JavaMethod("()Ljava/util/Map$Entry;")
    pollLastEntry = JavaMethod("()Ljava/util/Map$Entry;")
    descendingMap = JavaMethod("()Ljava/util/NavigableMap;")
    navigableKeySet = JavaMethod("()Ljava/util/NavigableSet;")
    descendingKeySet = JavaMethod("()Ljava/util/NavigableSet;")
    subMap = JavaMultipleMethod([("(Ljava/lang/Object;ZLjava/lang/Object;Z)Ljava/util/NavigableMap;", False, False), ("(Ljava/lang/Object;Ljava/lang/Object;)Ljava/util/SortedMap;", False, False)])
    headMap = JavaMultipleMethod([("(Ljava/lang/Object;Z)Ljava/util/NavigableMap;", False, False), ("(Ljava/lang/Object;)Ljava/util/SortedMap;", False, False)])
    tailMap = JavaMultipleMethod([("(Ljava/lang/Object;Z)Ljava/util/NavigableMap;", False, False), ("(Ljava/lang/Object;)Ljava/util/SortedMap;", False, False)])
    reversed = JavaMethod("()Ljava/util/NavigableMap;")