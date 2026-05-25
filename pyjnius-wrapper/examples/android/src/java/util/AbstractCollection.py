from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["AbstractCollection"]

class AbstractCollection(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/util/AbstractCollection"
    __javaconstructor__ = [("()V", False)]
    iterator = JavaMethod("()Ljava/util/Iterator;")
    size = JavaMethod("()I")
    isEmpty = JavaMethod("()Z")
    contains = JavaMethod("(Ljava/lang/Object;)Z")
    toArray = JavaMultipleMethod([("()[Ljava/lang/Object;", False, False), ("([Ljava/lang/Object;)[Ljava/lang/Object;", False, False)])
    add = JavaMethod("(Ljava/lang/Object;)Z")
    remove = JavaMethod("(Ljava/lang/Object;)Z")
    containsAll = JavaMethod("(Ljava/util/Collection;)Z")
    addAll = JavaMethod("(Ljava/util/Collection;)Z")
    removeAll = JavaMethod("(Ljava/util/Collection;)Z")
    retainAll = JavaMethod("(Ljava/util/Collection;)Z")
    clear = JavaMethod("()V")
    toString = JavaMethod("()Ljava/lang/String;")