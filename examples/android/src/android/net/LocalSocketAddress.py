from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["LocalSocketAddress"]

class LocalSocketAddress(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/net/LocalSocketAddress"
    __javaconstructor__ = [("(Ljava/lang/String;Landroid/net/LocalSocketAddress$Namespace;)V", False), ("(Ljava/lang/String;)V", False)]
    getName = JavaMethod("()Ljava/lang/String;")
    getNamespace = JavaMethod("()Landroid/net/LocalSocketAddress$Namespace;")

    class Namespace(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/net/LocalSocketAddress/Namespace"
        values = JavaStaticMethod("()[Landroid/net/LocalSocketAddress$Namespace;")
        valueOf = JavaStaticMethod("(Ljava/lang/String;)Landroid/net/LocalSocketAddress$Namespace;")
        ABSTRACT = JavaStaticField("Landroid/net/LocalSocketAddress/Namespace;")
        RESERVED = JavaStaticField("Landroid/net/LocalSocketAddress/Namespace;")
        FILESYSTEM = JavaStaticField("Landroid/net/LocalSocketAddress/Namespace;")