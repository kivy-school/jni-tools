from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["OpenOption"]

class OpenOption(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/nio/file/OpenOption"