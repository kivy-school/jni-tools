from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["DirectoryStream"]

class DirectoryStream(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "java/nio/file/DirectoryStream"
    iterator = JavaMethod("()Ljava/util/Iterator;")

    class Filter(JavaInterface, metaclass=MetaJavaClass):
        __javaclass__ = "java/nio/file/DirectoryStream/Filter"
        accept = JavaMethod("(Ljava/lang/Object;)Z")