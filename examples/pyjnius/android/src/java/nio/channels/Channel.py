from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Channel"]

class Channel(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/nio/channels/Channel"
    isOpen = JavaMethod("()Z")
    close = JavaMethod("()V")