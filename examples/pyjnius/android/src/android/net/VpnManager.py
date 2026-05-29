from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["VpnManager"]

class VpnManager(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/net/VpnManager"
    ACTION_VPN_MANAGER_EVENT = JavaStaticField("Ljava/lang/String;")
    CATEGORY_EVENT_ALWAYS_ON_STATE_CHANGED = JavaStaticField("Ljava/lang/String;")
    CATEGORY_EVENT_DEACTIVATED_BY_USER = JavaStaticField("Ljava/lang/String;")
    CATEGORY_EVENT_IKE_ERROR = JavaStaticField("Ljava/lang/String;")
    CATEGORY_EVENT_NETWORK_ERROR = JavaStaticField("Ljava/lang/String;")
    ERROR_CLASS_NOT_RECOVERABLE = JavaStaticField("I")
    ERROR_CLASS_RECOVERABLE = JavaStaticField("I")
    ERROR_CODE_NETWORK_IO = JavaStaticField("I")
    ERROR_CODE_NETWORK_LOST = JavaStaticField("I")
    ERROR_CODE_NETWORK_PROTOCOL_TIMEOUT = JavaStaticField("I")
    ERROR_CODE_NETWORK_UNKNOWN_HOST = JavaStaticField("I")
    EXTRA_ERROR_CLASS = JavaStaticField("Ljava/lang/String;")
    EXTRA_ERROR_CODE = JavaStaticField("Ljava/lang/String;")
    EXTRA_SESSION_KEY = JavaStaticField("Ljava/lang/String;")
    EXTRA_TIMESTAMP_MILLIS = JavaStaticField("Ljava/lang/String;")
    EXTRA_UNDERLYING_LINK_PROPERTIES = JavaStaticField("Ljava/lang/String;")
    EXTRA_UNDERLYING_NETWORK = JavaStaticField("Ljava/lang/String;")
    EXTRA_UNDERLYING_NETWORK_CAPABILITIES = JavaStaticField("Ljava/lang/String;")
    EXTRA_VPN_PROFILE_STATE = JavaStaticField("Ljava/lang/String;")
    provisionVpnProfile = JavaMethod("(Landroid/net/PlatformVpnProfile;)Landroid/content/Intent;")
    deleteProvisionedVpnProfile = JavaMethod("()V")
    startProvisionedVpnProfileSession = JavaMethod("()Ljava/lang/String;")
    startProvisionedVpnProfile = JavaMethod("()V")
    stopProvisionedVpnProfile = JavaMethod("()V")
    getProvisionedVpnProfileState = JavaMethod("()Landroid/net/VpnProfileState;")