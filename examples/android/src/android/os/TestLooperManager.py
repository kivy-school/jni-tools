from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["TestLooperManager"]

class TestLooperManager(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/os/TestLooperManager"
    getMessageQueue = JavaMethod("()Landroid/os/MessageQueue;")
    next = JavaMethod("()Landroid/os/Message;")
    release = JavaMethod("()V")
    execute = JavaMethod("(Landroid/os/Message;)V")
    recycle = JavaMethod("(Landroid/os/Message;)V")
    hasMessages = JavaMultipleMethod([("(Landroid/os/Handler;Ljava/lang/Object;I)Z", False, False), ("(Landroid/os/Handler;Ljava/lang/Object;Ljava/lang/Runnable;)Z", False, False)])