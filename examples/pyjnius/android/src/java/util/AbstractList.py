from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["AbstractList"]

class AbstractList(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/util/AbstractList"
    remove = JavaMethod("(I)Ljava/lang/Object;")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")
    indexOf = JavaMethod("(Ljava/lang/Object;)I")
    clear = JavaMethod("()V")
    lastIndexOf = JavaMethod("(Ljava/lang/Object;)I")
    add = JavaMultipleMethod([("(ILjava/lang/Object;)V", False, False), ("(Ljava/lang/Object;)Z", False, False)])
    get = JavaMethod("(I)Ljava/lang/Object;")
    subList = JavaMethod("(II)Ljava/util/List;")
    iterator = JavaMethod("()Ljava/util/Iterator;")
    addAll = JavaMethod("(ILjava/util/Collection;)Z")
    set = JavaMethod("(ILjava/lang/Object;)Ljava/lang/Object;")
    listIterator = JavaMultipleMethod([("()Ljava/util/ListIterator;", False, False), ("(I)Ljava/util/ListIterator;", False, False)])