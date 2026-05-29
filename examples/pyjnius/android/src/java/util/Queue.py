from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Queue"]

class Queue(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/util/Queue"
    remove = JavaMethod("()Ljava/lang/Object;")
    add = JavaMethod("(Ljava/lang/Object;)Z")
    offer = JavaMethod("(Ljava/lang/Object;)Z")
    peek = JavaMethod("()Ljava/lang/Object;")
    poll = JavaMethod("()Ljava/lang/Object;")
    element = JavaMethod("()Ljava/lang/Object;")