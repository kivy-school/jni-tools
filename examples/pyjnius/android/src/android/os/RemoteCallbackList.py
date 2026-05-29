from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["RemoteCallbackList"]

class RemoteCallbackList(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/os/RemoteCallbackList"
    __javaconstructor__ = [("()V", False)]
    register = JavaMultipleMethod([("(Landroid/os/IInterface;)Z", False, False), ("(Landroid/os/IInterface;Ljava/lang/Object;)Z", False, False)])
    unregister = JavaMethod("(Landroid/os/IInterface;)Z")
    kill = JavaMethod("()V")
    onCallbackDied = JavaMultipleMethod([("(Landroid/os/IInterface;)V", False, False), ("(Landroid/os/IInterface;Ljava/lang/Object;)V", False, False)])
    beginBroadcast = JavaMethod("()I")
    getBroadcastItem = JavaMethod("(I)Landroid/os/IInterface;")
    getBroadcastCookie = JavaMethod("(I)Ljava/lang/Object;")
    finishBroadcast = JavaMethod("()V")
    getRegisteredCallbackCount = JavaMethod("()I")
    getRegisteredCallbackItem = JavaMethod("(I)Landroid/os/IInterface;")
    getRegisteredCallbackCookie = JavaMethod("(I)Ljava/lang/Object;")