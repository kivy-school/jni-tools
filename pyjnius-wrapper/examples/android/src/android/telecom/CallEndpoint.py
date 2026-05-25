from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["CallEndpoint"]

class CallEndpoint(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/telecom/CallEndpoint"
    __javaconstructor__ = [("(Ljava/lang/CharSequence;ILandroid/os/ParcelUuid;)V", False)]
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    TYPE_BLUETOOTH = JavaStaticField("I")
    TYPE_EARPIECE = JavaStaticField("I")
    TYPE_SPEAKER = JavaStaticField("I")
    TYPE_STREAMING = JavaStaticField("I")
    TYPE_UNKNOWN = JavaStaticField("I")
    TYPE_WIRED_HEADSET = JavaStaticField("I")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")
    toString = JavaMethod("()Ljava/lang/String;")
    getEndpointName = JavaMethod("()Ljava/lang/CharSequence;")
    getEndpointType = JavaMethod("()I")
    getIdentifier = JavaMethod("()Landroid/os/ParcelUuid;")
    describeContents = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")