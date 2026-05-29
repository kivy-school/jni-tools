from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

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
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    getEndpointName = JavaMethod("()Ljava/lang/CharSequence;")
    getEndpointType = JavaMethod("()I")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    toString = JavaMethod("()Ljava/lang/String;")
    hashCode = JavaMethod("()I")
    getIdentifier = JavaMethod("()Landroid/os/ParcelUuid;")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")