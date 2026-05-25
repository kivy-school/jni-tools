from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Authenticator"]

class Authenticator(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/net/Authenticator"
    __javaconstructor__ = [("()V", False)]
    setDefault = JavaStaticMethod("(Ljava/net/Authenticator;)V")
    requestPasswordAuthentication = JavaMultipleMethod([("(Ljava/net/InetAddress;ILjava/lang/String;Ljava/lang/String;Ljava/lang/String;)Ljava/net/PasswordAuthentication;", True, False), ("(Ljava/lang/String;Ljava/net/InetAddress;ILjava/lang/String;Ljava/lang/String;Ljava/lang/String;)Ljava/net/PasswordAuthentication;", True, False), ("(Ljava/lang/String;Ljava/net/InetAddress;ILjava/lang/String;Ljava/lang/String;Ljava/lang/String;Ljava/net/URL;Ljava/net/Authenticator$RequestorType;)Ljava/net/PasswordAuthentication;", True, False)])
    getRequestingHost = JavaMethod("()Ljava/lang/String;")
    getRequestingSite = JavaMethod("()Ljava/net/InetAddress;")
    getRequestingPort = JavaMethod("()I")
    getRequestingProtocol = JavaMethod("()Ljava/lang/String;")
    getRequestingPrompt = JavaMethod("()Ljava/lang/String;")
    getRequestingScheme = JavaMethod("()Ljava/lang/String;")
    getPasswordAuthentication = JavaMethod("()Ljava/net/PasswordAuthentication;")
    getRequestingURL = JavaMethod("()Ljava/net/URL;")
    getRequestorType = JavaMethod("()Ljava/net/Authenticator$RequestorType;")

    class RequestorType(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "java/net/Authenticator/RequestorType"
        values = JavaStaticMethod("()[Ljava/net/Authenticator$RequestorType;")
        valueOf = JavaStaticMethod("(Ljava/lang/String;)Ljava/net/Authenticator$RequestorType;")
        PROXY = JavaStaticField("Ljava/net/Authenticator/RequestorType;")
        SERVER = JavaStaticField("Ljava/net/Authenticator/RequestorType;")