from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ProtocolFamily"]

class ProtocolFamily(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/net/ProtocolFamily"
    name = JavaMethod("()Ljava/lang/String;")