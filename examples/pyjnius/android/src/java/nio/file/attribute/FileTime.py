from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["FileTime"]

class FileTime(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/nio/file/attribute/FileTime"
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    toString = JavaMethod("()Ljava/lang/String;")
    hashCode = JavaMethod("()I")
    compareTo = JavaMultipleMethod([("(Ljava/nio/file/attribute/FileTime;)I", False, False), ("(Ljava/lang/Object;)I", False, False)])
    from = JavaMultipleMethod([("(Ljava/time/Instant;)Ljava/nio/file/attribute/FileTime;", True, False), ("(JLjava/util/concurrent/TimeUnit;)Ljava/nio/file/attribute/FileTime;", True, False)])
    to = JavaMethod("(Ljava/util/concurrent/TimeUnit;)J")
    toMillis = JavaMethod("()J")
    toInstant = JavaMethod("()Ljava/time/Instant;")
    fromMillis = JavaStaticMethod("(J)Ljava/nio/file/attribute/FileTime;")