from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ADMMessageHandler"]

class ADMMessageHandler(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/ADMMessageHandler"
    __javaconstructor__ = [("()V", False)]
    onMessage = JavaMethod("(Landroid/content/Intent;)V")
    onRegistered = JavaMethod("(Ljava/lang/String;)V")
    onRegistrationError = JavaMethod("(Ljava/lang/String;)V")
    onUnregistered = JavaMethod("(Ljava/lang/String;)V")

    class Receiver(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "com/onesignal/ADMMessageHandler/Receiver"
        __javaconstructor__ = [("()V", False)]