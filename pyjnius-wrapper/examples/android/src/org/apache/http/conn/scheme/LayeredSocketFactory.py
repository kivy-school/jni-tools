from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["LayeredSocketFactory"]

class LayeredSocketFactory(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "org/apache/http/conn/scheme/LayeredSocketFactory"
    createSocket = JavaMethod("(Ljava/net/Socket;Ljava/lang/String;IZ)Ljava/net/Socket;")