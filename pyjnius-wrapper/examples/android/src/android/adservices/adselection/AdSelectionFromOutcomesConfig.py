from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["AdSelectionFromOutcomesConfig"]

class AdSelectionFromOutcomesConfig(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/adservices/adselection/AdSelectionFromOutcomesConfig"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    getSeller = JavaMethod("()Landroid/adservices/common/AdTechIdentifier;")
    getAdSelectionIds = JavaMethod("()Ljava/util/List;")
    getSelectionSignals = JavaMethod("()Landroid/adservices/common/AdSelectionSignals;")
    getSelectionLogicUri = JavaMethod("()Landroid/net/Uri;")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/adservices/adselection/AdSelectionFromOutcomesConfig/Builder"
        __javaconstructor__ = [("()V", False)]
        setSeller = JavaMethod("(Landroid/adservices/common/AdTechIdentifier;)Landroid/adservices/adselection/AdSelectionFromOutcomesConfig$Builder;")
        setAdSelectionIds = JavaMethod("(Ljava/util/List;)Landroid/adservices/adselection/AdSelectionFromOutcomesConfig$Builder;")
        setSelectionSignals = JavaMethod("(Landroid/adservices/common/AdSelectionSignals;)Landroid/adservices/adselection/AdSelectionFromOutcomesConfig$Builder;")
        setSelectionLogicUri = JavaMethod("(Landroid/net/Uri;)Landroid/adservices/adselection/AdSelectionFromOutcomesConfig$Builder;")
        build = JavaMethod("()Landroid/adservices/adselection/AdSelectionFromOutcomesConfig;")