from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["QuicOptions"]

class QuicOptions(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/net/http/QuicOptions"
    getIdleConnectionTimeout = JavaMethod("()Ljava/time/Duration;")
    getHandshakeUserAgent = JavaMethod("()Ljava/lang/String;")
    getAllowedQuicHosts = JavaMethod("()Ljava/util/Set;")
    getInMemoryServerConfigsCacheSize = JavaMethod("()I")
    hasInMemoryServerConfigsCacheSize = JavaMethod("()Z")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/net/http/QuicOptions$Builder"
        __javaconstructor__ = [("()V", False)]
        setIdleConnectionTimeout = JavaMethod("(Ljava/time/Duration;)Landroid/net/http/QuicOptions$Builder;")
        addAllowedQuicHost = JavaMethod("(Ljava/lang/String;)Landroid/net/http/QuicOptions$Builder;")
        setHandshakeUserAgent = JavaMethod("(Ljava/lang/String;)Landroid/net/http/QuicOptions$Builder;")
        setInMemoryServerConfigsCacheSize = JavaMethod("(I)Landroid/net/http/QuicOptions$Builder;")
        build = JavaMethod("()Landroid/net/http/QuicOptions;")