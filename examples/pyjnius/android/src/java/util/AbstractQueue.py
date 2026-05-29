from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["AbstractQueue"]

class AbstractQueue(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/util/AbstractQueue"
    remove = JavaMethod("()Ljava/lang/Object;")
    clear = JavaMethod("()V")
    add = JavaMethod("(Ljava/lang/Object;)Z")
    addAll = JavaMethod("(Ljava/util/Collection;)Z")
    element = JavaMethod("()Ljava/lang/Object;")