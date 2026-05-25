from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["UserDefinedFileAttributeView"]

class UserDefinedFileAttributeView(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "java/nio/file/attribute/UserDefinedFileAttributeView"
    name = JavaMethod("()Ljava/lang/String;")
    list = JavaMethod("()Ljava/util/List;")
    size = JavaMethod("(Ljava/lang/String;)I")
    read = JavaMethod("(Ljava/lang/String;Ljava/nio/ByteBuffer;)I")
    write = JavaMethod("(Ljava/lang/String;Ljava/nio/ByteBuffer;)I")
    delete = JavaMethod("(Ljava/lang/String;)V")