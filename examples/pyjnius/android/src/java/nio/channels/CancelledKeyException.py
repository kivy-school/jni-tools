from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["CancelledKeyException"]

class CancelledKeyException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/nio/channels/CancelledKeyException"
    __javaconstructor__ = [("()V", False)]