from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["CertificateExpiredException"]

class CertificateExpiredException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/security/cert/CertificateExpiredException"
    __javaconstructor__ = [("()V", False), ("(Ljava/lang/String;)V", False)]