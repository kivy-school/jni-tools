from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["CertificateParsingException"]

class CertificateParsingException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "javax/security/cert/CertificateParsingException"
    __javaconstructor__ = [("()V", False), ("(Ljava/lang/String;)V", False)]