from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Cleaner"]

class Cleaner(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/lang/ref/Cleaner"
    register = JavaMethod("(Ljava/lang/Object;Ljava/lang/Runnable;)Ljava/lang/ref/Cleaner$Cleanable;")
    create = JavaMultipleMethod([("()Ljava/lang/ref/Cleaner;", True, False), ("(Ljava/util/concurrent/ThreadFactory;)Ljava/lang/ref/Cleaner;", True, False)])

    class Cleanable(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "java/lang/ref/Cleaner$Cleanable"
        clean = JavaMethod("()V")