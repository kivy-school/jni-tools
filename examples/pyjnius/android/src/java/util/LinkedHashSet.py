from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["LinkedHashSet"]

class LinkedHashSet(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/util/LinkedHashSet"
    __javaconstructor__ = [("(Ljava/util/Collection;)V", False), ("()V", False), ("(I)V", False), ("(IF)V", False)]
    spliterator = JavaMethod("()Ljava/util/Spliterator;")
    removeLast = JavaMethod("()Ljava/lang/Object;")
    getFirst = JavaMethod("()Ljava/lang/Object;")
    getLast = JavaMethod("()Ljava/lang/Object;")
    addFirst = JavaMethod("(Ljava/lang/Object;)V")
    addLast = JavaMethod("(Ljava/lang/Object;)V")
    removeFirst = JavaMethod("()Ljava/lang/Object;")
    reversed = JavaMultipleMethod([("()Ljava/util/SequencedSet;", False, False), ("()Ljava/util/SequencedCollection;", False, False)])
    newLinkedHashSet = JavaStaticMethod("(I)Ljava/util/LinkedHashSet;")