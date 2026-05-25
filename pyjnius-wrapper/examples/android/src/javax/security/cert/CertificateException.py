from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["CertificateException"]

class CertificateException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "javax/security/cert/CertificateException"
    __javaconstructor__ = [("()V", False), ("(Ljava/lang/String;)V", False)]