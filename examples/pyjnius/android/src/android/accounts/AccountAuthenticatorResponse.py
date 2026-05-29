from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["AccountAuthenticatorResponse"]

class AccountAuthenticatorResponse(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/accounts/AccountAuthenticatorResponse"
    __javaconstructor__ = [("(Landroid/os/Parcel;)V", False)]
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    onRequestContinued = JavaMethod("()V")
    onError = JavaMethod("(ILjava/lang/String;)V")
    onResult = JavaMethod("(Landroid/os/Bundle;)V")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")