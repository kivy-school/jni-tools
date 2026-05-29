from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["CertStoreException"]

class CertStoreException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/security/cert/CertStoreException"
    __javaconstructor__ = [("(Ljava/lang/String;Ljava/lang/Throwable;)V", False), ("(Ljava/lang/Throwable;)V", False), ("(Ljava/lang/String;)V", False), ("()V", False)]