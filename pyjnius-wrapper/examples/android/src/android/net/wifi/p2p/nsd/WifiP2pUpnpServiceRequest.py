from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["WifiP2pUpnpServiceRequest"]

class WifiP2pUpnpServiceRequest(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/net/wifi/p2p/nsd/WifiP2pUpnpServiceRequest"
    newInstance = JavaMultipleMethod([("()Landroid/net/wifi/p2p/nsd/WifiP2pUpnpServiceRequest;", True, False), ("(Ljava/lang/String;)Landroid/net/wifi/p2p/nsd/WifiP2pUpnpServiceRequest;", True, False)])