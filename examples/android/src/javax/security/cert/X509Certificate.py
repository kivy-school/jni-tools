from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["X509Certificate"]

class X509Certificate(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "javax/security/cert/X509Certificate"
    __javaconstructor__ = [("()V", False)]
    getInstance = JavaMultipleMethod([("(Ljava/io/InputStream;)Ljavax/security/cert/X509Certificate;", True, False), ("([B)Ljavax/security/cert/X509Certificate;", True, False)])
    checkValidity = JavaMultipleMethod([("()V", False, False), ("(Ljava/util/Date;)V", False, False)])
    getVersion = JavaMethod("()I")
    getSerialNumber = JavaMethod("()Ljava/math/BigInteger;")
    getIssuerDN = JavaMethod("()Ljava/security/Principal;")
    getSubjectDN = JavaMethod("()Ljava/security/Principal;")
    getNotBefore = JavaMethod("()Ljava/util/Date;")
    getNotAfter = JavaMethod("()Ljava/util/Date;")
    getSigAlgName = JavaMethod("()Ljava/lang/String;")
    getSigAlgOID = JavaMethod("()Ljava/lang/String;")
    getSigAlgParams = JavaMethod("()[B")