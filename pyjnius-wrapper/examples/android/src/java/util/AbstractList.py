from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["AbstractList"]

class AbstractList(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/util/AbstractList"
    __javaconstructor__ = [("()V", False)]
    modCount = JavaField("I")
    add = JavaMultipleMethod([("(Ljava/lang/Object;)Z", False, False), ("(ILjava/lang/Object;)V", False, False)])
    get = JavaMethod("(I)Ljava/lang/Object;")
    set = JavaMethod("(ILjava/lang/Object;)Ljava/lang/Object;")
    remove = JavaMethod("(I)Ljava/lang/Object;")
    indexOf = JavaMethod("(Ljava/lang/Object;)I")
    lastIndexOf = JavaMethod("(Ljava/lang/Object;)I")
    clear = JavaMethod("()V")
    addAll = JavaMethod("(ILjava/util/Collection;)Z")
    iterator = JavaMethod("()Ljava/util/Iterator;")
    listIterator = JavaMultipleMethod([("()Ljava/util/ListIterator;", False, False), ("(I)Ljava/util/ListIterator;", False, False)])
    subList = JavaMethod("(II)Ljava/util/List;")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")
    removeRange = JavaMethod("(II)V")