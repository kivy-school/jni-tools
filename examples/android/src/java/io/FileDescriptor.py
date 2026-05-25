from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["FileDescriptor"]

class FileDescriptor(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/io/FileDescriptor"
    __javaconstructor__ = [("()V", False)]
    err = JavaStaticField("Ljava/io/FileDescriptor;")
    in = JavaStaticField("Ljava/io/FileDescriptor;")
    out = JavaStaticField("Ljava/io/FileDescriptor;")
    valid = JavaMethod("()Z")
    sync = JavaMethod("()V")