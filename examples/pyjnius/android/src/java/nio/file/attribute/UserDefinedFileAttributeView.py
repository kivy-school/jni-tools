from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["UserDefinedFileAttributeView"]

class UserDefinedFileAttributeView(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/nio/file/attribute/UserDefinedFileAttributeView"
    name = JavaMethod("()Ljava/lang/String;")
    size = JavaMethod("(Ljava/lang/String;)I")
    list = JavaMethod("()Ljava/util/List;")
    write = JavaMethod("(Ljava/lang/String;Ljava/nio/ByteBuffer;)I")
    delete = JavaMethod("(Ljava/lang/String;)V")
    read = JavaMethod("(Ljava/lang/String;Ljava/nio/ByteBuffer;)I")