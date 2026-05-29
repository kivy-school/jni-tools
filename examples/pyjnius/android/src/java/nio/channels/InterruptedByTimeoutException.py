from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["InterruptedByTimeoutException"]

class InterruptedByTimeoutException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/nio/channels/InterruptedByTimeoutException"
    __javaconstructor__ = [("()V", False)]