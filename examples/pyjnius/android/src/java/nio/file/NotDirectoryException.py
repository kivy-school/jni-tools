from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["NotDirectoryException"]

class NotDirectoryException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/nio/file/NotDirectoryException"
    __javaconstructor__ = [("(Ljava/lang/String;)V", False)]