from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["FileTime"]

class FileTime(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/nio/file/attribute/FileTime"
    from = JavaMultipleMethod([("(JLjava/util/concurrent/TimeUnit;)Ljava/nio/file/attribute/FileTime;", True, False), ("(Ljava/time/Instant;)Ljava/nio/file/attribute/FileTime;", True, False)])
    fromMillis = JavaStaticMethod("(J)Ljava/nio/file/attribute/FileTime;")
    to = JavaMethod("(Ljava/util/concurrent/TimeUnit;)J")
    toMillis = JavaMethod("()J")
    toInstant = JavaMethod("()Ljava/time/Instant;")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")
    compareTo = JavaMethod("(Ljava/nio/file/attribute/FileTime;)I")
    toString = JavaMethod("()Ljava/lang/String;")