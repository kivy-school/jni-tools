from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["SequencedCollection"]

class SequencedCollection(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/util/SequencedCollection"
    removeLast = JavaMethod("()Ljava/lang/Object;")
    getFirst = JavaMethod("()Ljava/lang/Object;")
    getLast = JavaMethod("()Ljava/lang/Object;")
    addFirst = JavaMethod("(Ljava/lang/Object;)V")
    addLast = JavaMethod("(Ljava/lang/Object;)V")
    removeFirst = JavaMethod("()Ljava/lang/Object;")
    reversed = JavaMethod("()Ljava/util/SequencedCollection;")