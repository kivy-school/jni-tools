from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["AccountAuthenticatorResponse"]

class AccountAuthenticatorResponse(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/accounts/AccountAuthenticatorResponse"
    __javaconstructor__ = [("(Landroid/os/Parcel;)V", False)]
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    onResult = JavaMethod("(Landroid/os/Bundle;)V")
    onRequestContinued = JavaMethod("()V")
    onError = JavaMethod("(ILjava/lang/String;)V")
    describeContents = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")