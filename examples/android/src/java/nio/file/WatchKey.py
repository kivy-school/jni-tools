from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["WatchKey"]

class WatchKey(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "java/nio/file/WatchKey"
    isValid = JavaMethod("()Z")
    pollEvents = JavaMethod("()Ljava/util/List;")
    reset = JavaMethod("()Z")
    cancel = JavaMethod("()V")
    watchable = JavaMethod("()Ljava/nio/file/Watchable;")