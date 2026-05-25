from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ConcurrentNavigableMap"]

class ConcurrentNavigableMap(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "java/util/concurrent/ConcurrentNavigableMap"
    subMap = JavaMultipleMethod([("(Ljava/lang/Object;ZLjava/lang/Object;Z)Ljava/util/concurrent/ConcurrentNavigableMap;", False, False), ("(Ljava/lang/Object;Ljava/lang/Object;)Ljava/util/concurrent/ConcurrentNavigableMap;", False, False)])
    headMap = JavaMultipleMethod([("(Ljava/lang/Object;Z)Ljava/util/concurrent/ConcurrentNavigableMap;", False, False), ("(Ljava/lang/Object;)Ljava/util/concurrent/ConcurrentNavigableMap;", False, False)])
    tailMap = JavaMultipleMethod([("(Ljava/lang/Object;Z)Ljava/util/concurrent/ConcurrentNavigableMap;", False, False), ("(Ljava/lang/Object;)Ljava/util/concurrent/ConcurrentNavigableMap;", False, False)])
    descendingMap = JavaMethod("()Ljava/util/concurrent/ConcurrentNavigableMap;")
    navigableKeySet = JavaMethod("()Ljava/util/NavigableSet;")
    keySet = JavaMethod("()Ljava/util/NavigableSet;")
    descendingKeySet = JavaMethod("()Ljava/util/NavigableSet;")