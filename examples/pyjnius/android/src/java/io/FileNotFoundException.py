from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["FileNotFoundException"]

class FileNotFoundException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/io/FileNotFoundException"
    __javaconstructor__ = [("()V", False), ("(Ljava/lang/String;)V", False)]