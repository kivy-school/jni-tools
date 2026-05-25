from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["WifiP2pDnsSdServiceRequest"]

class WifiP2pDnsSdServiceRequest(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/net/wifi/p2p/nsd/WifiP2pDnsSdServiceRequest"
    newInstance = JavaMultipleMethod([("()Landroid/net/wifi/p2p/nsd/WifiP2pDnsSdServiceRequest;", True, False), ("(Ljava/lang/String;)Landroid/net/wifi/p2p/nsd/WifiP2pDnsSdServiceRequest;", True, False), ("(Ljava/lang/String;Ljava/lang/String;)Landroid/net/wifi/p2p/nsd/WifiP2pDnsSdServiceRequest;", True, False)])