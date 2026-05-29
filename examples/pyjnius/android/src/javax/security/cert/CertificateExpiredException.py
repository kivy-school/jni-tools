from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["CertificateExpiredException"]

class CertificateExpiredException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "javax/security/cert/CertificateExpiredException"
    __javaconstructor__ = [("()V", False), ("(Ljava/lang/String;)V", False)]