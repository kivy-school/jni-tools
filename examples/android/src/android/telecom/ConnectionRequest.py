from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ConnectionRequest"]

class ConnectionRequest(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/telecom/ConnectionRequest"
    __javaconstructor__ = [("(Landroid/telecom/PhoneAccountHandle;Landroid/net/Uri;Landroid/os/Bundle;)V", False), ("(Landroid/telecom/PhoneAccountHandle;Landroid/net/Uri;Landroid/os/Bundle;I)V", False)]
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    getAccountHandle = JavaMethod("()Landroid/telecom/PhoneAccountHandle;")
    getAddress = JavaMethod("()Landroid/net/Uri;")
    getParticipants = JavaMethod("()Ljava/util/List;")
    getExtras = JavaMethod("()Landroid/os/Bundle;")
    getVideoState = JavaMethod("()I")
    isAdhocConferenceCall = JavaMethod("()Z")
    getRttTextStream = JavaMethod("()Landroid/telecom/Connection$RttTextStream;")
    isRequestingRtt = JavaMethod("()Z")
    toString = JavaMethod("()Ljava/lang/String;")
    describeContents = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")