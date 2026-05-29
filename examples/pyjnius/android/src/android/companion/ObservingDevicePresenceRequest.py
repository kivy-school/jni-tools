from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ObservingDevicePresenceRequest"]

class ObservingDevicePresenceRequest(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/companion/ObservingDevicePresenceRequest"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    toString = JavaMethod("()Ljava/lang/String;")
    hashCode = JavaMethod("()I")
    getUuid = JavaMethod("()Landroid/os/ParcelUuid;")
    getAssociationId = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/companion/ObservingDevicePresenceRequest$Builder"
        __javaconstructor__ = [("()V", False)]
        setAssociationId = JavaMethod("(I)Landroid/companion/ObservingDevicePresenceRequest$Builder;")
        setUuid = JavaMethod("(Landroid/os/ParcelUuid;)Landroid/companion/ObservingDevicePresenceRequest$Builder;")
        build = JavaMethod("()Landroid/companion/ObservingDevicePresenceRequest;")