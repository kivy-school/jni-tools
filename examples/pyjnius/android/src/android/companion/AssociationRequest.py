from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["AssociationRequest"]

class AssociationRequest(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/companion/AssociationRequest"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    DEVICE_PROFILE_APP_STREAMING = JavaStaticField("Ljava/lang/String;")
    DEVICE_PROFILE_AUTOMOTIVE_PROJECTION = JavaStaticField("Ljava/lang/String;")
    DEVICE_PROFILE_COMPUTER = JavaStaticField("Ljava/lang/String;")
    DEVICE_PROFILE_GLASSES = JavaStaticField("Ljava/lang/String;")
    DEVICE_PROFILE_NEARBY_DEVICE_STREAMING = JavaStaticField("Ljava/lang/String;")
    DEVICE_PROFILE_WATCH = JavaStaticField("Ljava/lang/String;")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    isSelfManaged = JavaMethod("()Z")
    isSingleDevice = JavaMethod("()Z")
    getDeviceProfile = JavaMethod("()Ljava/lang/String;")
    isForceConfirmation = JavaMethod("()Z")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    toString = JavaMethod("()Ljava/lang/String;")
    hashCode = JavaMethod("()I")
    getDisplayName = JavaMethod("()Ljava/lang/CharSequence;")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/companion/AssociationRequest$Builder"
        __javaconstructor__ = [("()V", False)]
        addDeviceFilter = JavaMethod("(Landroid/companion/DeviceFilter;)Landroid/companion/AssociationRequest$Builder;")
        setSelfManaged = JavaMethod("(Z)Landroid/companion/AssociationRequest$Builder;")
        setDeviceProfile = JavaMethod("(Ljava/lang/String;)Landroid/companion/AssociationRequest$Builder;")
        setForceConfirmation = JavaMethod("(Z)Landroid/companion/AssociationRequest$Builder;")
        setSingleDevice = JavaMethod("(Z)Landroid/companion/AssociationRequest$Builder;")
        setDisplayName = JavaMethod("(Ljava/lang/CharSequence;)Landroid/companion/AssociationRequest$Builder;")
        build = JavaMethod("()Landroid/companion/AssociationRequest;")