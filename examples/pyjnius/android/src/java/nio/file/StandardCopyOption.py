from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["StandardCopyOption"]

class StandardCopyOption(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/nio/file/StandardCopyOption"
    REPLACE_EXISTING = JavaStaticField("Ljava/nio/file/StandardCopyOption;")
    COPY_ATTRIBUTES = JavaStaticField("Ljava/nio/file/StandardCopyOption;")
    ATOMIC_MOVE = JavaStaticField("Ljava/nio/file/StandardCopyOption;")
    values = JavaStaticMethod("()[Ljava/nio/file/StandardCopyOption;")
    valueOf = JavaStaticMethod("(Ljava/lang/String;)Ljava/nio/file/StandardCopyOption;")
    REPLACE_EXISTING = JavaStaticField("Ljava/nio/file/StandardCopyOption;")
    COPY_ATTRIBUTES = JavaStaticField("Ljava/nio/file/StandardCopyOption;")
    ATOMIC_MOVE = JavaStaticField("Ljava/nio/file/StandardCopyOption;")