from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ConnectionRequest"]

class ConnectionRequest(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/telecom/ConnectionRequest"
    __javaconstructor__ = [("(Landroid/telecom/PhoneAccountHandle;Landroid/net/Uri;Landroid/os/Bundle;)V", False), ("(Landroid/telecom/PhoneAccountHandle;Landroid/net/Uri;Landroid/os/Bundle;I)V", False)]
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    getParticipants = JavaMethod("()Ljava/util/List;")
    isRequestingRtt = JavaMethod("()Z")
    getRttTextStream = JavaMethod("()Landroid/telecom/Connection$RttTextStream;")
    isAdhocConferenceCall = JavaMethod("()Z")
    toString = JavaMethod("()Ljava/lang/String;")
    getAddress = JavaMethod("()Landroid/net/Uri;")
    getVideoState = JavaMethod("()I")
    getExtras = JavaMethod("()Landroid/os/Bundle;")
    getAccountHandle = JavaMethod("()Landroid/telecom/PhoneAccountHandle;")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")