from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ImsRcsManager"]

class ImsRcsManager(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/telephony/ims/ImsRcsManager"
    ACTION_SHOW_CAPABILITY_DISCOVERY_OPT_IN = JavaStaticField("Ljava/lang/String;")
    CAPABILITY_TYPE_NONE = JavaStaticField("I")
    CAPABILITY_TYPE_OPTIONS_UCE = JavaStaticField("I")
    CAPABILITY_TYPE_PRESENCE_UCE = JavaStaticField("I")
    getUceAdapter = JavaMethod("()Landroid/telephony/ims/RcsUceAdapter;")
    getRegistrationState = JavaMethod("(Ljava/util/concurrent/Executor;Ljava/util/function/Consumer;)V")
    getRegistrationTransportType = JavaMethod("(Ljava/util/concurrent/Executor;Ljava/util/function/Consumer;)V")
    registerImsRegistrationCallback = JavaMethod("(Ljava/util/concurrent/Executor;Landroid/telephony/ims/RegistrationManager$RegistrationCallback;)V")
    registerImsStateCallback = JavaMethod("(Ljava/util/concurrent/Executor;Landroid/telephony/ims/ImsStateCallback;)V")
    unregisterImsRegistrationCallback = JavaMethod("(Landroid/telephony/ims/RegistrationManager$RegistrationCallback;)V")
    unregisterImsStateCallback = JavaMethod("(Landroid/telephony/ims/ImsStateCallback;)V")