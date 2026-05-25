from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["PKIXBuilderParameters"]

class PKIXBuilderParameters(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/security/cert/PKIXBuilderParameters"
    __javaconstructor__ = [("(Ljava/util/Set;Ljava/security/cert/CertSelector;)V", False), ("(Ljava/security/KeyStore;Ljava/security/cert/CertSelector;)V", False)]
    setMaxPathLength = JavaMethod("(I)V")
    getMaxPathLength = JavaMethod("()I")
    toString = JavaMethod("()Ljava/lang/String;")