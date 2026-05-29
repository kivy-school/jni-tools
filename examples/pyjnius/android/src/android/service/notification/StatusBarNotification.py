from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["StatusBarNotification"]

class StatusBarNotification(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/service/notification/StatusBarNotification"
    __javaconstructor__ = [("(Ljava/lang/String;Ljava/lang/String;ILjava/lang/String;IIILandroid/app/Notification;Landroid/os/UserHandle;J)V", False), ("(Landroid/os/Parcel;)V", False)]
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    getGroupKey = JavaMethod("()Ljava/lang/String;")
    getNotification = JavaMethod("()Landroid/app/Notification;")
    getOpPkg = JavaMethod("()Ljava/lang/String;")
    getOverrideGroupKey = JavaMethod("()Ljava/lang/String;")
    getPostTime = JavaMethod("()J")
    getUserId = JavaMethod("()I")
    isAppGroup = JavaMethod("()Z")
    isClearable = JavaMethod("()Z")
    isGroup = JavaMethod("()Z")
    isOngoing = JavaMethod("()Z")
    setOverrideGroupKey = JavaMethod("(Ljava/lang/String;)V")
    toString = JavaMethod("()Ljava/lang/String;")
    clone = JavaMultipleMethod([("()Ljava/lang/Object;", False, False), ("()Landroid/service/notification/StatusBarNotification;", False, False)])
    getPackageName = JavaMethod("()Ljava/lang/String;")
    getKey = JavaMethod("()Ljava/lang/String;")
    getId = JavaMethod("()I")
    getUid = JavaMethod("()I")
    getTag = JavaMethod("()Ljava/lang/String;")
    getUser = JavaMethod("()Landroid/os/UserHandle;")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")