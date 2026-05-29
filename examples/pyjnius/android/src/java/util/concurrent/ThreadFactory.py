from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ThreadFactory"]

class ThreadFactory(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/util/concurrent/ThreadFactory"
    newThread = JavaMethod("(Ljava/lang/Runnable;)Ljava/lang/Thread;")