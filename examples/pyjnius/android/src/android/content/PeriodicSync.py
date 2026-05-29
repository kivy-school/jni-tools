from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["PeriodicSync"]

class PeriodicSync(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/content/PeriodicSync"
    __javaconstructor__ = [("(Landroid/accounts/Account;Ljava/lang/String;Landroid/os/Bundle;J)V", False)]
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    account = JavaField("Landroid/accounts/Account;")
    authority = JavaField("Ljava/lang/String;")
    extras = JavaField("Landroid/os/Bundle;")
    period = JavaField("J")
    describeContents = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    toString = JavaMethod("()Ljava/lang/String;")