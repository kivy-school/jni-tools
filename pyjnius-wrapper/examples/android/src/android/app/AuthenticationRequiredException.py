from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["AuthenticationRequiredException"]

class AuthenticationRequiredException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/app/AuthenticationRequiredException"
    __javaconstructor__ = [("(Ljava/lang/Throwable;Landroid/app/PendingIntent;)V", False)]
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    getUserAction = JavaMethod("()Landroid/app/PendingIntent;")
    describeContents = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")