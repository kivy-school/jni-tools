from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Reference"]

class Reference(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/lang/ref/Reference"
    clear = JavaMethod("()V")
    get = JavaMethod("()Ljava/lang/Object;")
    enqueue = JavaMethod("()Z")
    refersTo = JavaMethod("(Ljava/lang/Object;)Z")
    isEnqueued = JavaMethod("()Z")
    reachabilityFence = JavaStaticMethod("(Ljava/lang/Object;)V")