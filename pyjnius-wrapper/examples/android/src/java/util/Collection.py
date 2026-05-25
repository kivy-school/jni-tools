from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Collection"]

class Collection(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "java/util/Collection"
    size = JavaMethod("()I")
    isEmpty = JavaMethod("()Z")
    contains = JavaMethod("(Ljava/lang/Object;)Z")
    iterator = JavaMethod("()Ljava/util/Iterator;")
    toArray = JavaMultipleMethod([("()[Ljava/lang/Object;", False, False), ("([Ljava/lang/Object;)[Ljava/lang/Object;", False, False), ("(Ljava/util/function/IntFunction;)[Ljava/lang/Object;", False, False)])
    add = JavaMethod("(Ljava/lang/Object;)Z")
    remove = JavaMethod("(Ljava/lang/Object;)Z")
    containsAll = JavaMethod("(Ljava/util/Collection;)Z")
    addAll = JavaMethod("(Ljava/util/Collection;)Z")
    removeAll = JavaMethod("(Ljava/util/Collection;)Z")
    removeIf = JavaMethod("(Ljava/util/function/Predicate;)Z")
    retainAll = JavaMethod("(Ljava/util/Collection;)Z")
    clear = JavaMethod("()V")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")
    spliterator = JavaMethod("()Ljava/util/Spliterator;")
    stream = JavaMethod("()Ljava/util/stream/Stream;")
    parallelStream = JavaMethod("()Ljava/util/stream/Stream;")