from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["IkeSession"]

class IkeSession(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/net/ipsec/ike/IkeSession"
    __javaconstructor__ = [("(Landroid/content/Context;Landroid/net/ipsec/ike/IkeSessionParams;Landroid/net/ipsec/ike/ChildSessionParams;Ljava/util/concurrent/Executor;Landroid/net/ipsec/ike/IkeSessionCallback;Landroid/net/ipsec/ike/ChildSessionCallback;)V", False)]
    finalize = JavaMethod("()V")
    openChildSession = JavaMethod("(Landroid/net/ipsec/ike/ChildSessionParams;Landroid/net/ipsec/ike/ChildSessionCallback;)V")
    closeChildSession = JavaMethod("(Landroid/net/ipsec/ike/ChildSessionCallback;)V")
    close = JavaMethod("()V")
    kill = JavaMethod("()V")
    dump = JavaMethod("(Ljava/io/PrintWriter;)V")