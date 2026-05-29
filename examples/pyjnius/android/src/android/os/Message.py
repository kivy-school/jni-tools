from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

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
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    copyFrom = JavaMethod("(Landroid/os/Message;)V")
    getWhen = JavaMethod("()J")
    isAsynchronous = JavaMethod("()Z")
    peekData = JavaMethod("()Landroid/os/Bundle;")
    sendToTarget = JavaMethod("()V")
    setAsynchronous = JavaMethod("(Z)V")
    toString = JavaMethod("()Ljava/lang/String;")
    getTarget = JavaMethod("()Landroid/os/Handler;")
    setTarget = JavaMethod("(Landroid/os/Handler;)V")
    setData = JavaMethod("(Landroid/os/Bundle;)V")
    getData = JavaMethod("()Landroid/os/Bundle;")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")
    recycle = JavaMethod("()V")
    obtain = JavaMultipleMethod([("(Landroid/os/Handler;IIILjava/lang/Object;)Landroid/os/Message;", True, False), ("(Landroid/os/Handler;ILjava/lang/Object;)Landroid/os/Message;", True, False), ("(Landroid/os/Handler;III)Landroid/os/Message;", True, False), ("(Landroid/os/Handler;I)Landroid/os/Message;", True, False), ("(Landroid/os/Handler;)Landroid/os/Message;", True, False), ("()Landroid/os/Message;", True, False), ("(Landroid/os/Message;)Landroid/os/Message;", True, False), ("(Landroid/os/Handler;Ljava/lang/Runnable;)Landroid/os/Message;", True, False)])
    getCallback = JavaMethod("()Ljava/lang/Runnable;")