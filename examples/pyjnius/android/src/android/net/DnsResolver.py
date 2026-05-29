from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["DnsResolver"]

class DnsResolver(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/net/DnsResolver"
    CLASS_IN = JavaStaticField("I")
    ERROR_PARSE = JavaStaticField("I")
    ERROR_SYSTEM = JavaStaticField("I")
    FLAG_EMPTY = JavaStaticField("I")
    FLAG_NO_CACHE_LOOKUP = JavaStaticField("I")
    FLAG_NO_CACHE_STORE = JavaStaticField("I")
    FLAG_NO_RETRY = JavaStaticField("I")
    TYPE_A = JavaStaticField("I")
    TYPE_AAAA = JavaStaticField("I")
    getInstance = JavaStaticMethod("()Landroid/net/DnsResolver;")
    query = JavaMultipleMethod([("(Landroid/net/Network;Ljava/lang/String;ILjava/util/concurrent/Executor;Landroid/os/CancellationSignal;Landroid/net/DnsResolver$Callback;)V", False, False), ("(Landroid/net/Network;Ljava/lang/String;IILjava/util/concurrent/Executor;Landroid/os/CancellationSignal;Landroid/net/DnsResolver$Callback;)V", False, False)])
    rawQuery = JavaMultipleMethod([("(Landroid/net/Network;[BILjava/util/concurrent/Executor;Landroid/os/CancellationSignal;Landroid/net/DnsResolver$Callback;)V", False, False), ("(Landroid/net/Network;Ljava/lang/String;IIILjava/util/concurrent/Executor;Landroid/os/CancellationSignal;Landroid/net/DnsResolver$Callback;)V", False, False)])

    class DnsException(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/net/DnsResolver$DnsException"
        __javaconstructor__ = [("(ILjava/lang/Throwable;)V", False)]
        code = JavaField("I")

    class Callback(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/net/DnsResolver$Callback"
        onAnswer = JavaMethod("(Ljava/lang/Object;I)V")
        onError = JavaMethod("(Landroid/net/DnsResolver$DnsException;)V")