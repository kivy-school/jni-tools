from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["FileFilter"]

class FileFilter(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/io/FileFilter"
    accept = JavaMethod("(Ljava/io/File;)Z")