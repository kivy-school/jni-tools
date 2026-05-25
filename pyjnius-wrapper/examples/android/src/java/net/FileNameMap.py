from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["FileNameMap"]

class FileNameMap(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "java/net/FileNameMap"
    getContentTypeFor = JavaMethod("(Ljava/lang/String;)Ljava/lang/String;")