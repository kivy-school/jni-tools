from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["VisualVoicemailService"]

class VisualVoicemailService(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/telephony/VisualVoicemailService"
    __javaconstructor__ = [("()V", False)]
    SERVICE_INTERFACE = JavaStaticField("Ljava/lang/String;")
    onBind = JavaMethod("(Landroid/content/Intent;)Landroid/os/IBinder;")
    onCellServiceConnected = JavaMethod("(Landroid/telephony/VisualVoicemailService$VisualVoicemailTask;Landroid/telecom/PhoneAccountHandle;)V")
    onSmsReceived = JavaMethod("(Landroid/telephony/VisualVoicemailService$VisualVoicemailTask;Landroid/telephony/VisualVoicemailSms;)V")
    onSimRemoved = JavaMethod("(Landroid/telephony/VisualVoicemailService$VisualVoicemailTask;Landroid/telecom/PhoneAccountHandle;)V")
    onStopped = JavaMethod("(Landroid/telephony/VisualVoicemailService$VisualVoicemailTask;)V")

    class VisualVoicemailTask(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/telephony/VisualVoicemailService/VisualVoicemailTask"
        finish = JavaMethod("()V")
        equals = JavaMethod("(Ljava/lang/Object;)Z")
        hashCode = JavaMethod("()I")