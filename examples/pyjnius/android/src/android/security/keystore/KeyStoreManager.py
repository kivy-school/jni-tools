from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["KeyStoreManager"]

class KeyStoreManager(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/security/keystore/KeyStoreManager"
    MODULE_HASH = JavaStaticField("I")
    getGrantedCertificateChainFromId = JavaMethod("(J)Ljava/util/List;")
    getGrantedKeyFromId = JavaMethod("(J)Ljava/security/Key;")
    getGrantedKeyPairFromId = JavaMethod("(J)Ljava/security/KeyPair;")
    getSupplementaryAttestationInfo = JavaMethod("(I)[B")
    grantKeyAccess = JavaMethod("(Ljava/lang/String;I)J")
    revokeKeyAccess = JavaMethod("(Ljava/lang/String;I)V")