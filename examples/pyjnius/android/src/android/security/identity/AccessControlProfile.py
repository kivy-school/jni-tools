from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["AccessControlProfile"]

class AccessControlProfile(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/security/identity/AccessControlProfile"

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/security/identity/AccessControlProfile$Builder"
        __javaconstructor__ = [("(Landroid/security/identity/AccessControlProfileId;)V", False)]
        setUserAuthenticationRequired = JavaMethod("(Z)Landroid/security/identity/AccessControlProfile$Builder;")
        setReaderCertificate = JavaMethod("(Ljava/security/cert/X509Certificate;)Landroid/security/identity/AccessControlProfile$Builder;")
        setUserAuthenticationTimeout = JavaMethod("(J)Landroid/security/identity/AccessControlProfile$Builder;")
        build = JavaMethod("()Landroid/security/identity/AccessControlProfile;")