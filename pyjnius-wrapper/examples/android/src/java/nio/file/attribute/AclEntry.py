from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["AclEntry"]

class AclEntry(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/nio/file/attribute/AclEntry"
    newBuilder = JavaMultipleMethod([("()Ljava/nio/file/attribute/AclEntry$Builder;", True, False), ("(Ljava/nio/file/attribute/AclEntry;)Ljava/nio/file/attribute/AclEntry$Builder;", True, False)])
    type = JavaMethod("()Ljava/nio/file/attribute/AclEntryType;")
    principal = JavaMethod("()Ljava/nio/file/attribute/UserPrincipal;")
    permissions = JavaMethod("()Ljava/util/Set;")
    flags = JavaMethod("()Ljava/util/Set;")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")
    toString = JavaMethod("()Ljava/lang/String;")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "java/nio/file/attribute/AclEntry/Builder"
        build = JavaMethod("()Ljava/nio/file/attribute/AclEntry;")
        setType = JavaMethod("(Ljava/nio/file/attribute/AclEntryType;)Ljava/nio/file/attribute/AclEntry$Builder;")
        setPrincipal = JavaMethod("(Ljava/nio/file/attribute/UserPrincipal;)Ljava/nio/file/attribute/AclEntry$Builder;")
        setPermissions = JavaMultipleMethod([("(Ljava/util/Set;)Ljava/nio/file/attribute/AclEntry$Builder;", False, False), ("([Ljava/nio/file/attribute/AclEntryPermission;)Ljava/nio/file/attribute/AclEntry$Builder;", False, True)])
        setFlags = JavaMultipleMethod([("(Ljava/util/Set;)Ljava/nio/file/attribute/AclEntry$Builder;", False, False), ("([Ljava/nio/file/attribute/AclEntryFlag;)Ljava/nio/file/attribute/AclEntry$Builder;", False, True)])