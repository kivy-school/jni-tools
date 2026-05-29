from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["PolicyNode"]

class PolicyNode(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/security/cert/PolicyNode"
    getChildren = JavaMethod("()Ljava/util/Iterator;")
    getParent = JavaMethod("()Ljava/security/cert/PolicyNode;")
    getDepth = JavaMethod("()I")
    isCritical = JavaMethod("()Z")
    getValidPolicy = JavaMethod("()Ljava/lang/String;")
    getPolicyQualifiers = JavaMethod("()Ljava/util/Set;")
    getExpectedPolicies = JavaMethod("()Ljava/util/Set;")