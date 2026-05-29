from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ShutdownChannelGroupException"]

class ShutdownChannelGroupException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/nio/channels/ShutdownChannelGroupException"
    __javaconstructor__ = [("()V", False)]