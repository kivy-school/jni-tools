from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ImsMmTelManager"]

class ImsMmTelManager(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/telephony/ims/ImsMmTelManager"
    WIFI_MODE_CELLULAR_PREFERRED = JavaStaticField("I")
    WIFI_MODE_WIFI_ONLY = JavaStaticField("I")
    WIFI_MODE_WIFI_PREFERRED = JavaStaticField("I")
    registerImsRegistrationCallback = JavaMethod("(Ljava/util/concurrent/Executor;Landroid/telephony/ims/RegistrationManager$RegistrationCallback;)V")
    unregisterImsRegistrationCallback = JavaMethod("(Landroid/telephony/ims/RegistrationManager$RegistrationCallback;)V")
    getRegistrationState = JavaMethod("(Ljava/util/concurrent/Executor;Ljava/util/function/Consumer;)V")
    getRegistrationTransportType = JavaMethod("(Ljava/util/concurrent/Executor;Ljava/util/function/Consumer;)V")
    registerMmTelCapabilityCallback = JavaMethod("(Ljava/util/concurrent/Executor;Landroid/telephony/ims/ImsMmTelManager$CapabilityCallback;)V")
    unregisterMmTelCapabilityCallback = JavaMethod("(Landroid/telephony/ims/ImsMmTelManager$CapabilityCallback;)V")
    isAdvancedCallingSettingEnabled = JavaMethod("()Z")
    isVtSettingEnabled = JavaMethod("()Z")
    isVoWiFiSettingEnabled = JavaMethod("()Z")
    isCrossSimCallingEnabled = JavaMethod("()Z")
    isVoWiFiRoamingSettingEnabled = JavaMethod("()Z")
    getVoWiFiModeSetting = JavaMethod("()I")
    isTtyOverVolteEnabled = JavaMethod("()Z")
    registerImsStateCallback = JavaMethod("(Ljava/util/concurrent/Executor;Landroid/telephony/ims/ImsStateCallback;)V")
    unregisterImsStateCallback = JavaMethod("(Landroid/telephony/ims/ImsStateCallback;)V")

    class CapabilityCallback(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/telephony/ims/ImsMmTelManager/CapabilityCallback"
        __javaconstructor__ = [("()V", False)]
        onCapabilitiesStatusChanged = JavaMethod("(Landroid/telephony/ims/feature/MmTelFeature$MmTelCapabilities;)V")