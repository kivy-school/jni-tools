from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["CallAttributes"]

class CallAttributes(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/telecom/CallAttributes"
    AUDIO_CALL = JavaStaticField("I")
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    DIRECTION_INCOMING = JavaStaticField("I")
    DIRECTION_OUTGOING = JavaStaticField("I")
    SUPPORTS_SET_INACTIVE = JavaStaticField("I")
    SUPPORTS_STREAM = JavaStaticField("I")
    SUPPORTS_TRANSFER = JavaStaticField("I")
    SUPPORTS_VIDEO_CALLING = JavaStaticField("I")
    VIDEO_CALL = JavaStaticField("I")
    getPhoneAccountHandle = JavaMethod("()Landroid/telecom/PhoneAccountHandle;")
    getDisplayName = JavaMethod("()Ljava/lang/CharSequence;")
    getAddress = JavaMethod("()Landroid/net/Uri;")
    getDirection = JavaMethod("()I")
    getCallType = JavaMethod("()I")
    getCallCapabilities = JavaMethod("()I")
    describeContents = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    toString = JavaMethod("()Ljava/lang/String;")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/telecom/CallAttributes/Builder"
        __javaconstructor__ = [("(Landroid/telecom/PhoneAccountHandle;ILjava/lang/CharSequence;Landroid/net/Uri;)V", False)]
        setCallType = JavaMethod("(I)Landroid/telecom/CallAttributes$Builder;")
        setCallCapabilities = JavaMethod("(I)Landroid/telecom/CallAttributes$Builder;")
        build = JavaMethod("()Landroid/telecom/CallAttributes;")