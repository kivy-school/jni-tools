from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["CopyOption"]

class CopyOption(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/nio/file/CopyOption"