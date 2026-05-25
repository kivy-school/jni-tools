from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

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
    getActivity = JavaMultipleMethod([("(Landroid/content/Context;ILandroid/content/Intent;I)Landroid/app/PendingIntent;", True, False), ("(Landroid/content/Context;ILandroid/content/Intent;ILandroid/os/Bundle;)Landroid/app/PendingIntent;", True, False)])
    getActivities = JavaMultipleMethod([("(Landroid/content/Context;I[Landroid/content/Intent;I)Landroid/app/PendingIntent;", True, False), ("(Landroid/content/Context;I[Landroid/content/Intent;ILandroid/os/Bundle;)Landroid/app/PendingIntent;", True, False)])
    getBroadcast = JavaStaticMethod("(Landroid/content/Context;ILandroid/content/Intent;I)Landroid/app/PendingIntent;")
    getService = JavaStaticMethod("(Landroid/content/Context;ILandroid/content/Intent;I)Landroid/app/PendingIntent;")
    getForegroundService = JavaStaticMethod("(Landroid/content/Context;ILandroid/content/Intent;I)Landroid/app/PendingIntent;")
    getIntentSender = JavaMethod("()Landroid/content/IntentSender;")
    cancel = JavaMethod("()V")
    send = JavaMultipleMethod([("()V", False, False), ("(I)V", False, False), ("(Landroid/content/Context;ILandroid/content/Intent;)V", False, False), ("(Landroid/os/Bundle;)V", False, False), ("(ILandroid/app/PendingIntent$OnFinished;Landroid/os/Handler;)V", False, False), ("(Landroid/content/Context;ILandroid/content/Intent;Landroid/app/PendingIntent$OnFinished;Landroid/os/Handler;)V", False, False), ("(Landroid/content/Context;ILandroid/content/Intent;Landroid/app/PendingIntent$OnFinished;Landroid/os/Handler;Ljava/lang/String;)V", False, False), ("(Landroid/content/Context;ILandroid/content/Intent;Landroid/app/PendingIntent$OnFinished;Landroid/os/Handler;Ljava/lang/String;Landroid/os/Bundle;)V", False, False)])
    getTargetPackage = JavaMethod("()Ljava/lang/String;")
    getCreatorPackage = JavaMethod("()Ljava/lang/String;")
    getCreatorUid = JavaMethod("()I")
    getCreatorUserHandle = JavaMethod("()Landroid/os/UserHandle;")
    isImmutable = JavaMethod("()Z")
    isActivity = JavaMethod("()Z")
    isForegroundService = JavaMethod("()Z")
    isService = JavaMethod("()Z")
    isBroadcast = JavaMethod("()Z")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")
    toString = JavaMethod("()Ljava/lang/String;")
    describeContents = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    writePendingIntentOrNullToParcel = JavaStaticMethod("(Landroid/app/PendingIntent;Landroid/os/Parcel;)V")
    readPendingIntentOrNullFromParcel = JavaStaticMethod("(Landroid/os/Parcel;)Landroid/app/PendingIntent;")

    class CanceledException(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/app/PendingIntent/CanceledException"
        __javaconstructor__ = [("()V", False), ("(Ljava/lang/String;)V", False), ("(Ljava/lang/Exception;)V", False)]

    class OnFinished(JavaInterface, metaclass=MetaJavaClass):
        __javaclass__ = "android/app/PendingIntent/OnFinished"
        onSendFinished = JavaMethod("(Landroid/app/PendingIntent;Landroid/content/Intent;ILjava/lang/String;Landroid/os/Bundle;)V")