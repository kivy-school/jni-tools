from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["IntentSender"]

class IntentSender(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/content/IntentSender"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    sendIntent = JavaMultipleMethod([("(Landroid/content/Context;ILandroid/content/Intent;Landroid/content/IntentSender$OnFinished;Landroid/os/Handler;)V", False, False), ("(Landroid/content/Context;ILandroid/content/Intent;Landroid/content/IntentSender$OnFinished;Landroid/os/Handler;Ljava/lang/String;)V", False, False)])
    getTargetPackage = JavaMethod("()Ljava/lang/String;")
    getCreatorPackage = JavaMethod("()Ljava/lang/String;")
    getCreatorUid = JavaMethod("()I")
    getCreatorUserHandle = JavaMethod("()Landroid/os/UserHandle;")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")
    toString = JavaMethod("()Ljava/lang/String;")
    describeContents = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    writeIntentSenderOrNullToParcel = JavaStaticMethod("(Landroid/content/IntentSender;Landroid/os/Parcel;)V")
    readIntentSenderOrNullFromParcel = JavaStaticMethod("(Landroid/os/Parcel;)Landroid/content/IntentSender;")

    class OnFinished(JavaInterface, metaclass=MetaJavaClass):
        __javaclass__ = "android/content/IntentSender/OnFinished"
        onSendFinished = JavaMethod("(Landroid/content/IntentSender;Landroid/content/Intent;ILjava/lang/String;Landroid/os/Bundle;)V")

    class SendIntentException(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/content/IntentSender/SendIntentException"
        __javaconstructor__ = [("()V", False), ("(Ljava/lang/String;)V", False), ("(Ljava/lang/Exception;)V", False)]