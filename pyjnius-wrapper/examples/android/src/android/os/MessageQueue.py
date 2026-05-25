from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["MessageQueue"]

class MessageQueue(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/os/MessageQueue"
    finalize = JavaMethod("()V")
    isIdle = JavaMethod("()Z")
    addIdleHandler = JavaMethod("(Landroid/os/MessageQueue$IdleHandler;)V")
    removeIdleHandler = JavaMethod("(Landroid/os/MessageQueue$IdleHandler;)V")
    addOnFileDescriptorEventListener = JavaMethod("(Ljava/io/FileDescriptor;ILandroid/os/MessageQueue$OnFileDescriptorEventListener;)V")
    removeOnFileDescriptorEventListener = JavaMethod("(Ljava/io/FileDescriptor;)V")

    class IdleHandler(JavaInterface, metaclass=MetaJavaClass):
        __javaclass__ = "android/os/MessageQueue/IdleHandler"
        queueIdle = JavaMethod("()Z")

    class OnFileDescriptorEventListener(JavaInterface, metaclass=MetaJavaClass):
        __javaclass__ = "android/os/MessageQueue/OnFileDescriptorEventListener"
        EVENT_ERROR = JavaStaticField("I")
        EVENT_INPUT = JavaStaticField("I")
        EVENT_OUTPUT = JavaStaticField("I")
        onFileDescriptorEvents = JavaMethod("(Ljava/io/FileDescriptor;I)I")