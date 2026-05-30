from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

class GroupPrincipal(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/nio/file/attribute/GroupPrincipal"

class PosixFileAttributeView(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/nio/file/attribute/PosixFileAttributeView"
    setGroup = JavaMethod("(Ljava/nio/file/attribute/GroupPrincipal;)V")
    setPermissions = JavaMethod("(Ljava/util/Set;)V")
    name = JavaMethod("()Ljava/lang/String;")
    readAttributes = JavaMultipleMethod([("()Ljava/nio/file/attribute/PosixFileAttributes;", False, False), ("()Ljava/nio/file/attribute/BasicFileAttributes;", False, False)])

class FileAttribute(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/nio/file/attribute/FileAttribute"
    name = JavaMethod("()Ljava/lang/String;")
    value = JavaMethod("()Ljava/lang/Object;")

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

class AclEntry(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/nio/file/attribute/AclEntry"
    type = JavaMethod("()Ljava/nio/file/attribute/AclEntryType;")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    toString = JavaMethod("()Ljava/lang/String;")
    flags = JavaMethod("()Ljava/util/Set;")
    hashCode = JavaMethod("()I")
    permissions = JavaMethod("()Ljava/util/Set;")
    principal = JavaMethod("()Ljava/nio/file/attribute/UserPrincipal;")
    newBuilder = JavaMultipleMethod([("(Ljava/nio/file/attribute/AclEntry;)Ljava/nio/file/attribute/AclEntry$Builder;", True, False), ("()Ljava/nio/file/attribute/AclEntry$Builder;", True, False)])

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "java/nio/file/attribute/AclEntry$Builder"
        setPermissions = JavaMultipleMethod([("(Ljava/util/Set;)Ljava/nio/file/attribute/AclEntry$Builder;", False, False), ("([Ljava/nio/file/attribute/AclEntryPermission;)Ljava/nio/file/attribute/AclEntry$Builder;", False, True)])
        setFlags = JavaMultipleMethod([("(Ljava/util/Set;)Ljava/nio/file/attribute/AclEntry$Builder;", False, False), ("([Ljava/nio/file/attribute/AclEntryFlag;)Ljava/nio/file/attribute/AclEntry$Builder;", False, True)])
        setType = JavaMethod("(Ljava/nio/file/attribute/AclEntryType;)Ljava/nio/file/attribute/AclEntry$Builder;")
        build = JavaMethod("()Ljava/nio/file/attribute/AclEntry;")
        setPrincipal = JavaMethod("(Ljava/nio/file/attribute/UserPrincipal;)Ljava/nio/file/attribute/AclEntry$Builder;")

class FileOwnerAttributeView(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/nio/file/attribute/FileOwnerAttributeView"
    setOwner = JavaMethod("(Ljava/nio/file/attribute/UserPrincipal;)V")
    name = JavaMethod("()Ljava/lang/String;")
    getOwner = JavaMethod("()Ljava/nio/file/attribute/UserPrincipal;")

class UserPrincipal(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/nio/file/attribute/UserPrincipal"

class PosixFilePermissions(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/nio/file/attribute/PosixFilePermissions"
    toString = JavaStaticMethod("(Ljava/util/Set;)Ljava/lang/String;")
    fromString = JavaStaticMethod("(Ljava/lang/String;)Ljava/util/Set;")
    asFileAttribute = JavaStaticMethod("(Ljava/util/Set;)Ljava/nio/file/attribute/FileAttribute;")

class UserDefinedFileAttributeView(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/nio/file/attribute/UserDefinedFileAttributeView"
    name = JavaMethod("()Ljava/lang/String;")
    size = JavaMethod("(Ljava/lang/String;)I")
    list = JavaMethod("()Ljava/util/List;")
    write = JavaMethod("(Ljava/lang/String;Ljava/nio/ByteBuffer;)I")
    read = JavaMethod("(Ljava/lang/String;Ljava/nio/ByteBuffer;)I")
    delete = JavaMethod("(Ljava/lang/String;)V")

class PosixFilePermission(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/nio/file/attribute/PosixFilePermission"
    OWNER_READ = JavaStaticField("Ljava/nio/file/attribute/PosixFilePermission;")
    OWNER_WRITE = JavaStaticField("Ljava/nio/file/attribute/PosixFilePermission;")
    OWNER_EXECUTE = JavaStaticField("Ljava/nio/file/attribute/PosixFilePermission;")
    GROUP_READ = JavaStaticField("Ljava/nio/file/attribute/PosixFilePermission;")
    GROUP_WRITE = JavaStaticField("Ljava/nio/file/attribute/PosixFilePermission;")
    GROUP_EXECUTE = JavaStaticField("Ljava/nio/file/attribute/PosixFilePermission;")
    OTHERS_READ = JavaStaticField("Ljava/nio/file/attribute/PosixFilePermission;")
    OTHERS_WRITE = JavaStaticField("Ljava/nio/file/attribute/PosixFilePermission;")
    OTHERS_EXECUTE = JavaStaticField("Ljava/nio/file/attribute/PosixFilePermission;")
    values = JavaStaticMethod("()[Ljava/nio/file/attribute/PosixFilePermission;")
    valueOf = JavaStaticMethod("(Ljava/lang/String;)Ljava/nio/file/attribute/PosixFilePermission;")
    OWNER_READ = JavaStaticField("Ljava/nio/file/attribute/PosixFilePermission;")
    OWNER_WRITE = JavaStaticField("Ljava/nio/file/attribute/PosixFilePermission;")
    OWNER_EXECUTE = JavaStaticField("Ljava/nio/file/attribute/PosixFilePermission;")
    GROUP_READ = JavaStaticField("Ljava/nio/file/attribute/PosixFilePermission;")
    GROUP_WRITE = JavaStaticField("Ljava/nio/file/attribute/PosixFilePermission;")
    GROUP_EXECUTE = JavaStaticField("Ljava/nio/file/attribute/PosixFilePermission;")
    OTHERS_READ = JavaStaticField("Ljava/nio/file/attribute/PosixFilePermission;")
    OTHERS_WRITE = JavaStaticField("Ljava/nio/file/attribute/PosixFilePermission;")
    OTHERS_EXECUTE = JavaStaticField("Ljava/nio/file/attribute/PosixFilePermission;")

class BasicFileAttributeView(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/nio/file/attribute/BasicFileAttributeView"
    setTimes = JavaMethod("(Ljava/nio/file/attribute/FileTime;Ljava/nio/file/attribute/FileTime;Ljava/nio/file/attribute/FileTime;)V")
    name = JavaMethod("()Ljava/lang/String;")
    readAttributes = JavaMethod("()Ljava/nio/file/attribute/BasicFileAttributes;")

class AclEntryPermission(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/nio/file/attribute/AclEntryPermission"
    READ_DATA = JavaStaticField("Ljava/nio/file/attribute/AclEntryPermission;")
    WRITE_DATA = JavaStaticField("Ljava/nio/file/attribute/AclEntryPermission;")
    APPEND_DATA = JavaStaticField("Ljava/nio/file/attribute/AclEntryPermission;")
    READ_NAMED_ATTRS = JavaStaticField("Ljava/nio/file/attribute/AclEntryPermission;")
    WRITE_NAMED_ATTRS = JavaStaticField("Ljava/nio/file/attribute/AclEntryPermission;")
    EXECUTE = JavaStaticField("Ljava/nio/file/attribute/AclEntryPermission;")
    DELETE_CHILD = JavaStaticField("Ljava/nio/file/attribute/AclEntryPermission;")
    READ_ATTRIBUTES = JavaStaticField("Ljava/nio/file/attribute/AclEntryPermission;")
    WRITE_ATTRIBUTES = JavaStaticField("Ljava/nio/file/attribute/AclEntryPermission;")
    DELETE = JavaStaticField("Ljava/nio/file/attribute/AclEntryPermission;")
    READ_ACL = JavaStaticField("Ljava/nio/file/attribute/AclEntryPermission;")
    WRITE_ACL = JavaStaticField("Ljava/nio/file/attribute/AclEntryPermission;")
    WRITE_OWNER = JavaStaticField("Ljava/nio/file/attribute/AclEntryPermission;")
    SYNCHRONIZE = JavaStaticField("Ljava/nio/file/attribute/AclEntryPermission;")
    LIST_DIRECTORY = JavaStaticField("Ljava/nio/file/attribute/AclEntryPermission;")
    ADD_FILE = JavaStaticField("Ljava/nio/file/attribute/AclEntryPermission;")
    ADD_SUBDIRECTORY = JavaStaticField("Ljava/nio/file/attribute/AclEntryPermission;")
    values = JavaStaticMethod("()[Ljava/nio/file/attribute/AclEntryPermission;")
    valueOf = JavaStaticMethod("(Ljava/lang/String;)Ljava/nio/file/attribute/AclEntryPermission;")
    READ_DATA = JavaStaticField("Ljava/nio/file/attribute/AclEntryPermission;")
    WRITE_DATA = JavaStaticField("Ljava/nio/file/attribute/AclEntryPermission;")
    APPEND_DATA = JavaStaticField("Ljava/nio/file/attribute/AclEntryPermission;")
    READ_NAMED_ATTRS = JavaStaticField("Ljava/nio/file/attribute/AclEntryPermission;")
    WRITE_NAMED_ATTRS = JavaStaticField("Ljava/nio/file/attribute/AclEntryPermission;")
    EXECUTE = JavaStaticField("Ljava/nio/file/attribute/AclEntryPermission;")
    DELETE_CHILD = JavaStaticField("Ljava/nio/file/attribute/AclEntryPermission;")
    READ_ATTRIBUTES = JavaStaticField("Ljava/nio/file/attribute/AclEntryPermission;")
    WRITE_ATTRIBUTES = JavaStaticField("Ljava/nio/file/attribute/AclEntryPermission;")
    DELETE = JavaStaticField("Ljava/nio/file/attribute/AclEntryPermission;")
    READ_ACL = JavaStaticField("Ljava/nio/file/attribute/AclEntryPermission;")
    WRITE_ACL = JavaStaticField("Ljava/nio/file/attribute/AclEntryPermission;")
    WRITE_OWNER = JavaStaticField("Ljava/nio/file/attribute/AclEntryPermission;")
    SYNCHRONIZE = JavaStaticField("Ljava/nio/file/attribute/AclEntryPermission;")
    LIST_DIRECTORY = JavaStaticField("Ljava/nio/file/attribute/AclEntryPermission;")
    ADD_FILE = JavaStaticField("Ljava/nio/file/attribute/AclEntryPermission;")
    ADD_SUBDIRECTORY = JavaStaticField("Ljava/nio/file/attribute/AclEntryPermission;")

class FileStoreAttributeView(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/nio/file/attribute/FileStoreAttributeView"

class UserPrincipalNotFoundException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/nio/file/attribute/UserPrincipalNotFoundException"
    __javaconstructor__ = [("(Ljava/lang/String;)V", False)]
    getName = JavaMethod("()Ljava/lang/String;")

class DosFileAttributeView(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/nio/file/attribute/DosFileAttributeView"
    setHidden = JavaMethod("(Z)V")
    name = JavaMethod("()Ljava/lang/String;")
    setReadOnly = JavaMethod("(Z)V")
    readAttributes = JavaMultipleMethod([("()Ljava/nio/file/attribute/BasicFileAttributes;", False, False), ("()Ljava/nio/file/attribute/DosFileAttributes;", False, False)])
    setSystem = JavaMethod("(Z)V")
    setArchive = JavaMethod("(Z)V")

class FileTime(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/nio/file/attribute/FileTime"
    toInstant = JavaMethod("()Ljava/time/Instant;")
    fromMillis = JavaStaticMethod("(J)Ljava/nio/file/attribute/FileTime;")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    toString = JavaMethod("()Ljava/lang/String;")
    hashCode = JavaMethod("()I")
    compareTo = JavaMultipleMethod([("(Ljava/nio/file/attribute/FileTime;)I", False, False), ("(Ljava/lang/Object;)I", False, False)])
    from = JavaMultipleMethod([("(Ljava/time/Instant;)Ljava/nio/file/attribute/FileTime;", True, False), ("(JLjava/util/concurrent/TimeUnit;)Ljava/nio/file/attribute/FileTime;", True, False)])
    to = JavaMethod("(Ljava/util/concurrent/TimeUnit;)J")
    toMillis = JavaMethod("()J")

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

class BasicFileAttributes(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/nio/file/attribute/BasicFileAttributes"
    lastAccessTime = JavaMethod("()Ljava/nio/file/attribute/FileTime;")
    lastModifiedTime = JavaMethod("()Ljava/nio/file/attribute/FileTime;")
    isSymbolicLink = JavaMethod("()Z")
    fileKey = JavaMethod("()Ljava/lang/Object;")
    creationTime = JavaMethod("()Ljava/nio/file/attribute/FileTime;")
    isOther = JavaMethod("()Z")
    size = JavaMethod("()J")
    isRegularFile = JavaMethod("()Z")
    isDirectory = JavaMethod("()Z")

class PosixFileAttributes(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/nio/file/attribute/PosixFileAttributes"
    group = JavaMethod("()Ljava/nio/file/attribute/GroupPrincipal;")
    permissions = JavaMethod("()Ljava/util/Set;")
    owner = JavaMethod("()Ljava/nio/file/attribute/UserPrincipal;")

class UserPrincipalLookupService(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/nio/file/attribute/UserPrincipalLookupService"
    lookupPrincipalByName = JavaMethod("(Ljava/lang/String;)Ljava/nio/file/attribute/UserPrincipal;")
    lookupPrincipalByGroupName = JavaMethod("(Ljava/lang/String;)Ljava/nio/file/attribute/GroupPrincipal;")

class FileAttributeView(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/nio/file/attribute/FileAttributeView"

class DosFileAttributes(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/nio/file/attribute/DosFileAttributes"
    isHidden = JavaMethod("()Z")
    isSystem = JavaMethod("()Z")
    isReadOnly = JavaMethod("()Z")
    isArchive = JavaMethod("()Z")

class AttributeView(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/nio/file/attribute/AttributeView"
    name = JavaMethod("()Ljava/lang/String;")

class AclFileAttributeView(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/nio/file/attribute/AclFileAttributeView"
    name = JavaMethod("()Ljava/lang/String;")
    getAcl = JavaMethod("()Ljava/util/List;")
    setAcl = JavaMethod("(Ljava/util/List;)V")