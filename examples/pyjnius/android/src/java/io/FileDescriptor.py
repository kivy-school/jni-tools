from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["FileDescriptor"]

class FileDescriptor(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/io/FileDescriptor"
    __javaconstructor__ = [("()V", False)]
    in = JavaStaticField("Ljava/io/FileDescriptor;")
    out = JavaStaticField("Ljava/io/FileDescriptor;")
    err = JavaStaticField("Ljava/io/FileDescriptor;")
    sync = JavaMethod("()V")
    valid = JavaMethod("()Z")