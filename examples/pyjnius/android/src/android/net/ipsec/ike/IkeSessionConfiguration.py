from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["IkeSessionConfiguration"]

class IkeSessionConfiguration(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/net/ipsec/ike/IkeSessionConfiguration"
    EXTENSION_TYPE_FRAGMENTATION = JavaStaticField("I")
    EXTENSION_TYPE_MOBIKE = JavaStaticField("I")
    getRemoteVendorIds = JavaMethod("()Ljava/util/List;")
    getEapInfo = JavaMethod("()Landroid/net/eap/EapInfo;")
    getIkeSessionConnectionInfo = JavaMethod("()Landroid/net/ipsec/ike/IkeSessionConnectionInfo;")
    getRemoteApplicationVersion = JavaMethod("()Ljava/lang/String;")
    isIkeExtensionEnabled = JavaMethod("(I)Z")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/net/ipsec/ike/IkeSessionConfiguration$Builder"
        __javaconstructor__ = [("(Landroid/net/ipsec/ike/IkeSessionConnectionInfo;)V", False)]
        clearIkeExtensions = JavaMethod("()Landroid/net/ipsec/ike/IkeSessionConfiguration$Builder;")
        addRemoteVendorId = JavaMethod("([B)Landroid/net/ipsec/ike/IkeSessionConfiguration$Builder;")
        addIkeExtension = JavaMethod("(I)Landroid/net/ipsec/ike/IkeSessionConfiguration$Builder;")
        setEapInfo = JavaMethod("(Landroid/net/eap/EapInfo;)Landroid/net/ipsec/ike/IkeSessionConfiguration$Builder;")
        clearRemoteApplicationVersion = JavaMethod("()Landroid/net/ipsec/ike/IkeSessionConfiguration$Builder;")
        clearRemoteVendorIds = JavaMethod("()Landroid/net/ipsec/ike/IkeSessionConfiguration$Builder;")
        setRemoteApplicationVersion = JavaMethod("(Ljava/lang/String;)Landroid/net/ipsec/ike/IkeSessionConfiguration$Builder;")
        build = JavaMethod("()Landroid/net/ipsec/ike/IkeSessionConfiguration;")