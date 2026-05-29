from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["AdData"]

class AdData(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/adservices/common/AdData"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    getAdFilters = JavaMethod("()Landroid/adservices/common/AdFilters;")
    getAdRenderId = JavaMethod("()Ljava/lang/String;")
    getAdCounterKeys = JavaMethod("()Ljava/util/Set;")
    getRenderUri = JavaMethod("()Landroid/net/Uri;")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    toString = JavaMethod("()Ljava/lang/String;")
    hashCode = JavaMethod("()I")
    getMetadata = JavaMethod("()Ljava/lang/String;")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/adservices/common/AdData$Builder"
        __javaconstructor__ = [("()V", False)]
        setRenderUri = JavaMethod("(Landroid/net/Uri;)Landroid/adservices/common/AdData$Builder;")
        setAdFilters = JavaMethod("(Landroid/adservices/common/AdFilters;)Landroid/adservices/common/AdData$Builder;")
        setAdCounterKeys = JavaMethod("(Ljava/util/Set;)Landroid/adservices/common/AdData$Builder;")
        setAdRenderId = JavaMethod("(Ljava/lang/String;)Landroid/adservices/common/AdData$Builder;")
        build = JavaMethod("()Landroid/adservices/common/AdData;")
        setMetadata = JavaMethod("(Ljava/lang/String;)Landroid/adservices/common/AdData$Builder;")