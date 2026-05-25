from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["CallRedirectionService"]

class CallRedirectionService(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/telecom/CallRedirectionService"
    __javaconstructor__ = [("()V", False)]
    SERVICE_INTERFACE = JavaStaticField("Ljava/lang/String;")
    onPlaceCall = JavaMethod("(Landroid/net/Uri;Landroid/telecom/PhoneAccountHandle;Z)V")
    onRedirectionTimeout = JavaMethod("()V")
    placeCallUnmodified = JavaMethod("()V")
    redirectCall = JavaMethod("(Landroid/net/Uri;Landroid/telecom/PhoneAccountHandle;Z)V")
    cancelCall = JavaMethod("()V")
    onBind = JavaMethod("(Landroid/content/Intent;)Landroid/os/IBinder;")
    onUnbind = JavaMethod("(Landroid/content/Intent;)Z")