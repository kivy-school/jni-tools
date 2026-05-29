from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["FileIntegrityManager"]

class FileIntegrityManager(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/security/FileIntegrityManager"
    isApkVeritySupported = JavaMethod("()Z")
    isAppSourceCertificateTrusted = JavaMethod("(Ljava/security/cert/X509Certificate;)Z")