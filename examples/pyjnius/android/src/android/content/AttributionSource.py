from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["AttributionSource"]

class AttributionSource(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/content/AttributionSource"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    toString = JavaMethod("()Ljava/lang/String;")
    hashCode = JavaMethod("()I")
    getPackageName = JavaMethod("()Ljava/lang/String;")
    getNext = JavaMethod("()Landroid/content/AttributionSource;")
    checkCallingUid = JavaMethod("()Z")
    enforceCallingUid = JavaMethod("()V")
    getPid = JavaMethod("()I")
    getUid = JavaMethod("()I")
    myAttributionSource = JavaStaticMethod("()Landroid/content/AttributionSource;")
    getAttributionTag = JavaMethod("()Ljava/lang/String;")
    getDeviceId = JavaMethod("()I")
    isTrusted = JavaMethod("(Landroid/content/Context;)Z")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/content/AttributionSource$Builder"
        __javaconstructor__ = [("(Landroid/content/AttributionSource;)V", False), ("(I)V", False)]
        setPackageName = JavaMethod("(Ljava/lang/String;)Landroid/content/AttributionSource$Builder;")
        build = JavaMethod("()Landroid/content/AttributionSource;")
        setNext = JavaMethod("(Landroid/content/AttributionSource;)Landroid/content/AttributionSource$Builder;")
        setDeviceId = JavaMethod("(I)Landroid/content/AttributionSource$Builder;")
        setAttributionTag = JavaMethod("(Ljava/lang/String;)Landroid/content/AttributionSource$Builder;")
        setPid = JavaMethod("(I)Landroid/content/AttributionSource$Builder;")