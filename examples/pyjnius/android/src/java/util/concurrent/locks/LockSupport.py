from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["LockSupport"]

class LockSupport(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/util/concurrent/locks/LockSupport"
    park = JavaMultipleMethod([("()V", True, False), ("(Ljava/lang/Object;)V", True, False)])
    unpark = JavaStaticMethod("(Ljava/lang/Thread;)V")
    parkNanos = JavaMultipleMethod([("(J)V", True, False), ("(Ljava/lang/Object;J)V", True, False)])
    parkUntil = JavaMultipleMethod([("(J)V", True, False), ("(Ljava/lang/Object;J)V", True, False)])
    setCurrentBlocker = JavaStaticMethod("(Ljava/lang/Object;)V")
    getBlocker = JavaStaticMethod("(Ljava/lang/Thread;)Ljava/lang/Object;")