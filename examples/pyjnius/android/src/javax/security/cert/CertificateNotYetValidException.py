from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["CertificateNotYetValidException"]

class CertificateNotYetValidException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "javax/security/cert/CertificateNotYetValidException"
    __javaconstructor__ = [("()V", False), ("(Ljava/lang/String;)V", False)]