from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["HashSet"]

class HashSet(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/util/HashSet"
    __javaconstructor__ = [("(I)V", False), ("(IF)V", False), ("(Ljava/util/Collection;)V", False), ("()V", False)]
    remove = JavaMethod("(Ljava/lang/Object;)Z")
    size = JavaMethod("()I")
    clone = JavaMethod("()Ljava/lang/Object;")
    clear = JavaMethod("()V")
    isEmpty = JavaMethod("()Z")
    add = JavaMethod("(Ljava/lang/Object;)Z")
    toArray = JavaMultipleMethod([("([Ljava/lang/Object;)[Ljava/lang/Object;", False, False), ("()[Ljava/lang/Object;", False, False)])
    iterator = JavaMethod("()Ljava/util/Iterator;")
    contains = JavaMethod("(Ljava/lang/Object;)Z")
    spliterator = JavaMethod("()Ljava/util/Spliterator;")
    newHashSet = JavaStaticMethod("(I)Ljava/util/HashSet;")