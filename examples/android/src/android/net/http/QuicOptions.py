from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["QuicOptions"]

class QuicOptions(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/net/http/QuicOptions"
    getAllowedQuicHosts = JavaMethod("()Ljava/util/Set;")
    hasInMemoryServerConfigsCacheSize = JavaMethod("()Z")
    getInMemoryServerConfigsCacheSize = JavaMethod("()I")
    getHandshakeUserAgent = JavaMethod("()Ljava/lang/String;")
    getIdleConnectionTimeout = JavaMethod("()Ljava/time/Duration;")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/net/http/QuicOptions/Builder"
        __javaconstructor__ = [("()V", False)]
        addAllowedQuicHost = JavaMethod("(Ljava/lang/String;)Landroid/net/http/QuicOptions$Builder;")
        setInMemoryServerConfigsCacheSize = JavaMethod("(I)Landroid/net/http/QuicOptions$Builder;")
        setHandshakeUserAgent = JavaMethod("(Ljava/lang/String;)Landroid/net/http/QuicOptions$Builder;")
        setIdleConnectionTimeout = JavaMethod("(Ljava/time/Duration;)Landroid/net/http/QuicOptions$Builder;")
        build = JavaMethod("()Landroid/net/http/QuicOptions;")