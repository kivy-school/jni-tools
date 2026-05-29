from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ListIterator"]

class ListIterator(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/util/ListIterator"
    remove = JavaMethod("()V")
    add = JavaMethod("(Ljava/lang/Object;)V")
    hasNext = JavaMethod("()Z")
    next = JavaMethod("()Ljava/lang/Object;")
    set = JavaMethod("(Ljava/lang/Object;)V")
    nextIndex = JavaMethod("()I")
    previousIndex = JavaMethod("()I")
    hasPrevious = JavaMethod("()Z")
    previous = JavaMethod("()Ljava/lang/Object;")