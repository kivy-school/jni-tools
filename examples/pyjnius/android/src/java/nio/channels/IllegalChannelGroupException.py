from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["IllegalChannelGroupException"]

class IllegalChannelGroupException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/nio/channels/IllegalChannelGroupException"
    __javaconstructor__ = [("()V", False)]