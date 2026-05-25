from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ProtocolFamily"]

class ProtocolFamily(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "java/net/ProtocolFamily"
    name = JavaMethod("()Ljava/lang/String;")