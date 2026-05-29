from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["AlreadyConnectedException"]

class AlreadyConnectedException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/nio/channels/AlreadyConnectedException"
    __javaconstructor__ = [("()V", False)]