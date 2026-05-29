from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ProvisioningManager"]

class ProvisioningManager(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/telephony/ims/ProvisioningManager"
    getRcsProvisioningStatusForCapability = JavaMethod("(II)Z")
    isProvisioningRequiredForCapability = JavaMethod("(II)Z")
    isRcsProvisioningRequiredForCapability = JavaMethod("(II)Z")
    registerFeatureProvisioningChangedCallback = JavaMethod("(Ljava/util/concurrent/Executor;Landroid/telephony/ims/ProvisioningManager$FeatureProvisioningCallback;)V")
    getProvisioningStatusForCapability = JavaMethod("(II)Z")
    setProvisioningStatusForCapability = JavaMethod("(IIZ)V")
    setRcsProvisioningStatusForCapability = JavaMethod("(IIZ)V")
    unregisterFeatureProvisioningChangedCallback = JavaMethod("(Landroid/telephony/ims/ProvisioningManager$FeatureProvisioningCallback;)V")

    class FeatureProvisioningCallback(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/telephony/ims/ProvisioningManager$FeatureProvisioningCallback"
        __javaconstructor__ = [("()V", False)]
        onFeatureProvisioningChanged = JavaMethod("(IIZ)V")
        onRcsFeatureProvisioningChanged = JavaMethod("(IIZ)V")