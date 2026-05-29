from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["MessageQueue"]

class MessageQueue(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/os/MessageQueue"
    isIdle = JavaMethod("()Z")
    removeIdleHandler = JavaMethod("(Landroid/os/MessageQueue$IdleHandler;)V")
    addOnFileDescriptorEventListener = JavaMethod("(Ljava/io/FileDescriptor;ILandroid/os/MessageQueue$OnFileDescriptorEventListener;)V")
    addIdleHandler = JavaMethod("(Landroid/os/MessageQueue$IdleHandler;)V")
    removeOnFileDescriptorEventListener = JavaMethod("(Ljava/io/FileDescriptor;)V")

    class OnFileDescriptorEventListener(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/os/MessageQueue$OnFileDescriptorEventListener"
        EVENT_ERROR = JavaStaticField("I")
        EVENT_INPUT = JavaStaticField("I")
        EVENT_OUTPUT = JavaStaticField("I")
        onFileDescriptorEvents = JavaMethod("(Ljava/io/FileDescriptor;I)I")

    class IdleHandler(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/os/MessageQueue$IdleHandler"
        queueIdle = JavaMethod("()Z")