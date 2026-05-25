from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["AsynchronousChannel"]

class AsynchronousChannel(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "java/nio/channels/AsynchronousChannel"
    close = JavaMethod("()V")