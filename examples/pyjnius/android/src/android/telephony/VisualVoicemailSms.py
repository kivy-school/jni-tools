from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["VisualVoicemailSms"]

class VisualVoicemailSms(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/telephony/VisualVoicemailSms"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    getPhoneAccountHandle = JavaMethod("()Landroid/telecom/PhoneAccountHandle;")
    getFields = JavaMethod("()Landroid/os/Bundle;")
    getPrefix = JavaMethod("()Ljava/lang/String;")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")
    getMessageBody = JavaMethod("()Ljava/lang/String;")