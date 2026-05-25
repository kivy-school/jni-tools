from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["AdData"]

class AdData(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/adservices/common/AdData"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")
    getRenderUri = JavaMethod("()Landroid/net/Uri;")
    getMetadata = JavaMethod("()Ljava/lang/String;")
    getAdCounterKeys = JavaMethod("()Ljava/util/Set;")
    getAdFilters = JavaMethod("()Landroid/adservices/common/AdFilters;")
    getAdRenderId = JavaMethod("()Ljava/lang/String;")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")
    toString = JavaMethod("()Ljava/lang/String;")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/adservices/common/AdData/Builder"
        __javaconstructor__ = [("()V", False)]
        setRenderUri = JavaMethod("(Landroid/net/Uri;)Landroid/adservices/common/AdData$Builder;")
        setMetadata = JavaMethod("(Ljava/lang/String;)Landroid/adservices/common/AdData$Builder;")
        setAdCounterKeys = JavaMethod("(Ljava/util/Set;)Landroid/adservices/common/AdData$Builder;")
        setAdFilters = JavaMethod("(Landroid/adservices/common/AdFilters;)Landroid/adservices/common/AdData$Builder;")
        setAdRenderId = JavaMethod("(Ljava/lang/String;)Landroid/adservices/common/AdData$Builder;")
        build = JavaMethod("()Landroid/adservices/common/AdData;")