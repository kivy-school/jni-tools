from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["HostNameResolver"]

class HostNameResolver(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "org/apache/http/conn/scheme/HostNameResolver"
    resolve = JavaMethod("(Ljava/lang/String;)Ljava/net/InetAddress;")