from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["OpenOption"]

class OpenOption(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "java/nio/file/OpenOption"