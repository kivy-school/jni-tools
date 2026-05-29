from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["DirectoryStream"]

class DirectoryStream(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/nio/file/DirectoryStream"
    iterator = JavaMethod("()Ljava/util/Iterator;")

    class Filter(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "java/nio/file/DirectoryStream$Filter"
        accept = JavaMethod("(Ljava/lang/Object;)Z")