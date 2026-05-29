from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["SubjectDomainCombiner"]

class SubjectDomainCombiner(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "javax/security/auth/SubjectDomainCombiner"
    __javaconstructor__ = [("(Ljavax/security/auth/Subject;)V", False)]
    getSubject = JavaMethod("()Ljavax/security/auth/Subject;")
    combine = JavaMethod("([Ljava/security/ProtectionDomain;[Ljava/security/ProtectionDomain;)[Ljava/security/ProtectionDomain;")