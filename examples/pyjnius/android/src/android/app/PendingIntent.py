from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["PendingIntent"]

class PendingIntent(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/app/PendingIntent"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    FLAG_ALLOW_UNSAFE_IMPLICIT_INTENT = JavaStaticField("I")
    FLAG_CANCEL_CURRENT = JavaStaticField("I")
    FLAG_IMMUTABLE = JavaStaticField("I")
    FLAG_MUTABLE = JavaStaticField("I")
    FLAG_NO_CREATE = JavaStaticField("I")
    FLAG_ONE_SHOT = JavaStaticField("I")
    FLAG_UPDATE_CURRENT = JavaStaticField("I")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    toString = JavaMethod("()Ljava/lang/String;")
    hashCode = JavaMethod("()I")
    cancel = JavaMethod("()V")
    getBroadcast = JavaStaticMethod("(Landroid/content/Context;ILandroid/content/Intent;I)Landroid/app/PendingIntent;")
    getCreatorPackage = JavaMethod("()Ljava/lang/String;")
    getCreatorUid = JavaMethod("()I")
    getCreatorUserHandle = JavaMethod("()Landroid/os/UserHandle;")
    getForegroundService = JavaStaticMethod("(Landroid/content/Context;ILandroid/content/Intent;I)Landroid/app/PendingIntent;")
    getIntentSender = JavaMethod("()Landroid/content/IntentSender;")
    getService = JavaStaticMethod("(Landroid/content/Context;ILandroid/content/Intent;I)Landroid/app/PendingIntent;")
    getTargetPackage = JavaMethod("()Ljava/lang/String;")
    isActivity = JavaMethod("()Z")
    isBroadcast = JavaMethod("()Z")
    isForegroundService = JavaMethod("()Z")
    getActivities = JavaMultipleMethod([("(Landroid/content/Context;I[Landroid/content/Intent;I)Landroid/app/PendingIntent;", True, False), ("(Landroid/content/Context;I[Landroid/content/Intent;ILandroid/os/Bundle;)Landroid/app/PendingIntent;", True, False)])
    getActivity = JavaMultipleMethod([("(Landroid/content/Context;ILandroid/content/Intent;ILandroid/os/Bundle;)Landroid/app/PendingIntent;", True, False), ("(Landroid/content/Context;ILandroid/content/Intent;I)Landroid/app/PendingIntent;", True, False)])
    isImmutable = JavaMethod("()Z")
    isService = JavaMethod("()Z")
    readPendingIntentOrNullFromParcel = JavaStaticMethod("(Landroid/os/Parcel;)Landroid/app/PendingIntent;")
    send = JavaMultipleMethod([("(Landroid/content/Context;ILandroid/content/Intent;Landroid/app/PendingIntent$OnFinished;Landroid/os/Handler;Ljava/lang/String;Landroid/os/Bundle;)V", False, False), ("(Landroid/os/Bundle;)V", False, False), ("(I)V", False, False), ("(ILandroid/app/PendingIntent$OnFinished;Landroid/os/Handler;)V", False, False), ("()V", False, False), ("(Landroid/content/Context;ILandroid/content/Intent;)V", False, False), ("(Landroid/content/Context;ILandroid/content/Intent;Landroid/app/PendingIntent$OnFinished;Landroid/os/Handler;)V", False, False), ("(Landroid/content/Context;ILandroid/content/Intent;Landroid/app/PendingIntent$OnFinished;Landroid/os/Handler;Ljava/lang/String;)V", False, False)])
    writePendingIntentOrNullToParcel = JavaStaticMethod("(Landroid/app/PendingIntent;Landroid/os/Parcel;)V")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")

    class OnFinished(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/app/PendingIntent$OnFinished"
        onSendFinished = JavaMethod("(Landroid/app/PendingIntent;Landroid/content/Intent;ILjava/lang/String;Landroid/os/Bundle;)V")

    class CanceledException(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/app/PendingIntent$CanceledException"
        __javaconstructor__ = [("()V", False), ("(Ljava/lang/Exception;)V", False), ("(Ljava/lang/String;)V", False)]