from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["WatchService"]

class WatchService(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/nio/file/WatchService"
    close = JavaMethod("()V")
    poll = JavaMultipleMethod([("(JLjava/util/concurrent/TimeUnit;)Ljava/nio/file/WatchKey;", False, False), ("()Ljava/nio/file/WatchKey;", False, False)])
    take = JavaMethod("()Ljava/nio/file/WatchKey;")