from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

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
    getDeviceProfile = JavaMethod("()Ljava/lang/String;")
    getDisplayName = JavaMethod("()Ljava/lang/CharSequence;")
    isSelfManaged = JavaMethod("()Z")
    isForceConfirmation = JavaMethod("()Z")
    isSingleDevice = JavaMethod("()Z")
    toString = JavaMethod("()Ljava/lang/String;")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/companion/AssociationRequest/Builder"
        __javaconstructor__ = [("()V", False)]
        setSingleDevice = JavaMethod("(Z)Landroid/companion/AssociationRequest$Builder;")
        addDeviceFilter = JavaMethod("(Landroid/companion/DeviceFilter;)Landroid/companion/AssociationRequest$Builder;")
        setDeviceProfile = JavaMethod("(Ljava/lang/String;)Landroid/companion/AssociationRequest$Builder;")
        setDisplayName = JavaMethod("(Ljava/lang/CharSequence;)Landroid/companion/AssociationRequest$Builder;")
        setSelfManaged = JavaMethod("(Z)Landroid/companion/AssociationRequest$Builder;")
        setForceConfirmation = JavaMethod("(Z)Landroid/companion/AssociationRequest$Builder;")
        build = JavaMethod("()Landroid/companion/AssociationRequest;")