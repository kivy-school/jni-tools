from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["DirectoryNotEmptyException"]

class DirectoryNotEmptyException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/nio/file/DirectoryNotEmptyException"
    __javaconstructor__ = [("(Ljava/lang/String;)V", False)]