from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["FCMBroadcastReceiver"]

class FCMBroadcastReceiver(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/FCMBroadcastReceiver"
    __javaconstructor__ = [("()V", False)]
    onReceive = JavaMethod("(Landroid/content/Context;Landroid/content/Intent;)V")