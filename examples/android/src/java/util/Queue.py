from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Queue"]

class Queue(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "java/util/Queue"
    add = JavaMethod("(Ljava/lang/Object;)Z")
    offer = JavaMethod("(Ljava/lang/Object;)Z")
    remove = JavaMethod("()Ljava/lang/Object;")
    poll = JavaMethod("()Ljava/lang/Object;")
    element = JavaMethod("()Ljava/lang/Object;")
    peek = JavaMethod("()Ljava/lang/Object;")