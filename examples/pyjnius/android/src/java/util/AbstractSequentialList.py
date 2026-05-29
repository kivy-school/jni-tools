from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["AbstractSequentialList"]

class AbstractSequentialList(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/util/AbstractSequentialList"
    __javaconstructor__ = [("()V", False)]
    get = JavaMethod("(I)Ljava/lang/Object;")
    set = JavaMethod("(ILjava/lang/Object;)Ljava/lang/Object;")
    add = JavaMethod("(ILjava/lang/Object;)V")
    remove = JavaMethod("(I)Ljava/lang/Object;")
    addAll = JavaMethod("(ILjava/util/Collection;)Z")
    iterator = JavaMethod("()Ljava/util/Iterator;")
    listIterator = JavaMethod("(I)Ljava/util/ListIterator;")