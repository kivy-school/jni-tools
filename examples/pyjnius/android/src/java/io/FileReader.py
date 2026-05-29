from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["FileReader"]

class FileReader(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/io/FileReader"
    __javaconstructor__ = [("(Ljava/io/File;Ljava/nio/charset/Charset;)V", False), ("(Ljava/lang/String;Ljava/nio/charset/Charset;)V", False), ("(Ljava/io/FileDescriptor;)V", False), ("(Ljava/io/File;)V", False), ("(Ljava/lang/String;)V", False)]