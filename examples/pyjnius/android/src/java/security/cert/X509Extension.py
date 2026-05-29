from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["X509Extension"]

class X509Extension(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/security/cert/X509Extension"
    getExtensionValue = JavaMethod("(Ljava/lang/String;)[B")
    hasUnsupportedCriticalExtension = JavaMethod("()Z")
    getCriticalExtensionOIDs = JavaMethod("()Ljava/util/Set;")
    getNonCriticalExtensionOIDs = JavaMethod("()Ljava/util/Set;")