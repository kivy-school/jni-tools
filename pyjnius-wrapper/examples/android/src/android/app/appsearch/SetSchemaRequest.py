from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["SetSchemaRequest"]

class SetSchemaRequest(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/app/appsearch/SetSchemaRequest"
    READ_ASSISTANT_APP_SEARCH_DATA = JavaStaticField("I")
    READ_CALENDAR = JavaStaticField("I")
    READ_CONTACTS = JavaStaticField("I")
    READ_EXTERNAL_STORAGE = JavaStaticField("I")
    READ_HOME_APP_SEARCH_DATA = JavaStaticField("I")
    READ_SMS = JavaStaticField("I")
    getSchemas = JavaMethod("()Ljava/util/Set;")
    getSchemasNotDisplayedBySystem = JavaMethod("()Ljava/util/Set;")
    getSchemasVisibleToPackages = JavaMethod("()Ljava/util/Map;")
    getRequiredPermissionsForSchemaTypeVisibility = JavaMethod("()Ljava/util/Map;")
    getPubliclyVisibleSchemas = JavaMethod("()Ljava/util/Map;")
    getSchemasVisibleToConfigs = JavaMethod("()Ljava/util/Map;")
    getMigrators = JavaMethod("()Ljava/util/Map;")
    isForceOverride = JavaMethod("()Z")
    getVersion = JavaMethod("()I")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/app/appsearch/SetSchemaRequest/Builder"
        __javaconstructor__ = [("()V", False)]
        addSchemas = JavaMultipleMethod([("([Landroid/app/appsearch/AppSearchSchema;)Landroid/app/appsearch/SetSchemaRequest$Builder;", False, True), ("(Ljava/util/Collection;)Landroid/app/appsearch/SetSchemaRequest$Builder;", False, False)])
        setSchemaTypeDisplayedBySystem = JavaMethod("(Ljava/lang/String;Z)Landroid/app/appsearch/SetSchemaRequest$Builder;")
        addRequiredPermissionsForSchemaTypeVisibility = JavaMethod("(Ljava/lang/String;Ljava/util/Set;)Landroid/app/appsearch/SetSchemaRequest$Builder;")
        clearRequiredPermissionsForSchemaTypeVisibility = JavaMethod("(Ljava/lang/String;)Landroid/app/appsearch/SetSchemaRequest$Builder;")
        setSchemaTypeVisibilityForPackage = JavaMethod("(Ljava/lang/String;ZLandroid/app/appsearch/PackageIdentifier;)Landroid/app/appsearch/SetSchemaRequest$Builder;")
        setPubliclyVisibleSchema = JavaMethod("(Ljava/lang/String;Landroid/app/appsearch/PackageIdentifier;)Landroid/app/appsearch/SetSchemaRequest$Builder;")
        addSchemaTypeVisibleToConfig = JavaMethod("(Ljava/lang/String;Landroid/app/appsearch/SchemaVisibilityConfig;)Landroid/app/appsearch/SetSchemaRequest$Builder;")
        clearSchemaTypeVisibleToConfigs = JavaMethod("(Ljava/lang/String;)Landroid/app/appsearch/SetSchemaRequest$Builder;")
        setMigrator = JavaMethod("(Ljava/lang/String;Landroid/app/appsearch/Migrator;)Landroid/app/appsearch/SetSchemaRequest$Builder;")
        setMigrators = JavaMethod("(Ljava/util/Map;)Landroid/app/appsearch/SetSchemaRequest$Builder;")
        setForceOverride = JavaMethod("(Z)Landroid/app/appsearch/SetSchemaRequest$Builder;")
        setVersion = JavaMethod("(I)Landroid/app/appsearch/SetSchemaRequest$Builder;")
        build = JavaMethod("()Landroid/app/appsearch/SetSchemaRequest;")