from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["AppInstallFilters"]

class AppInstallFilters(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/adservices/common/AppInstallFilters"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    toString = JavaMethod("()Ljava/lang/String;")
    hashCode = JavaMethod("()I")
    getPackageNames = JavaMethod("()Ljava/util/Set;")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/adservices/common/AppInstallFilters$Builder"
        __javaconstructor__ = [("()V", False)]
        setPackageNames = JavaMethod("(Ljava/util/Set;)Landroid/adservices/common/AppInstallFilters$Builder;")
        build = JavaMethod("()Landroid/adservices/common/AppInstallFilters;")