from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ADMMessageHandlerJob"]

class ADMMessageHandlerJob(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/ADMMessageHandlerJob"
    __javaconstructor__ = [("()V", False)]
    onMessage = JavaMethod("(Landroid/content/Context;Landroid/content/Intent;)V")
    onRegistered = JavaMethod("(Landroid/content/Context;Ljava/lang/String;)V")
    onUnregistered = JavaMethod("(Landroid/content/Context;Ljava/lang/String;)V")
    onRegistrationError = JavaMethod("(Landroid/content/Context;Ljava/lang/String;)V")