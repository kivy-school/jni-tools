from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["WifiP2pDnsSdServiceInfo"]

class WifiP2pDnsSdServiceInfo(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/net/wifi/p2p/nsd/WifiP2pDnsSdServiceInfo"
    SERVICE_TYPE_ALL = JavaStaticField("I")
    SERVICE_TYPE_BONJOUR = JavaStaticField("I")
    SERVICE_TYPE_UPNP = JavaStaticField("I")
    SERVICE_TYPE_VENDOR_SPECIFIC = JavaStaticField("I")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    newInstance = JavaStaticMethod("(Ljava/lang/String;Ljava/lang/String;Ljava/util/Map;)Landroid/net/wifi/p2p/nsd/WifiP2pDnsSdServiceInfo;")