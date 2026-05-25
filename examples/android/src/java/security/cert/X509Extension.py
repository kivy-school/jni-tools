from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["X509Extension"]

class X509Extension(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "java/security/cert/X509Extension"
    hasUnsupportedCriticalExtension = JavaMethod("()Z")
    getCriticalExtensionOIDs = JavaMethod("()Ljava/util/Set;")
    getNonCriticalExtensionOIDs = JavaMethod("()Ljava/util/Set;")
    getExtensionValue = JavaMethod("(Ljava/lang/String;)[B")