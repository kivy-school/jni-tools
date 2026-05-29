from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ReadWriteLock"]

class ReadWriteLock(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "java/util/concurrent/locks/ReadWriteLock"
    readLock = JavaMethod("()Ljava/util/concurrent/locks/Lock;")
    writeLock = JavaMethod("()Ljava/util/concurrent/locks/Lock;")