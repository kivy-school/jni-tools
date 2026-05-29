from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["AclEntryType"]

class AclEntryType(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/nio/file/attribute/AclEntryType"
    ALLOW = JavaStaticField("Ljava/nio/file/attribute/AclEntryType;")
    DENY = JavaStaticField("Ljava/nio/file/attribute/AclEntryType;")
    AUDIT = JavaStaticField("Ljava/nio/file/attribute/AclEntryType;")
    ALARM = JavaStaticField("Ljava/nio/file/attribute/AclEntryType;")
    values = JavaStaticMethod("()[Ljava/nio/file/attribute/AclEntryType;")
    valueOf = JavaStaticMethod("(Ljava/lang/String;)Ljava/nio/file/attribute/AclEntryType;")
    ALLOW = JavaStaticField("Ljava/nio/file/attribute/AclEntryType;")
    DENY = JavaStaticField("Ljava/nio/file/attribute/AclEntryType;")
    AUDIT = JavaStaticField("Ljava/nio/file/attribute/AclEntryType;")
    ALARM = JavaStaticField("Ljava/nio/file/attribute/AclEntryType;")