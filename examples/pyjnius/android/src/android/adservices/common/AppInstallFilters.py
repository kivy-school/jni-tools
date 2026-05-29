from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["AppInstallFilters"]

class AppInstallFilters(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/adservices/common/AppInstallFilters"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    getPackageNames = JavaMethod("()Ljava/util/Set;")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")
    toString = JavaMethod("()Ljava/lang/String;")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/adservices/common/AppInstallFilters/Builder"
        __javaconstructor__ = [("()V", False)]
        setPackageNames = JavaMethod("(Ljava/util/Set;)Landroid/adservices/common/AppInstallFilters$Builder;")
        build = JavaMethod("()Landroid/adservices/common/AppInstallFilters;")