from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["X509Certificate"]

class X509Certificate(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "javax/security/cert/X509Certificate"
    __javaconstructor__ = [("()V", False)]
    getInstance = JavaMultipleMethod([("([B)Ljavax/security/cert/X509Certificate;", True, False), ("(Ljava/io/InputStream;)Ljavax/security/cert/X509Certificate;", True, False)])
    getSigAlgName = JavaMethod("()Ljava/lang/String;")
    getSigAlgParams = JavaMethod("()[B")
    checkValidity = JavaMultipleMethod([("()V", False, False), ("(Ljava/util/Date;)V", False, False)])
    getSerialNumber = JavaMethod("()Ljava/math/BigInteger;")
    getIssuerDN = JavaMethod("()Ljava/security/Principal;")
    getSubjectDN = JavaMethod("()Ljava/security/Principal;")
    getNotBefore = JavaMethod("()Ljava/util/Date;")
    getNotAfter = JavaMethod("()Ljava/util/Date;")
    getSigAlgOID = JavaMethod("()Ljava/lang/String;")
    getVersion = JavaMethod("()I")