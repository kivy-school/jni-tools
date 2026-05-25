from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["SequencedCollection"]

class SequencedCollection(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "java/util/SequencedCollection"
    reversed = JavaMethod("()Ljava/util/SequencedCollection;")
    addFirst = JavaMethod("(Ljava/lang/Object;)V")
    addLast = JavaMethod("(Ljava/lang/Object;)V")
    getFirst = JavaMethod("()Ljava/lang/Object;")
    getLast = JavaMethod("()Ljava/lang/Object;")
    removeFirst = JavaMethod("()Ljava/lang/Object;")
    removeLast = JavaMethod("()Ljava/lang/Object;")