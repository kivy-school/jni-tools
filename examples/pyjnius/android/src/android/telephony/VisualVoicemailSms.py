from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["VisualVoicemailSms"]

class VisualVoicemailSms(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/telephony/VisualVoicemailSms"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    getPhoneAccountHandle = JavaMethod("()Landroid/telecom/PhoneAccountHandle;")
    getPrefix = JavaMethod("()Ljava/lang/String;")
    getFields = JavaMethod("()Landroid/os/Bundle;")
    getMessageBody = JavaMethod("()Ljava/lang/String;")
    describeContents = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")