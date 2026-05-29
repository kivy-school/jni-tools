from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["AccessMode"]

class AccessMode(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/nio/file/AccessMode"
    READ = JavaStaticField("Ljava/nio/file/AccessMode;")
    WRITE = JavaStaticField("Ljava/nio/file/AccessMode;")
    EXECUTE = JavaStaticField("Ljava/nio/file/AccessMode;")
    values = JavaStaticMethod("()[Ljava/nio/file/AccessMode;")
    valueOf = JavaStaticMethod("(Ljava/lang/String;)Ljava/nio/file/AccessMode;")
    READ = JavaStaticField("Ljava/nio/file/AccessMode;")
    WRITE = JavaStaticField("Ljava/nio/file/AccessMode;")
    EXECUTE = JavaStaticField("Ljava/nio/file/AccessMode;")