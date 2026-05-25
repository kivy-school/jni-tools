from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["UserPrincipalLookupService"]

class UserPrincipalLookupService(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/nio/file/attribute/UserPrincipalLookupService"
    __javaconstructor__ = [("()V", False)]
    lookupPrincipalByName = JavaMethod("(Ljava/lang/String;)Ljava/nio/file/attribute/UserPrincipal;")
    lookupPrincipalByGroupName = JavaMethod("(Ljava/lang/String;)Ljava/nio/file/attribute/GroupPrincipal;")