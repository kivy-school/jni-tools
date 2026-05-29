from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["AbstractCollection"]

class AbstractCollection(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/util/AbstractCollection"
    remove = JavaMethod("(Ljava/lang/Object;)Z")
    size = JavaMethod("()I")
    toString = JavaMethod("()Ljava/lang/String;")
    clear = JavaMethod("()V")
    isEmpty = JavaMethod("()Z")
    add = JavaMethod("(Ljava/lang/Object;)Z")
    toArray = JavaMultipleMethod([("([Ljava/lang/Object;)[Ljava/lang/Object;", False, False), ("()[Ljava/lang/Object;", False, False)])
    iterator = JavaMethod("()Ljava/util/Iterator;")
    contains = JavaMethod("(Ljava/lang/Object;)Z")
    addAll = JavaMethod("(Ljava/util/Collection;)Z")
    removeAll = JavaMethod("(Ljava/util/Collection;)Z")
    retainAll = JavaMethod("(Ljava/util/Collection;)Z")
    containsAll = JavaMethod("(Ljava/util/Collection;)Z")