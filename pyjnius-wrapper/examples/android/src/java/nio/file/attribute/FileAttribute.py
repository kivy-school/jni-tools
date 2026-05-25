from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["FileAttribute"]

class FileAttribute(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "java/nio/file/attribute/FileAttribute"
    name = JavaMethod("()Ljava/lang/String;")
    value = JavaMethod("()Ljava/lang/Object;")