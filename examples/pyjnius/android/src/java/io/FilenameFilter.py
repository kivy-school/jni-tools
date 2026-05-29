from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["FilenameFilter"]

class FilenameFilter(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/io/FilenameFilter"
    accept = JavaMethod("(Ljava/io/File;Ljava/lang/String;)Z")