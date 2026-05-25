from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ConcurrentLinkedQueue"]

class ConcurrentLinkedQueue(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/util/concurrent/ConcurrentLinkedQueue"
    __javaconstructor__ = [("()V", False), ("(Ljava/util/Collection;)V", False)]
    add = JavaMethod("(Ljava/lang/Object;)Z")
    offer = JavaMethod("(Ljava/lang/Object;)Z")
    poll = JavaMethod("()Ljava/lang/Object;")
    peek = JavaMethod("()Ljava/lang/Object;")
    isEmpty = JavaMethod("()Z")
    size = JavaMethod("()I")
    contains = JavaMethod("(Ljava/lang/Object;)Z")
    remove = JavaMethod("(Ljava/lang/Object;)Z")
    addAll = JavaMethod("(Ljava/util/Collection;)Z")
    toString = JavaMethod("()Ljava/lang/String;")
    toArray = JavaMultipleMethod([("()[Ljava/lang/Object;", False, False), ("([Ljava/lang/Object;)[Ljava/lang/Object;", False, False)])
    iterator = JavaMethod("()Ljava/util/Iterator;")
    spliterator = JavaMethod("()Ljava/util/Spliterator;")
    removeIf = JavaMethod("(Ljava/util/function/Predicate;)Z")
    removeAll = JavaMethod("(Ljava/util/Collection;)Z")
    retainAll = JavaMethod("(Ljava/util/Collection;)Z")
    clear = JavaMethod("()V")
    forEach = JavaMethod("(Ljava/util/function/Consumer;)V")