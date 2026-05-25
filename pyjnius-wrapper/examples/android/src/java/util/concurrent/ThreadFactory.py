from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ThreadFactory"]

class ThreadFactory(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "java/util/concurrent/ThreadFactory"
    newThread = JavaMethod("(Ljava/lang/Runnable;)Ljava/lang/Thread;")