from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ImsMmTelManager"]

class ImsMmTelManager(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/telephony/ims/ImsMmTelManager"
    WIFI_MODE_CELLULAR_PREFERRED = JavaStaticField("I")
    WIFI_MODE_WIFI_ONLY = JavaStaticField("I")
    WIFI_MODE_WIFI_PREFERRED = JavaStaticField("I")
    REGISTRATION_STATE_NOT_REGISTERED = JavaStaticField("I")
    REGISTRATION_STATE_REGISTERED = JavaStaticField("I")
    REGISTRATION_STATE_REGISTERING = JavaStaticField("I")
    isVtSettingEnabled = JavaMethod("()Z")
    getRegistrationState = JavaMethod("(Ljava/util/concurrent/Executor;Ljava/util/function/Consumer;)V")
    getRegistrationTransportType = JavaMethod("(Ljava/util/concurrent/Executor;Ljava/util/function/Consumer;)V")
    getVoWiFiModeSetting = JavaMethod("()I")
    isAdvancedCallingSettingEnabled = JavaMethod("()Z")
    isCrossSimCallingEnabled = JavaMethod("()Z")
    isTtyOverVolteEnabled = JavaMethod("()Z")
    isVoWiFiRoamingSettingEnabled = JavaMethod("()Z")
    isVoWiFiSettingEnabled = JavaMethod("()Z")
    registerImsRegistrationCallback = JavaMethod("(Ljava/util/concurrent/Executor;Landroid/telephony/ims/RegistrationManager$RegistrationCallback;)V")
    registerImsStateCallback = JavaMethod("(Ljava/util/concurrent/Executor;Landroid/telephony/ims/ImsStateCallback;)V")
    registerMmTelCapabilityCallback = JavaMethod("(Ljava/util/concurrent/Executor;Landroid/telephony/ims/ImsMmTelManager$CapabilityCallback;)V")
    unregisterImsRegistrationCallback = JavaMethod("(Landroid/telephony/ims/RegistrationManager$RegistrationCallback;)V")
    unregisterImsStateCallback = JavaMethod("(Landroid/telephony/ims/ImsStateCallback;)V")
    unregisterMmTelCapabilityCallback = JavaMethod("(Landroid/telephony/ims/ImsMmTelManager$CapabilityCallback;)V")

    class CapabilityCallback(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/telephony/ims/ImsMmTelManager$CapabilityCallback"
        __javaconstructor__ = [("()V", False)]
        onCapabilitiesStatusChanged = JavaMethod("(Landroid/telephony/ims/feature/MmTelFeature$MmTelCapabilities;)V")