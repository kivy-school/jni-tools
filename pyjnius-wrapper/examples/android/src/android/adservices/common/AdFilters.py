from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["AdFilters"]

class AdFilters(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/adservices/common/AdFilters"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    getFrequencyCapFilters = JavaMethod("()Landroid/adservices/common/FrequencyCapFilters;")
    getAppInstallFilters = JavaMethod("()Landroid/adservices/common/AppInstallFilters;")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")
    toString = JavaMethod("()Ljava/lang/String;")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/adservices/common/AdFilters/Builder"
        __javaconstructor__ = [("()V", False)]
        setFrequencyCapFilters = JavaMethod("(Landroid/adservices/common/FrequencyCapFilters;)Landroid/adservices/common/AdFilters$Builder;")
        setAppInstallFilters = JavaMethod("(Landroid/adservices/common/AppInstallFilters;)Landroid/adservices/common/AdFilters$Builder;")
        build = JavaMethod("()Landroid/adservices/common/AdFilters;")