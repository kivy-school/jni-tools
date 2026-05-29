from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["FileReader"]

class FileReader(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/io/FileReader"
    __javaconstructor__ = [("(Ljava/lang/String;)V", False), ("(Ljava/io/File;)V", False), ("(Ljava/io/FileDescriptor;)V", False), ("(Ljava/lang/String;Ljava/nio/charset/Charset;)V", False), ("(Ljava/io/File;Ljava/nio/charset/Charset;)V", False)]