from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["AdManagerAdViewOptions"]

class AdManagerAdViewOptions(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/google/android/gms/ads/formats/AdManagerAdViewOptions"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    getManualImpressionsEnabled = JavaMethod("()Z")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "com/google/android/gms/ads/formats/AdManagerAdViewOptions/Builder"
        __javaconstructor__ = [("()V", False)]
        setManualImpressionsEnabled = JavaMethod("(Z)Lcom/google/android/gms/ads/formats/AdManagerAdViewOptions$Builder;")
        build = JavaMethod("()Lcom/google/android/gms/ads/formats/AdManagerAdViewOptions;")