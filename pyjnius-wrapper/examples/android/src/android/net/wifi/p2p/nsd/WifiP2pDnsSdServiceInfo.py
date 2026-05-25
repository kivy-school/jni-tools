from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["WifiP2pDnsSdServiceInfo"]

class WifiP2pDnsSdServiceInfo(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/net/wifi/p2p/nsd/WifiP2pDnsSdServiceInfo"
    newInstance = JavaStaticMethod("(Ljava/lang/String;Ljava/lang/String;Ljava/util/Map;)Landroid/net/wifi/p2p/nsd/WifiP2pDnsSdServiceInfo;")