from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["SchemaVisibilityConfig"]

class SchemaVisibilityConfig(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/app/appsearch/SchemaVisibilityConfig"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    getAllowedPackages = JavaMethod("()Ljava/util/List;")
    getPubliclyVisibleTargetPackage = JavaMethod("()Landroid/app/appsearch/PackageIdentifier;")
    getRequiredPermissions = JavaMethod("()Ljava/util/Set;")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/app/appsearch/SchemaVisibilityConfig$Builder"
        __javaconstructor__ = [("()V", False)]
        addAllowedPackage = JavaMethod("(Landroid/app/appsearch/PackageIdentifier;)Landroid/app/appsearch/SchemaVisibilityConfig$Builder;")
        addRequiredPermissions = JavaMethod("(Ljava/util/Set;)Landroid/app/appsearch/SchemaVisibilityConfig$Builder;")
        clearAllowedPackages = JavaMethod("()Landroid/app/appsearch/SchemaVisibilityConfig$Builder;")
        clearRequiredPermissions = JavaMethod("()Landroid/app/appsearch/SchemaVisibilityConfig$Builder;")
        setPubliclyVisibleTargetPackage = JavaMethod("(Landroid/app/appsearch/PackageIdentifier;)Landroid/app/appsearch/SchemaVisibilityConfig$Builder;")
        build = JavaMethod("()Landroid/app/appsearch/SchemaVisibilityConfig;")