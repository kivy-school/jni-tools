from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["LockSupport"]

class LockSupport(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/util/concurrent/locks/LockSupport"
    setCurrentBlocker = JavaStaticMethod("(Ljava/lang/Object;)V")
    unpark = JavaStaticMethod("(Ljava/lang/Thread;)V")
    park = JavaMultipleMethod([("(Ljava/lang/Object;)V", True, False), ("()V", True, False)])
    parkNanos = JavaMultipleMethod([("(Ljava/lang/Object;J)V", True, False), ("(J)V", True, False)])
    parkUntil = JavaMultipleMethod([("(Ljava/lang/Object;J)V", True, False), ("(J)V", True, False)])
    getBlocker = JavaStaticMethod("(Ljava/lang/Thread;)Ljava/lang/Object;")