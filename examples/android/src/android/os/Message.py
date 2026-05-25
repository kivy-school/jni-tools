from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Message"]

class Message(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/os/Message"
    __javaconstructor__ = [("()V", False)]
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    arg1 = JavaField("I")
    arg2 = JavaField("I")
    obj = JavaField("Ljava/lang/Object;")
    replyTo = JavaField("Landroid/os/Messenger;")
    sendingUid = JavaField("I")
    what = JavaField("I")
    obtain = JavaMultipleMethod([("()Landroid/os/Message;", True, False), ("(Landroid/os/Message;)Landroid/os/Message;", True, False), ("(Landroid/os/Handler;)Landroid/os/Message;", True, False), ("(Landroid/os/Handler;Ljava/lang/Runnable;)Landroid/os/Message;", True, False), ("(Landroid/os/Handler;I)Landroid/os/Message;", True, False), ("(Landroid/os/Handler;ILjava/lang/Object;)Landroid/os/Message;", True, False), ("(Landroid/os/Handler;III)Landroid/os/Message;", True, False), ("(Landroid/os/Handler;IIILjava/lang/Object;)Landroid/os/Message;", True, False)])
    recycle = JavaMethod("()V")
    copyFrom = JavaMethod("(Landroid/os/Message;)V")
    getWhen = JavaMethod("()J")
    setTarget = JavaMethod("(Landroid/os/Handler;)V")
    getTarget = JavaMethod("()Landroid/os/Handler;")
    getCallback = JavaMethod("()Ljava/lang/Runnable;")
    getData = JavaMethod("()Landroid/os/Bundle;")
    peekData = JavaMethod("()Landroid/os/Bundle;")
    setData = JavaMethod("(Landroid/os/Bundle;)V")
    sendToTarget = JavaMethod("()V")
    isAsynchronous = JavaMethod("()Z")
    setAsynchronous = JavaMethod("(Z)V")
    toString = JavaMethod("()Ljava/lang/String;")
    describeContents = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")