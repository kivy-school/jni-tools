from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ReadWriteLock"]

class ReadWriteLock(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/util/concurrent/locks/ReadWriteLock"
    writeLock = JavaMethod("()Ljava/util/concurrent/locks/Lock;")
    readLock = JavaMethod("()Ljava/util/concurrent/locks/Lock;")