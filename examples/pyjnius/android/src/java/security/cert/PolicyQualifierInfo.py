from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["PolicyQualifierInfo"]

class PolicyQualifierInfo(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/security/cert/PolicyQualifierInfo"
    __javaconstructor__ = [("([B)V", False)]
    toString = JavaMethod("()Ljava/lang/String;")
    getEncoded = JavaMethod("()[B")
    getPolicyQualifierId = JavaMethod("()Ljava/lang/String;")
    getPolicyQualifier = JavaMethod("()[B")