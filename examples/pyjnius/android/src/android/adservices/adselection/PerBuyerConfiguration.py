from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["PerBuyerConfiguration"]

class PerBuyerConfiguration(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/adservices/adselection/PerBuyerConfiguration"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    getBuyer = JavaMethod("()Landroid/adservices/common/AdTechIdentifier;")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")
    getTargetInputSizeBytes = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/adservices/adselection/PerBuyerConfiguration$Builder"
        __javaconstructor__ = [("()V", False)]
        setBuyer = JavaMethod("(Landroid/adservices/common/AdTechIdentifier;)Landroid/adservices/adselection/PerBuyerConfiguration$Builder;")
        build = JavaMethod("()Landroid/adservices/adselection/PerBuyerConfiguration;")
        setTargetInputSizeBytes = JavaMethod("(I)Landroid/adservices/adselection/PerBuyerConfiguration$Builder;")