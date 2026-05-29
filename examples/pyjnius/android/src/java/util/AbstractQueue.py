from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["AbstractQueue"]

class AbstractQueue(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/util/AbstractQueue"
    __javaconstructor__ = [("()V", False)]
    add = JavaMethod("(Ljava/lang/Object;)Z")
    remove = JavaMethod("()Ljava/lang/Object;")
    element = JavaMethod("()Ljava/lang/Object;")
    clear = JavaMethod("()V")
    addAll = JavaMethod("(Ljava/util/Collection;)Z")