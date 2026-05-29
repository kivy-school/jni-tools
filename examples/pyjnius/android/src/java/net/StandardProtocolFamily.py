from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["StandardProtocolFamily"]

class StandardProtocolFamily(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/net/StandardProtocolFamily"
    INET = JavaStaticField("Ljava/net/StandardProtocolFamily;")
    INET6 = JavaStaticField("Ljava/net/StandardProtocolFamily;")
    UNIX = JavaStaticField("Ljava/net/StandardProtocolFamily;")
    values = JavaStaticMethod("()[Ljava/net/StandardProtocolFamily;")
    valueOf = JavaStaticMethod("(Ljava/lang/String;)Ljava/net/StandardProtocolFamily;")
    INET = JavaStaticField("Ljava/net/StandardProtocolFamily;")
    INET6 = JavaStaticField("Ljava/net/StandardProtocolFamily;")
    UNIX = JavaStaticField("Ljava/net/StandardProtocolFamily;")