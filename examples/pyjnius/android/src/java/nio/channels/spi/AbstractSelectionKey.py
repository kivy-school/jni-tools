from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["AbstractSelectionKey"]

class AbstractSelectionKey(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/nio/channels/spi/AbstractSelectionKey"
    OP_READ = JavaStaticField("I")
    OP_WRITE = JavaStaticField("I")
    OP_CONNECT = JavaStaticField("I")
    OP_ACCEPT = JavaStaticField("I")
    cancel = JavaMethod("()V")
    isValid = JavaMethod("()Z")