from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["FileFilter"]

class FileFilter(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "java/io/FileFilter"
    accept = JavaMethod("(Ljava/io/File;)Z")