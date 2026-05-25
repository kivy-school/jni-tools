from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ProvisioningManager"]

class ProvisioningManager(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/telephony/ims/ProvisioningManager"
    registerFeatureProvisioningChangedCallback = JavaMethod("(Ljava/util/concurrent/Executor;Landroid/telephony/ims/ProvisioningManager$FeatureProvisioningCallback;)V")
    unregisterFeatureProvisioningChangedCallback = JavaMethod("(Landroid/telephony/ims/ProvisioningManager$FeatureProvisioningCallback;)V")
    setProvisioningStatusForCapability = JavaMethod("(IIZ)V")
    getProvisioningStatusForCapability = JavaMethod("(II)Z")
    getRcsProvisioningStatusForCapability = JavaMethod("(II)Z")
    setRcsProvisioningStatusForCapability = JavaMethod("(IIZ)V")
    isProvisioningRequiredForCapability = JavaMethod("(II)Z")
    isRcsProvisioningRequiredForCapability = JavaMethod("(II)Z")

    class FeatureProvisioningCallback(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/telephony/ims/ProvisioningManager/FeatureProvisioningCallback"
        __javaconstructor__ = [("()V", False)]
        onFeatureProvisioningChanged = JavaMethod("(IIZ)V")
        onRcsFeatureProvisioningChanged = JavaMethod("(IIZ)V")