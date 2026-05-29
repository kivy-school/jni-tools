from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["SEService"]

class SEService(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/se/omapi/SEService"
    __javaconstructor__ = [("(Landroid/content/Context;Ljava/util/concurrent/Executor;Landroid/se/omapi/SEService$OnConnectedListener;)V", False)]
    ACTION_SECURE_ELEMENT_STATE_CHANGED = JavaStaticField("Ljava/lang/String;")
    EXTRA_READER_NAME = JavaStaticField("Ljava/lang/String;")
    EXTRA_READER_STATE = JavaStaticField("Ljava/lang/String;")
    isConnected = JavaMethod("()Z")
    shutdown = JavaMethod("()V")
    getReaders = JavaMethod("()[Landroid/se/omapi/Reader;")
    getUiccReader = JavaMethod("(I)Landroid/se/omapi/Reader;")
    getVersion = JavaMethod("()Ljava/lang/String;")

    class OnConnectedListener(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/se/omapi/SEService$OnConnectedListener"
        onConnected = JavaMethod("()V")