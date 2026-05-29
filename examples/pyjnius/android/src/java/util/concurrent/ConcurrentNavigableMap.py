from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ConcurrentNavigableMap"]

class ConcurrentNavigableMap(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/util/concurrent/ConcurrentNavigableMap"
    keySet = JavaMultipleMethod([("()Ljava/util/NavigableSet;", False, False), ("()Ljava/util/Set;", False, False)])
    descendingMap = JavaMultipleMethod([("()Ljava/util/NavigableMap;", False, False), ("()Ljava/util/concurrent/ConcurrentNavigableMap;", False, False)])
    navigableKeySet = JavaMethod("()Ljava/util/NavigableSet;")
    subMap = JavaMultipleMethod([("(Ljava/lang/Object;Ljava/lang/Object;)Ljava/util/SortedMap;", False, False), ("(Ljava/lang/Object;ZLjava/lang/Object;Z)Ljava/util/NavigableMap;", False, False), ("(Ljava/lang/Object;ZLjava/lang/Object;Z)Ljava/util/concurrent/ConcurrentNavigableMap;", False, False), ("(Ljava/lang/Object;Ljava/lang/Object;)Ljava/util/concurrent/ConcurrentNavigableMap;", False, False)])
    headMap = JavaMultipleMethod([("(Ljava/lang/Object;Z)Ljava/util/NavigableMap;", False, False), ("(Ljava/lang/Object;)Ljava/util/SortedMap;", False, False), ("(Ljava/lang/Object;)Ljava/util/concurrent/ConcurrentNavigableMap;", False, False), ("(Ljava/lang/Object;Z)Ljava/util/concurrent/ConcurrentNavigableMap;", False, False)])
    tailMap = JavaMultipleMethod([("(Ljava/lang/Object;Z)Ljava/util/NavigableMap;", False, False), ("(Ljava/lang/Object;)Ljava/util/concurrent/ConcurrentNavigableMap;", False, False), ("(Ljava/lang/Object;)Ljava/util/SortedMap;", False, False), ("(Ljava/lang/Object;Z)Ljava/util/concurrent/ConcurrentNavigableMap;", False, False)])
    descendingKeySet = JavaMethod("()Ljava/util/NavigableSet;")