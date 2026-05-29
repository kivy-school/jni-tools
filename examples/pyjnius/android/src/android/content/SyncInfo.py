from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["SyncInfo"]

class SyncInfo(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/content/SyncInfo"
    account = JavaField("Landroid/accounts/Account;")
    authority = JavaField("Ljava/lang/String;")
    startTime = JavaField("J")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")