from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["CoreConnectionPNames"]

class CoreConnectionPNames(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "org/apache/http/params/CoreConnectionPNames"
    CONNECTION_TIMEOUT = JavaStaticField("Ljava/lang/String;")
    MAX_HEADER_COUNT = JavaStaticField("Ljava/lang/String;")
    MAX_LINE_LENGTH = JavaStaticField("Ljava/lang/String;")
    SOCKET_BUFFER_SIZE = JavaStaticField("Ljava/lang/String;")
    SO_LINGER = JavaStaticField("Ljava/lang/String;")
    SO_TIMEOUT = JavaStaticField("Ljava/lang/String;")
    STALE_CONNECTION_CHECK = JavaStaticField("Ljava/lang/String;")
    TCP_NODELAY = JavaStaticField("Ljava/lang/String;")