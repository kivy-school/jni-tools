from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["StatusBarNotification"]

class StatusBarNotification(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/service/notification/StatusBarNotification"
    __javaconstructor__ = [("(Ljava/lang/String;Ljava/lang/String;ILjava/lang/String;IIILandroid/app/Notification;Landroid/os/UserHandle;J)V", False), ("(Landroid/os/Parcel;)V", False)]
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    isGroup = JavaMethod("()Z")
    isAppGroup = JavaMethod("()Z")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")
    clone = JavaMethod("()Landroid/service/notification/StatusBarNotification;")
    toString = JavaMethod("()Ljava/lang/String;")
    isOngoing = JavaMethod("()Z")
    isClearable = JavaMethod("()Z")
    getUserId = JavaMethod("()I")
    getPackageName = JavaMethod("()Ljava/lang/String;")
    getId = JavaMethod("()I")
    getTag = JavaMethod("()Ljava/lang/String;")
    getUid = JavaMethod("()I")
    getOpPkg = JavaMethod("()Ljava/lang/String;")
    getNotification = JavaMethod("()Landroid/app/Notification;")
    getUser = JavaMethod("()Landroid/os/UserHandle;")
    getPostTime = JavaMethod("()J")
    getKey = JavaMethod("()Ljava/lang/String;")
    getGroupKey = JavaMethod("()Ljava/lang/String;")
    setOverrideGroupKey = JavaMethod("(Ljava/lang/String;)V")
    getOverrideGroupKey = JavaMethod("()Ljava/lang/String;")