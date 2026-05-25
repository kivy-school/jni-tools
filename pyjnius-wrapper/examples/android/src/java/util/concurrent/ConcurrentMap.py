from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ConcurrentMap"]

class ConcurrentMap(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "java/util/concurrent/ConcurrentMap"
    getOrDefault = JavaMethod("(Ljava/lang/Object;Ljava/lang/Object;)Ljava/lang/Object;")
    forEach = JavaMethod("(Ljava/util/function/BiConsumer;)V")
    putIfAbsent = JavaMethod("(Ljava/lang/Object;Ljava/lang/Object;)Ljava/lang/Object;")
    remove = JavaMethod("(Ljava/lang/Object;Ljava/lang/Object;)Z")
    replace = JavaMultipleMethod([("(Ljava/lang/Object;Ljava/lang/Object;Ljava/lang/Object;)Z", False, False), ("(Ljava/lang/Object;Ljava/lang/Object;)Ljava/lang/Object;", False, False)])
    replaceAll = JavaMethod("(Ljava/util/function/BiFunction;)V")
    computeIfAbsent = JavaMethod("(Ljava/lang/Object;Ljava/util/function/Function;)Ljava/lang/Object;")
    computeIfPresent = JavaMethod("(Ljava/lang/Object;Ljava/util/function/BiFunction;)Ljava/lang/Object;")
    compute = JavaMethod("(Ljava/lang/Object;Ljava/util/function/BiFunction;)Ljava/lang/Object;")
    merge = JavaMethod("(Ljava/lang/Object;Ljava/lang/Object;Ljava/util/function/BiFunction;)Ljava/lang/Object;")