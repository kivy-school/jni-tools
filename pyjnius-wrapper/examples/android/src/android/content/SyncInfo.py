from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["SyncInfo"]

class SyncInfo(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/content/SyncInfo"
    account = JavaField("Landroid/accounts/Account;")
    authority = JavaField("Ljava/lang/String;")
    startTime = JavaField("J")
    describeContents = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")