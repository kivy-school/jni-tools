from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Reference"]

class Reference(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/lang/ref/Reference"
    get = JavaMethod("()Ljava/lang/Object;")
    refersTo = JavaMethod("(Ljava/lang/Object;)Z")
    clear = JavaMethod("()V")
    isEnqueued = JavaMethod("()Z")
    enqueue = JavaMethod("()Z")
    clone = JavaMethod("()Ljava/lang/Object;")
    reachabilityFence = JavaStaticMethod("(Ljava/lang/Object;)V")