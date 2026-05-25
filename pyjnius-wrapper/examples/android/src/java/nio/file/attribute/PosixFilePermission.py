from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["PosixFilePermission"]

class PosixFilePermission(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/nio/file/attribute/PosixFilePermission"
    values = JavaStaticMethod("()[Ljava/nio/file/attribute/PosixFilePermission;")
    valueOf = JavaStaticMethod("(Ljava/lang/String;)Ljava/nio/file/attribute/PosixFilePermission;")
    OWNER_READ = JavaStaticField("Ljava/nio/file/attribute/PosixFilePermission;")
    OWNER_WRITE = JavaStaticField("Ljava/nio/file/attribute/PosixFilePermission;")
    OWNER_EXECUTE = JavaStaticField("Ljava/nio/file/attribute/PosixFilePermission;")
    GROUP_READ = JavaStaticField("Ljava/nio/file/attribute/PosixFilePermission;")
    GROUP_WRITE = JavaStaticField("Ljava/nio/file/attribute/PosixFilePermission;")
    GROUP_EXECUTE = JavaStaticField("Ljava/nio/file/attribute/PosixFilePermission;")
    OTHERS_READ = JavaStaticField("Ljava/nio/file/attribute/PosixFilePermission;")
    OTHERS_WRITE = JavaStaticField("Ljava/nio/file/attribute/PosixFilePermission;")
    OTHERS_EXECUTE = JavaStaticField("Ljava/nio/file/attribute/PosixFilePermission;")