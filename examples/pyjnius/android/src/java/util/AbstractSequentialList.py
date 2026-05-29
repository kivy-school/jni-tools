from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["AbstractSequentialList"]

class AbstractSequentialList(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/util/AbstractSequentialList"
    remove = JavaMethod("(I)Ljava/lang/Object;")
    add = JavaMethod("(ILjava/lang/Object;)V")
    get = JavaMethod("(I)Ljava/lang/Object;")
    iterator = JavaMethod("()Ljava/util/Iterator;")
    addAll = JavaMethod("(ILjava/util/Collection;)Z")
    set = JavaMethod("(ILjava/lang/Object;)Ljava/lang/Object;")
    listIterator = JavaMethod("(I)Ljava/util/ListIterator;")