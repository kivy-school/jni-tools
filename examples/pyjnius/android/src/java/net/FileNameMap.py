from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["FileNameMap"]

class FileNameMap(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/net/FileNameMap"
    getContentTypeFor = JavaMethod("(Ljava/lang/String;)Ljava/lang/String;")