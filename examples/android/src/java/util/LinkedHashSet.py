from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["LinkedHashSet"]

class LinkedHashSet(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/util/LinkedHashSet"
    __javaconstructor__ = [("(IF)V", False), ("(I)V", False), ("()V", False), ("(Ljava/util/Collection;)V", False)]
    spliterator = JavaMethod("()Ljava/util/Spliterator;")
    newLinkedHashSet = JavaStaticMethod("(I)Ljava/util/LinkedHashSet;")
    addFirst = JavaMethod("(Ljava/lang/Object;)V")
    addLast = JavaMethod("(Ljava/lang/Object;)V")
    getFirst = JavaMethod("()Ljava/lang/Object;")
    getLast = JavaMethod("()Ljava/lang/Object;")
    removeFirst = JavaMethod("()Ljava/lang/Object;")
    removeLast = JavaMethod("()Ljava/lang/Object;")
    reversed = JavaMethod("()Ljava/util/SequencedSet;")