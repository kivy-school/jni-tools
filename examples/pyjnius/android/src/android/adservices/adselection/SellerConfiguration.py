from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["SellerConfiguration"]

class SellerConfiguration(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/adservices/adselection/SellerConfiguration"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")
    getMaximumPayloadSizeBytes = JavaMethod("()I")
    getPerBuyerConfigurations = JavaMethod("()Ljava/util/Set;")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/adservices/adselection/SellerConfiguration$Builder"
        __javaconstructor__ = [("()V", False)]
        setPerBuyerConfigurations = JavaMethod("(Ljava/util/Set;)Landroid/adservices/adselection/SellerConfiguration$Builder;")
        setMaximumPayloadSizeBytes = JavaMethod("(I)Landroid/adservices/adselection/SellerConfiguration$Builder;")
        build = JavaMethod("()Landroid/adservices/adselection/SellerConfiguration;")