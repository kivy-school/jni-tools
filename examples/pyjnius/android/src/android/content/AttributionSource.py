from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["AttributionSource"]

class AttributionSource(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/content/AttributionSource"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    myAttributionSource = JavaStaticMethod("()Landroid/content/AttributionSource;")
    enforceCallingUid = JavaMethod("()V")
    checkCallingUid = JavaMethod("()Z")
    toString = JavaMethod("()Ljava/lang/String;")
    isTrusted = JavaMethod("(Landroid/content/Context;)Z")
    getUid = JavaMethod("()I")
    getPid = JavaMethod("()I")
    getPackageName = JavaMethod("()Ljava/lang/String;")
    getAttributionTag = JavaMethod("()Ljava/lang/String;")
    getDeviceId = JavaMethod("()I")
    getNext = JavaMethod("()Landroid/content/AttributionSource;")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/content/AttributionSource/Builder"
        __javaconstructor__ = [("(I)V", False), ("(Landroid/content/AttributionSource;)V", False)]
        setPid = JavaMethod("(I)Landroid/content/AttributionSource$Builder;")
        setPackageName = JavaMethod("(Ljava/lang/String;)Landroid/content/AttributionSource$Builder;")
        setAttributionTag = JavaMethod("(Ljava/lang/String;)Landroid/content/AttributionSource$Builder;")
        setDeviceId = JavaMethod("(I)Landroid/content/AttributionSource$Builder;")
        setNext = JavaMethod("(Landroid/content/AttributionSource;)Landroid/content/AttributionSource$Builder;")
        build = JavaMethod("()Landroid/content/AttributionSource;")