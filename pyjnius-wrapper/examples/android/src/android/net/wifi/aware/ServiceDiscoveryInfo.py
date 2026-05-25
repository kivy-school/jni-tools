from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ServiceDiscoveryInfo"]

class ServiceDiscoveryInfo(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/net/wifi/aware/ServiceDiscoveryInfo"
    getPeerHandle = JavaMethod("()Landroid/net/wifi/aware/PeerHandle;")
    getMatchFilters = JavaMethod("()Ljava/util/List;")
    getServiceSpecificInfo = JavaMethod("()[B")
    getScid = JavaMethod("()[B")
    getPeerCipherSuite = JavaMethod("()I")
    getPairedAlias = JavaMethod("()Ljava/lang/String;")
    getPairingConfig = JavaMethod("()Landroid/net/wifi/aware/AwarePairingConfig;")