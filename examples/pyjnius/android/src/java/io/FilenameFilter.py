from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["FilenameFilter"]

class FilenameFilter(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "java/io/FilenameFilter"
    accept = JavaMethod("(Ljava/io/File;Ljava/lang/String;)Z")