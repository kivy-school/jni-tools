from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["CallScreeningService"]

class CallScreeningService(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/telecom/CallScreeningService"
    __javaconstructor__ = [("()V", False)]
    SERVICE_INTERFACE = JavaStaticField("Ljava/lang/String;")
    onBind = JavaMethod("(Landroid/content/Intent;)Landroid/os/IBinder;")
    onUnbind = JavaMethod("(Landroid/content/Intent;)Z")
    onScreenCall = JavaMethod("(Landroid/telecom/Call$Details;)V")
    respondToCall = JavaMethod("(Landroid/telecom/Call$Details;Landroid/telecom/CallScreeningService$CallResponse;)V")

    class CallResponse(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/telecom/CallScreeningService/CallResponse"
        CALL_COMPOSER_ATTACHMENT_LOCATION = JavaStaticField("I")
        CALL_COMPOSER_ATTACHMENT_PICTURE = JavaStaticField("I")
        CALL_COMPOSER_ATTACHMENT_PRIORITY = JavaStaticField("I")
        CALL_COMPOSER_ATTACHMENT_SUBJECT = JavaStaticField("I")
        getDisallowCall = JavaMethod("()Z")
        getRejectCall = JavaMethod("()Z")
        getSilenceCall = JavaMethod("()Z")
        getSkipCallLog = JavaMethod("()Z")
        getSkipNotification = JavaMethod("()Z")
        getCallComposerAttachmentsToShow = JavaMethod("()I")
        equals = JavaMethod("(Ljava/lang/Object;)Z")
        hashCode = JavaMethod("()I")

        class Builder(JavaClass, metaclass=MetaJavaClass):
            __javaclass__ = "android/telecom/CallScreeningService/CallResponse/Builder"
            __javaconstructor__ = [("()V", False)]
            setDisallowCall = JavaMethod("(Z)Landroid/telecom/CallScreeningService$CallResponse$Builder;")
            setRejectCall = JavaMethod("(Z)Landroid/telecom/CallScreeningService$CallResponse$Builder;")
            setSilenceCall = JavaMethod("(Z)Landroid/telecom/CallScreeningService$CallResponse$Builder;")
            setSkipCallLog = JavaMethod("(Z)Landroid/telecom/CallScreeningService$CallResponse$Builder;")
            setSkipNotification = JavaMethod("(Z)Landroid/telecom/CallScreeningService$CallResponse$Builder;")
            setCallComposerAttachmentsToShow = JavaMethod("(I)Landroid/telecom/CallScreeningService$CallResponse$Builder;")
            build = JavaMethod("()Landroid/telecom/CallScreeningService$CallResponse;")