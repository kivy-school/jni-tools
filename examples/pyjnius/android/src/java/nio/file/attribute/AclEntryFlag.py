from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["AclEntryFlag"]

class AclEntryFlag(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/nio/file/attribute/AclEntryFlag"
    FILE_INHERIT = JavaStaticField("Ljava/nio/file/attribute/AclEntryFlag;")
    DIRECTORY_INHERIT = JavaStaticField("Ljava/nio/file/attribute/AclEntryFlag;")
    NO_PROPAGATE_INHERIT = JavaStaticField("Ljava/nio/file/attribute/AclEntryFlag;")
    INHERIT_ONLY = JavaStaticField("Ljava/nio/file/attribute/AclEntryFlag;")
    values = JavaStaticMethod("()[Ljava/nio/file/attribute/AclEntryFlag;")
    valueOf = JavaStaticMethod("(Ljava/lang/String;)Ljava/nio/file/attribute/AclEntryFlag;")
    FILE_INHERIT = JavaStaticField("Ljava/nio/file/attribute/AclEntryFlag;")
    DIRECTORY_INHERIT = JavaStaticField("Ljava/nio/file/attribute/AclEntryFlag;")
    NO_PROPAGATE_INHERIT = JavaStaticField("Ljava/nio/file/attribute/AclEntryFlag;")
    INHERIT_ONLY = JavaStaticField("Ljava/nio/file/attribute/AclEntryFlag;")