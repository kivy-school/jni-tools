from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Cleaner"]

class Cleaner(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/lang/ref/Cleaner"
    create = JavaMultipleMethod([("()Ljava/lang/ref/Cleaner;", True, False), ("(Ljava/util/concurrent/ThreadFactory;)Ljava/lang/ref/Cleaner;", True, False)])
    register = JavaMethod("(Ljava/lang/Object;Ljava/lang/Runnable;)Ljava/lang/ref/Cleaner$Cleanable;")

    class Cleanable(JavaInterface, metaclass=MetaJavaClass):
        __javaclass__ = "java/lang/ref/Cleaner/Cleanable"
        clean = JavaMethod("()V")