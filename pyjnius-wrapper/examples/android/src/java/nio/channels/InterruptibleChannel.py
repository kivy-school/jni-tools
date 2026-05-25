from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["InterruptibleChannel"]

class InterruptibleChannel(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "java/nio/channels/InterruptibleChannel"
    close = JavaMethod("()V")