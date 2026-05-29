from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["PolicyQualifierInfo"]

class PolicyQualifierInfo(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/security/cert/PolicyQualifierInfo"
    __javaconstructor__ = [("([B)V", False)]
    getPolicyQualifierId = JavaMethod("()Ljava/lang/String;")
    getEncoded = JavaMethod("()[B")
    getPolicyQualifier = JavaMethod("()[B")
    toString = JavaMethod("()Ljava/lang/String;")