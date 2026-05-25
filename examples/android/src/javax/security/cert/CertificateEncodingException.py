from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["CertificateEncodingException"]

class CertificateEncodingException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "javax/security/cert/CertificateEncodingException"
    __javaconstructor__ = [("()V", False), ("(Ljava/lang/String;)V", False)]