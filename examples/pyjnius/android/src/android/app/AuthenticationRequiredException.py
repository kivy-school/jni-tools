from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["AuthenticationRequiredException"]

class AuthenticationRequiredException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/app/AuthenticationRequiredException"
    __javaconstructor__ = [("(Ljava/lang/Throwable;Landroid/app/PendingIntent;)V", False)]
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    getUserAction = JavaMethod("()Landroid/app/PendingIntent;")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")