from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["CopyOnWriteArraySet"]

class CopyOnWriteArraySet(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/util/concurrent/CopyOnWriteArraySet"
    __javaconstructor__ = [("()V", False), ("(Ljava/util/Collection;)V", False)]
    size = JavaMethod("()I")
    isEmpty = JavaMethod("()Z")
    contains = JavaMethod("(Ljava/lang/Object;)Z")
    toArray = JavaMultipleMethod([("()[Ljava/lang/Object;", False, False), ("([Ljava/lang/Object;)[Ljava/lang/Object;", False, False)])
    clear = JavaMethod("()V")
    remove = JavaMethod("(Ljava/lang/Object;)Z")
    add = JavaMethod("(Ljava/lang/Object;)Z")
    containsAll = JavaMethod("(Ljava/util/Collection;)Z")
    addAll = JavaMethod("(Ljava/util/Collection;)Z")
    removeAll = JavaMethod("(Ljava/util/Collection;)Z")
    retainAll = JavaMethod("(Ljava/util/Collection;)Z")
    iterator = JavaMethod("()Ljava/util/Iterator;")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    removeIf = JavaMethod("(Ljava/util/function/Predicate;)Z")
    forEach = JavaMethod("(Ljava/util/function/Consumer;)V")
    spliterator = JavaMethod("()Ljava/util/Spliterator;")