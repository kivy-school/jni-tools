from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["WatchService"]

class WatchService(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "java/nio/file/WatchService"
    close = JavaMethod("()V")
    poll = JavaMultipleMethod([("()Ljava/nio/file/WatchKey;", False, False), ("(JLjava/util/concurrent/TimeUnit;)Ljava/nio/file/WatchKey;", False, False)])
    take = JavaMethod("()Ljava/nio/file/WatchKey;")