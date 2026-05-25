from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Owner"]

class Owner(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "java/security/acl/Owner"
    addOwner = JavaMethod("(Ljava/security/Principal;Ljava/security/Principal;)Z")
    deleteOwner = JavaMethod("(Ljava/security/Principal;Ljava/security/Principal;)Z")
    isOwner = JavaMethod("(Ljava/security/Principal;)Z")