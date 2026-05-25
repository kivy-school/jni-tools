from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["FileWriter"]

class FileWriter(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/io/FileWriter"
    __javaconstructor__ = [("(Ljava/lang/String;)V", False), ("(Ljava/lang/String;Z)V", False), ("(Ljava/io/File;)V", False), ("(Ljava/io/File;Z)V", False), ("(Ljava/io/FileDescriptor;)V", False), ("(Ljava/lang/String;Ljava/nio/charset/Charset;)V", False), ("(Ljava/lang/String;Ljava/nio/charset/Charset;Z)V", False), ("(Ljava/io/File;Ljava/nio/charset/Charset;)V", False), ("(Ljava/io/File;Ljava/nio/charset/Charset;Z)V", False)]