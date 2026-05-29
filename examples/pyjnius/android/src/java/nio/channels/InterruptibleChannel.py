from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["InterruptibleChannel"]

class InterruptibleChannel(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/nio/channels/InterruptibleChannel"
    close = JavaMethod("()V")