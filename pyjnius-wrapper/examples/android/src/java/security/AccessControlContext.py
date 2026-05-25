from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["AccessControlContext"]

class AccessControlContext(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/security/AccessControlContext"
    __javaconstructor__ = [("([Ljava/security/ProtectionDomain;)V", False), ("(Ljava/security/AccessControlContext;Ljava/security/DomainCombiner;)V", False)]
    getDomainCombiner = JavaMethod("()Ljava/security/DomainCombiner;")
    checkPermission = JavaMethod("(Ljava/security/Permission;)V")