from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["PlatformVpnProfile"]

class PlatformVpnProfile(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/net/PlatformVpnProfile"
    TYPE_IKEV2_IPSEC_PSK = JavaStaticField("I")
    TYPE_IKEV2_IPSEC_RSA = JavaStaticField("I")
    TYPE_IKEV2_IPSEC_USER_PASS = JavaStaticField("I")
    areLocalRoutesExcluded = JavaMethod("()Z")
    isInternetValidationRequired = JavaMethod("()Z")
    getType = JavaMethod("()I")
    getTypeString = JavaMethod("()Ljava/lang/String;")