from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["RecoverableSecurityException"]

class RecoverableSecurityException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/app/RecoverableSecurityException"
    __javaconstructor__ = [("(Ljava/lang/Throwable;Ljava/lang/CharSequence;Landroid/app/RemoteAction;)V", False)]
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    getUserMessage = JavaMethod("()Ljava/lang/CharSequence;")
    getUserAction = JavaMethod("()Landroid/app/RemoteAction;")
    describeContents = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")