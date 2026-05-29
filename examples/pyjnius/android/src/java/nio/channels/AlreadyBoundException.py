from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["AlreadyBoundException"]

class AlreadyBoundException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/nio/channels/AlreadyBoundException"
    __javaconstructor__ = [("()V", False)]