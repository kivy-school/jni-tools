from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["AcceptPendingException"]

class AcceptPendingException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/nio/channels/AcceptPendingException"
    __javaconstructor__ = [("()V", False)]