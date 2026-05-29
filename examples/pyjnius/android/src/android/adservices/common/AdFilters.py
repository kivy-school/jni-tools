from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["AdFilters"]

class AdFilters(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/adservices/common/AdFilters"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    toString = JavaMethod("()Ljava/lang/String;")
    hashCode = JavaMethod("()I")
    getFrequencyCapFilters = JavaMethod("()Landroid/adservices/common/FrequencyCapFilters;")
    getAppInstallFilters = JavaMethod("()Landroid/adservices/common/AppInstallFilters;")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/adservices/common/AdFilters$Builder"
        __javaconstructor__ = [("()V", False)]
        setAppInstallFilters = JavaMethod("(Landroid/adservices/common/AppInstallFilters;)Landroid/adservices/common/AdFilters$Builder;")
        setFrequencyCapFilters = JavaMethod("(Landroid/adservices/common/FrequencyCapFilters;)Landroid/adservices/common/AdFilters$Builder;")
        build = JavaMethod("()Landroid/adservices/common/AdFilters;")