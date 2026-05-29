from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["RegistrationManager"]

class RegistrationManager(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "android/telephony/ims/RegistrationManager"
    REGISTRATION_STATE_NOT_REGISTERED = JavaStaticField("I")
    REGISTRATION_STATE_REGISTERED = JavaStaticField("I")
    REGISTRATION_STATE_REGISTERING = JavaStaticField("I")
    registerImsRegistrationCallback = JavaMethod("(Ljava/util/concurrent/Executor;Landroid/telephony/ims/RegistrationManager$RegistrationCallback;)V")
    unregisterImsRegistrationCallback = JavaMethod("(Landroid/telephony/ims/RegistrationManager$RegistrationCallback;)V")
    getRegistrationState = JavaMethod("(Ljava/util/concurrent/Executor;Ljava/util/function/Consumer;)V")
    getRegistrationTransportType = JavaMethod("(Ljava/util/concurrent/Executor;Ljava/util/function/Consumer;)V")

    class RegistrationCallback(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/telephony/ims/RegistrationManager/RegistrationCallback"
        __javaconstructor__ = [("()V", False)]
        onRegistered = JavaMultipleMethod([("(I)V", False, False), ("(Landroid/telephony/ims/ImsRegistrationAttributes;)V", False, False)])
        onRegistering = JavaMultipleMethod([("(I)V", False, False), ("(Landroid/telephony/ims/ImsRegistrationAttributes;)V", False, False)])
        onUnregistered = JavaMethod("(Landroid/telephony/ims/ImsReasonInfo;)V")
        onTechnologyChangeFailed = JavaMethod("(ILandroid/telephony/ims/ImsReasonInfo;)V")