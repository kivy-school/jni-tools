from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["HashSet"]

class HashSet(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/util/HashSet"
    __javaconstructor__ = [("()V", False), ("(Ljava/util/Collection;)V", False), ("(IF)V", False), ("(I)V", False)]
    iterator = JavaMethod("()Ljava/util/Iterator;")
    size = JavaMethod("()I")
    isEmpty = JavaMethod("()Z")
    contains = JavaMethod("(Ljava/lang/Object;)Z")
    add = JavaMethod("(Ljava/lang/Object;)Z")
    remove = JavaMethod("(Ljava/lang/Object;)Z")
    clear = JavaMethod("()V")
    clone = JavaMethod("()Ljava/lang/Object;")
    spliterator = JavaMethod("()Ljava/util/Spliterator;")
    toArray = JavaMultipleMethod([("()[Ljava/lang/Object;", False, False), ("([Ljava/lang/Object;)[Ljava/lang/Object;", False, False)])
    newHashSet = JavaStaticMethod("(I)Ljava/util/HashSet;")