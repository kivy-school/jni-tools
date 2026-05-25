from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Future"]

class Future(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "java/util/concurrent/Future"
    cancel = JavaMethod("(Z)Z")
    isCancelled = JavaMethod("()Z")
    isDone = JavaMethod("()Z")
    get = JavaMultipleMethod([("()Ljava/lang/Object;", False, False), ("(JLjava/util/concurrent/TimeUnit;)Ljava/lang/Object;", False, False)])