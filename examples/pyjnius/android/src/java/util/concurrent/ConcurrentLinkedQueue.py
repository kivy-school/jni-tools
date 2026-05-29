from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ConcurrentLinkedQueue"]

class ConcurrentLinkedQueue(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/util/concurrent/ConcurrentLinkedQueue"
    __javaconstructor__ = [("()V", False), ("(Ljava/util/Collection;)V", False)]
    remove = JavaMethod("(Ljava/lang/Object;)Z")
    size = JavaMethod("()I")
    toString = JavaMethod("()Ljava/lang/String;")
    clear = JavaMethod("()V")
    isEmpty = JavaMethod("()Z")
    add = JavaMethod("(Ljava/lang/Object;)Z")
    toArray = JavaMultipleMethod([("()[Ljava/lang/Object;", False, False), ("([Ljava/lang/Object;)[Ljava/lang/Object;", False, False)])
    iterator = JavaMethod("()Ljava/util/Iterator;")
    contains = JavaMethod("(Ljava/lang/Object;)Z")
    spliterator = JavaMethod("()Ljava/util/Spliterator;")
    addAll = JavaMethod("(Ljava/util/Collection;)Z")
    forEach = JavaMethod("(Ljava/util/function/Consumer;)V")
    offer = JavaMethod("(Ljava/lang/Object;)Z")
    peek = JavaMethod("()Ljava/lang/Object;")
    poll = JavaMethod("()Ljava/lang/Object;")
    removeIf = JavaMethod("(Ljava/util/function/Predicate;)Z")
    removeAll = JavaMethod("(Ljava/util/Collection;)Z")
    retainAll = JavaMethod("(Ljava/util/Collection;)Z")