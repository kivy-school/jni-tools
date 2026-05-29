from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["RecoverableSecurityException"]

class RecoverableSecurityException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/app/RecoverableSecurityException"
    __javaconstructor__ = [("(Ljava/lang/Throwable;Ljava/lang/CharSequence;Landroid/app/RemoteAction;)V", False)]
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    getUserAction = JavaMethod("()Landroid/app/RemoteAction;")
    getUserMessage = JavaMethod("()Ljava/lang/CharSequence;")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")