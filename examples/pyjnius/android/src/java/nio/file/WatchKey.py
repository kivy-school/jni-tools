from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["WatchKey"]

class WatchKey(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/nio/file/WatchKey"
    reset = JavaMethod("()Z")
    cancel = JavaMethod("()V")
    isValid = JavaMethod("()Z")
    pollEvents = JavaMethod("()Ljava/util/List;")
    watchable = JavaMethod("()Ljava/nio/file/Watchable;")