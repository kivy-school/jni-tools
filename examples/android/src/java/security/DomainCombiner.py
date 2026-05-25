from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["DomainCombiner"]

class DomainCombiner(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "java/security/DomainCombiner"
    combine = JavaMethod("([Ljava/security/ProtectionDomain;[Ljava/security/ProtectionDomain;)[Ljava/security/ProtectionDomain;")