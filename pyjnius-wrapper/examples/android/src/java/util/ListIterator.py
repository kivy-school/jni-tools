from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ListIterator"]

class ListIterator(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "java/util/ListIterator"
    hasNext = JavaMethod("()Z")
    next = JavaMethod("()Ljava/lang/Object;")
    hasPrevious = JavaMethod("()Z")
    previous = JavaMethod("()Ljava/lang/Object;")
    nextIndex = JavaMethod("()I")
    previousIndex = JavaMethod("()I")
    remove = JavaMethod("()V")
    set = JavaMethod("(Ljava/lang/Object;)V")
    add = JavaMethod("(Ljava/lang/Object;)V")