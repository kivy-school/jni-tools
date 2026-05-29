from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["IntentSender"]

class IntentSender(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/content/IntentSender"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    toString = JavaMethod("()Ljava/lang/String;")
    hashCode = JavaMethod("()I")
    getCreatorPackage = JavaMethod("()Ljava/lang/String;")
    getCreatorUid = JavaMethod("()I")
    getCreatorUserHandle = JavaMethod("()Landroid/os/UserHandle;")
    getTargetPackage = JavaMethod("()Ljava/lang/String;")
    sendIntent = JavaMultipleMethod([("(Landroid/content/Context;ILandroid/content/Intent;Ljava/lang/String;Landroid/os/Bundle;Ljava/util/concurrent/Executor;Landroid/content/IntentSender$OnFinished;)V", False, False), ("(Landroid/content/Context;ILandroid/content/Intent;Landroid/content/IntentSender$OnFinished;Landroid/os/Handler;Ljava/lang/String;)V", False, False), ("(Landroid/content/Context;ILandroid/content/Intent;Landroid/content/IntentSender$OnFinished;Landroid/os/Handler;)V", False, False)])
    readIntentSenderOrNullFromParcel = JavaStaticMethod("(Landroid/os/Parcel;)Landroid/content/IntentSender;")
    writeIntentSenderOrNullToParcel = JavaStaticMethod("(Landroid/content/IntentSender;Landroid/os/Parcel;)V")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")

    class SendIntentException(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/content/IntentSender$SendIntentException"
        __javaconstructor__ = [("()V", False), ("(Ljava/lang/Exception;)V", False), ("(Ljava/lang/String;)V", False)]

    class OnFinished(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/content/IntentSender$OnFinished"
        onSendFinished = JavaMethod("(Landroid/content/IntentSender;Landroid/content/Intent;ILjava/lang/String;Landroid/os/Bundle;)V")