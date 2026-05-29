from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Authenticator"]

class Authenticator(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/net/Authenticator"
    __javaconstructor__ = [("()V", False)]
    getDefault = JavaStaticMethod("()Ljava/net/Authenticator;")
    requestPasswordAuthenticationInstance = JavaMethod("(Ljava/lang/String;Ljava/net/InetAddress;ILjava/lang/String;Ljava/lang/String;Ljava/lang/String;Ljava/net/URL;Ljava/net/Authenticator$RequestorType;)Ljava/net/PasswordAuthentication;")
    requestPasswordAuthentication = JavaMultipleMethod([("(Ljava/lang/String;Ljava/net/InetAddress;ILjava/lang/String;Ljava/lang/String;Ljava/lang/String;Ljava/net/URL;Ljava/net/Authenticator$RequestorType;)Ljava/net/PasswordAuthentication;", True, False), ("(Ljava/net/Authenticator;Ljava/lang/String;Ljava/net/InetAddress;ILjava/lang/String;Ljava/lang/String;Ljava/lang/String;Ljava/net/URL;Ljava/net/Authenticator$RequestorType;)Ljava/net/PasswordAuthentication;", True, False), ("(Ljava/lang/String;Ljava/net/InetAddress;ILjava/lang/String;Ljava/lang/String;Ljava/lang/String;)Ljava/net/PasswordAuthentication;", True, False), ("(Ljava/net/InetAddress;ILjava/lang/String;Ljava/lang/String;Ljava/lang/String;)Ljava/net/PasswordAuthentication;", True, False)])
    setDefault = JavaStaticMethod("(Ljava/net/Authenticator;)V")

    class RequestorType(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "java/net/Authenticator$RequestorType"
        PROXY = JavaStaticField("Ljava/net/Authenticator$RequestorType;")
        SERVER = JavaStaticField("Ljava/net/Authenticator$RequestorType;")
        values = JavaStaticMethod("()[Ljava/net/Authenticator$RequestorType;")
        valueOf = JavaStaticMethod("(Ljava/lang/String;)Ljava/net/Authenticator$RequestorType;")
        PROXY = JavaStaticField("Ljava/net/Authenticator$RequestorType;")
        SERVER = JavaStaticField("Ljava/net/Authenticator$RequestorType;")