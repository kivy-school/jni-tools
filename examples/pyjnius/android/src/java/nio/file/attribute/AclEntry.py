from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["AclEntry"]

class AclEntry(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/nio/file/attribute/AclEntry"
    type = JavaMethod("()Ljava/nio/file/attribute/AclEntryType;")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    toString = JavaMethod("()Ljava/lang/String;")
    flags = JavaMethod("()Ljava/util/Set;")
    hashCode = JavaMethod("()I")
    permissions = JavaMethod("()Ljava/util/Set;")
    newBuilder = JavaMultipleMethod([("()Ljava/nio/file/attribute/AclEntry$Builder;", True, False), ("(Ljava/nio/file/attribute/AclEntry;)Ljava/nio/file/attribute/AclEntry$Builder;", True, False)])
    principal = JavaMethod("()Ljava/nio/file/attribute/UserPrincipal;")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "java/nio/file/attribute/AclEntry$Builder"
        setType = JavaMethod("(Ljava/nio/file/attribute/AclEntryType;)Ljava/nio/file/attribute/AclEntry$Builder;")
        setFlags = JavaMultipleMethod([("(Ljava/util/Set;)Ljava/nio/file/attribute/AclEntry$Builder;", False, False), ("([Ljava/nio/file/attribute/AclEntryFlag;)Ljava/nio/file/attribute/AclEntry$Builder;", False, True)])
        build = JavaMethod("()Ljava/nio/file/attribute/AclEntry;")
        setPrincipal = JavaMethod("(Ljava/nio/file/attribute/UserPrincipal;)Ljava/nio/file/attribute/AclEntry$Builder;")
        setPermissions = JavaMultipleMethod([("(Ljava/util/Set;)Ljava/nio/file/attribute/AclEntry$Builder;", False, False), ("([Ljava/nio/file/attribute/AclEntryPermission;)Ljava/nio/file/attribute/AclEntry$Builder;", False, True)])