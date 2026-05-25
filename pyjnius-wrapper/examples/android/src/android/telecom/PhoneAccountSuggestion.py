from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["PhoneAccountSuggestion"]

class PhoneAccountSuggestion(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/telecom/PhoneAccountSuggestion"
    __javaconstructor__ = [("(Landroid/telecom/PhoneAccountHandle;IZ)V", False)]
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    REASON_FREQUENT = JavaStaticField("I")
    REASON_INTRA_CARRIER = JavaStaticField("I")
    REASON_NONE = JavaStaticField("I")
    REASON_OTHER = JavaStaticField("I")
    REASON_USER_SET = JavaStaticField("I")
    getPhoneAccountHandle = JavaMethod("()Landroid/telecom/PhoneAccountHandle;")
    getReason = JavaMethod("()I")
    shouldAutoSelect = JavaMethod("()Z")
    describeContents = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")