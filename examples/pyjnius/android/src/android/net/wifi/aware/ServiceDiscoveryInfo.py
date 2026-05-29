from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ServiceDiscoveryInfo"]

class ServiceDiscoveryInfo(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/net/wifi/aware/ServiceDiscoveryInfo"
    getPairingConfig = JavaMethod("()Landroid/net/wifi/aware/AwarePairingConfig;")
    getPairedAlias = JavaMethod("()Ljava/lang/String;")
    getPeerCipherSuite = JavaMethod("()I")
    getMatchFilters = JavaMethod("()Ljava/util/List;")
    getPeerHandle = JavaMethod("()Landroid/net/wifi/aware/PeerHandle;")
    getScid = JavaMethod("()[B")
    getServiceSpecificInfo = JavaMethod("()[B")