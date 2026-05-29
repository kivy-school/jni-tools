from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["TestLooperManager"]

class TestLooperManager(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/os/TestLooperManager"
    getMessageQueue = JavaMethod("()Landroid/os/MessageQueue;")
    isBlockedOnSyncBarrier = JavaMethod("()Z")
    peekWhen = JavaMethod("()Ljava/lang/Long;")
    next = JavaMethod("()Landroid/os/Message;")
    execute = JavaMethod("(Landroid/os/Message;)V")
    release = JavaMethod("()V")
    hasMessages = JavaMultipleMethod([("(Landroid/os/Handler;Ljava/lang/Object;Ljava/lang/Runnable;)Z", False, False), ("(Landroid/os/Handler;Ljava/lang/Object;I)Z", False, False)])
    poll = JavaMethod("()Landroid/os/Message;")
    recycle = JavaMethod("(Landroid/os/Message;)V")