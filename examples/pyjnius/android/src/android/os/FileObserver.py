from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["FileObserver"]

class FileObserver(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/os/FileObserver"
    __javaconstructor__ = [("(Ljava/io/File;)V", False), ("(Ljava/util/List;I)V", False), ("(Ljava/util/List;)V", False), ("(Ljava/lang/String;)V", False), ("(Ljava/io/File;I)V", False), ("(Ljava/lang/String;I)V", False)]
    ACCESS = JavaStaticField("I")
    ALL_EVENTS = JavaStaticField("I")
    ATTRIB = JavaStaticField("I")
    CLOSE_NOWRITE = JavaStaticField("I")
    CLOSE_WRITE = JavaStaticField("I")
    CREATE = JavaStaticField("I")
    DELETE = JavaStaticField("I")
    DELETE_SELF = JavaStaticField("I")
    MODIFY = JavaStaticField("I")
    MOVED_FROM = JavaStaticField("I")
    MOVED_TO = JavaStaticField("I")
    MOVE_SELF = JavaStaticField("I")
    OPEN = JavaStaticField("I")
    stopWatching = JavaMethod("()V")
    startWatching = JavaMethod("()V")
    onEvent = JavaMethod("(ILjava/lang/String;)V")