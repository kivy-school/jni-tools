from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["PolicyNode"]

class PolicyNode(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "java/security/cert/PolicyNode"
    getParent = JavaMethod("()Ljava/security/cert/PolicyNode;")
    getChildren = JavaMethod("()Ljava/util/Iterator;")
    getDepth = JavaMethod("()I")
    getValidPolicy = JavaMethod("()Ljava/lang/String;")
    getPolicyQualifiers = JavaMethod("()Ljava/util/Set;")
    getExpectedPolicies = JavaMethod("()Ljava/util/Set;")
    isCritical = JavaMethod("()Z")