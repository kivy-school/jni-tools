from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["SchemaVisibilityConfig"]

class SchemaVisibilityConfig(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/app/appsearch/SchemaVisibilityConfig"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    getAllowedPackages = JavaMethod("()Ljava/util/List;")
    getRequiredPermissions = JavaMethod("()Ljava/util/Set;")
    getPubliclyVisibleTargetPackage = JavaMethod("()Landroid/app/appsearch/PackageIdentifier;")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")
    describeContents = JavaMethod("()I")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/app/appsearch/SchemaVisibilityConfig/Builder"
        __javaconstructor__ = [("()V", False)]
        addAllowedPackage = JavaMethod("(Landroid/app/appsearch/PackageIdentifier;)Landroid/app/appsearch/SchemaVisibilityConfig$Builder;")
        clearAllowedPackages = JavaMethod("()Landroid/app/appsearch/SchemaVisibilityConfig$Builder;")
        addRequiredPermissions = JavaMethod("(Ljava/util/Set;)Landroid/app/appsearch/SchemaVisibilityConfig$Builder;")
        clearRequiredPermissions = JavaMethod("()Landroid/app/appsearch/SchemaVisibilityConfig$Builder;")
        setPubliclyVisibleTargetPackage = JavaMethod("(Landroid/app/appsearch/PackageIdentifier;)Landroid/app/appsearch/SchemaVisibilityConfig$Builder;")
        build = JavaMethod("()Landroid/app/appsearch/SchemaVisibilityConfig;")