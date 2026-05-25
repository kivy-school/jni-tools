from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["IllegalBlockingModeException"]

class IllegalBlockingModeException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/nio/channels/IllegalBlockingModeException"
    __javaconstructor__ = [("()V", False)]