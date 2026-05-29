from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["CopyOption"]

class CopyOption(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "java/nio/file/CopyOption"