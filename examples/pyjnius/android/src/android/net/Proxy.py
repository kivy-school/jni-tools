from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Proxy"]

class Proxy(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/net/Proxy"
    __javaconstructor__ = [("()V", False)]
    PROXY_CHANGE_ACTION = JavaStaticField("Ljava/lang/String;")
    getDefaultHost = JavaStaticMethod("()Ljava/lang/String;")
    getHost = JavaStaticMethod("(Landroid/content/Context;)Ljava/lang/String;")
    getPort = JavaStaticMethod("(Landroid/content/Context;)I")
    getDefaultPort = JavaStaticMethod("()I")