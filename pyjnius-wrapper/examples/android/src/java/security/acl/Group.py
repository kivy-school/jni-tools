from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Group"]

class Group(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "java/security/acl/Group"
    addMember = JavaMethod("(Ljava/security/Principal;)Z")
    removeMember = JavaMethod("(Ljava/security/Principal;)Z")
    isMember = JavaMethod("(Ljava/security/Principal;)Z")
    members = JavaMethod("()Ljava/util/Enumeration;")