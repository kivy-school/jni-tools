from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["RemoteCallbackList"]

class RemoteCallbackList(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/os/RemoteCallbackList"
    __javaconstructor__ = [("()V", False)]
    FROZEN_CALLEE_POLICY_DROP = JavaStaticField("I")
    FROZEN_CALLEE_POLICY_ENQUEUE_ALL = JavaStaticField("I")
    FROZEN_CALLEE_POLICY_ENQUEUE_MOST_RECENT = JavaStaticField("I")
    FROZEN_CALLEE_POLICY_UNSET = JavaStaticField("I")
    getExecutor = JavaMethod("()Ljava/util/concurrent/Executor;")
    getBroadcastItem = JavaMethod("(I)Landroid/os/IInterface;")
    broadcast = JavaMethod("(Ljava/util/function/Consumer;)V")
    getBroadcastCookie = JavaMethod("(I)Ljava/lang/Object;")
    finishBroadcast = JavaMethod("()V")
    beginBroadcast = JavaMethod("()I")
    getFrozenCalleePolicy = JavaMethod("()I")
    getMaxQueueSize = JavaMethod("()I")
    getRegisteredCallbackCookie = JavaMethod("(I)Ljava/lang/Object;")
    getRegisteredCallbackCount = JavaMethod("()I")
    getRegisteredCallbackItem = JavaMethod("(I)Landroid/os/IInterface;")
    onCallbackDied = JavaMultipleMethod([("(Landroid/os/IInterface;Ljava/lang/Object;)V", False, False), ("(Landroid/os/IInterface;)V", False, False)])
    kill = JavaMethod("()V")
    register = JavaMultipleMethod([("(Landroid/os/IInterface;Ljava/lang/Object;)Z", False, False), ("(Landroid/os/IInterface;)Z", False, False)])
    unregister = JavaMethod("(Landroid/os/IInterface;)Z")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/os/RemoteCallbackList$Builder"
        __javaconstructor__ = [("(I)V", False)]
        setExecutor = JavaMethod("(Ljava/util/concurrent/Executor;)Landroid/os/RemoteCallbackList$Builder;")
        build = JavaMethod("()Landroid/os/RemoteCallbackList;")
        setMaxQueueSize = JavaMethod("(I)Landroid/os/RemoteCallbackList$Builder;")
        setInterfaceDiedCallback = JavaMethod("(Landroid/os/RemoteCallbackList$Builder$InterfaceDiedCallback;)Landroid/os/RemoteCallbackList$Builder;")

        class InterfaceDiedCallback(JavaClass, metaclass=MetaJavaClass):
            __javaclass__ = "android/os/RemoteCallbackList$Builder$InterfaceDiedCallback"
            onInterfaceDied = JavaMethod("(Landroid/os/RemoteCallbackList;Landroid/os/IInterface;Ljava/lang/Object;)V")