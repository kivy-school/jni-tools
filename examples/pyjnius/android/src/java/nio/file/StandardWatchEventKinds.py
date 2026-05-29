from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["StandardWatchEventKinds"]

class StandardWatchEventKinds(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/nio/file/StandardWatchEventKinds"
    OVERFLOW = JavaStaticField("Ljava/nio/file/WatchEvent$Kind;")
    ENTRY_CREATE = JavaStaticField("Ljava/nio/file/WatchEvent$Kind;")
    ENTRY_DELETE = JavaStaticField("Ljava/nio/file/WatchEvent$Kind;")
    ENTRY_MODIFY = JavaStaticField("Ljava/nio/file/WatchEvent$Kind;")