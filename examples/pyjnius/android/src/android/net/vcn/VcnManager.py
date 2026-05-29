from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["VcnManager"]

class VcnManager(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/net/vcn/VcnManager"
    VCN_ERROR_CODE_CONFIG_ERROR = JavaStaticField("I")
    VCN_ERROR_CODE_INTERNAL_ERROR = JavaStaticField("I")
    VCN_ERROR_CODE_NETWORK_ERROR = JavaStaticField("I")
    VCN_STATUS_CODE_ACTIVE = JavaStaticField("I")
    VCN_STATUS_CODE_INACTIVE = JavaStaticField("I")
    VCN_STATUS_CODE_NOT_CONFIGURED = JavaStaticField("I")
    VCN_STATUS_CODE_SAFE_MODE = JavaStaticField("I")
    clearVcnConfig = JavaMethod("(Landroid/os/ParcelUuid;)V")
    setVcnConfig = JavaMethod("(Landroid/os/ParcelUuid;Landroid/net/vcn/VcnConfig;)V")
    getConfiguredSubscriptionGroups = JavaMethod("()Ljava/util/List;")
    registerVcnStatusCallback = JavaMethod("(Landroid/os/ParcelUuid;Ljava/util/concurrent/Executor;Landroid/net/vcn/VcnManager$VcnStatusCallback;)V")
    unregisterVcnStatusCallback = JavaMethod("(Landroid/net/vcn/VcnManager$VcnStatusCallback;)V")

    class VcnStatusCallback(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/net/vcn/VcnManager$VcnStatusCallback"
        __javaconstructor__ = [("()V", False)]
        onStatusChanged = JavaMethod("(I)V")
        onGatewayConnectionError = JavaMethod("(Ljava/lang/String;ILjava/lang/Throwable;)V")