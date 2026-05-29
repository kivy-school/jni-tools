from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["StandardOpenOption"]

class StandardOpenOption(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/nio/file/StandardOpenOption"
    READ = JavaStaticField("Ljava/nio/file/StandardOpenOption;")
    WRITE = JavaStaticField("Ljava/nio/file/StandardOpenOption;")
    APPEND = JavaStaticField("Ljava/nio/file/StandardOpenOption;")
    TRUNCATE_EXISTING = JavaStaticField("Ljava/nio/file/StandardOpenOption;")
    CREATE = JavaStaticField("Ljava/nio/file/StandardOpenOption;")
    CREATE_NEW = JavaStaticField("Ljava/nio/file/StandardOpenOption;")
    DELETE_ON_CLOSE = JavaStaticField("Ljava/nio/file/StandardOpenOption;")
    SPARSE = JavaStaticField("Ljava/nio/file/StandardOpenOption;")
    SYNC = JavaStaticField("Ljava/nio/file/StandardOpenOption;")
    DSYNC = JavaStaticField("Ljava/nio/file/StandardOpenOption;")
    values = JavaStaticMethod("()[Ljava/nio/file/StandardOpenOption;")
    valueOf = JavaStaticMethod("(Ljava/lang/String;)Ljava/nio/file/StandardOpenOption;")
    READ = JavaStaticField("Ljava/nio/file/StandardOpenOption;")
    WRITE = JavaStaticField("Ljava/nio/file/StandardOpenOption;")
    APPEND = JavaStaticField("Ljava/nio/file/StandardOpenOption;")
    TRUNCATE_EXISTING = JavaStaticField("Ljava/nio/file/StandardOpenOption;")
    CREATE = JavaStaticField("Ljava/nio/file/StandardOpenOption;")
    CREATE_NEW = JavaStaticField("Ljava/nio/file/StandardOpenOption;")
    DELETE_ON_CLOSE = JavaStaticField("Ljava/nio/file/StandardOpenOption;")
    SPARSE = JavaStaticField("Ljava/nio/file/StandardOpenOption;")
    SYNC = JavaStaticField("Ljava/nio/file/StandardOpenOption;")
    DSYNC = JavaStaticField("Ljava/nio/file/StandardOpenOption;")