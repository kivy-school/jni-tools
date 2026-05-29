from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["RegistrationManager"]

class RegistrationManager(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/telephony/ims/RegistrationManager"
    REGISTRATION_STATE_NOT_REGISTERED = JavaStaticField("I")
    REGISTRATION_STATE_REGISTERED = JavaStaticField("I")
    REGISTRATION_STATE_REGISTERING = JavaStaticField("I")
    getRegistrationState = JavaMethod("(Ljava/util/concurrent/Executor;Ljava/util/function/Consumer;)V")
    getRegistrationTransportType = JavaMethod("(Ljava/util/concurrent/Executor;Ljava/util/function/Consumer;)V")
    registerImsRegistrationCallback = JavaMethod("(Ljava/util/concurrent/Executor;Landroid/telephony/ims/RegistrationManager$RegistrationCallback;)V")
    unregisterImsRegistrationCallback = JavaMethod("(Landroid/telephony/ims/RegistrationManager$RegistrationCallback;)V")

    class RegistrationCallback(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/telephony/ims/RegistrationManager$RegistrationCallback"
        __javaconstructor__ = [("()V", False)]
        onRegistering = JavaMultipleMethod([("(I)V", False, False), ("(Landroid/telephony/ims/ImsRegistrationAttributes;)V", False, False)])
        onTechnologyChangeFailed = JavaMethod("(ILandroid/telephony/ims/ImsReasonInfo;)V")
        onUnregistered = JavaMethod("(Landroid/telephony/ims/ImsReasonInfo;)V")
        onRegistered = JavaMultipleMethod([("(I)V", False, False), ("(Landroid/telephony/ims/ImsRegistrationAttributes;)V", False, False)])