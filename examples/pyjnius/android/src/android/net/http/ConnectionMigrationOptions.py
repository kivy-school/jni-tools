from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ConnectionMigrationOptions"]

class ConnectionMigrationOptions(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/net/http/ConnectionMigrationOptions"
    MIGRATION_OPTION_DISABLED = JavaStaticField("I")
    MIGRATION_OPTION_ENABLED = JavaStaticField("I")
    MIGRATION_OPTION_UNSPECIFIED = JavaStaticField("I")
    getDefaultNetworkMigration = JavaMethod("()I")
    getPathDegradationMigration = JavaMethod("()I")
    getAllowNonDefaultNetworkUsage = JavaMethod("()I")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/net/http/ConnectionMigrationOptions/Builder"
        __javaconstructor__ = [("()V", False)]
        setDefaultNetworkMigration = JavaMethod("(I)Landroid/net/http/ConnectionMigrationOptions$Builder;")
        setPathDegradationMigration = JavaMethod("(I)Landroid/net/http/ConnectionMigrationOptions$Builder;")
        setAllowNonDefaultNetworkUsage = JavaMethod("(I)Landroid/net/http/ConnectionMigrationOptions$Builder;")
        build = JavaMethod("()Landroid/net/http/ConnectionMigrationOptions;")