from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Channel"]

class Channel(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "java/nio/channels/Channel"
    isOpen = JavaMethod("()Z")
    close = JavaMethod("()V")