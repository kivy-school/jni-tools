from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["IBinder"]

class IBinder(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "android/os/IBinder"
    DUMP_TRANSACTION = JavaStaticField("I")
    FIRST_CALL_TRANSACTION = JavaStaticField("I")
    FLAG_ONEWAY = JavaStaticField("I")
    INTERFACE_TRANSACTION = JavaStaticField("I")
    LAST_CALL_TRANSACTION = JavaStaticField("I")
    LIKE_TRANSACTION = JavaStaticField("I")
    PING_TRANSACTION = JavaStaticField("I")
    TWEET_TRANSACTION = JavaStaticField("I")
    getSuggestedMaxIpcSizeBytes = JavaStaticMethod("()I")
    getInterfaceDescriptor = JavaMethod("()Ljava/lang/String;")
    pingBinder = JavaMethod("()Z")
    isBinderAlive = JavaMethod("()Z")
    queryLocalInterface = JavaMethod("(Ljava/lang/String;)Landroid/os/IInterface;")
    dump = JavaMethod("(Ljava/io/FileDescriptor;[Ljava/lang/String;)V")
    dumpAsync = JavaMethod("(Ljava/io/FileDescriptor;[Ljava/lang/String;)V")
    transact = JavaMethod("(ILandroid/os/Parcel;Landroid/os/Parcel;I)Z")
    linkToDeath = JavaMethod("(Landroid/os/IBinder$DeathRecipient;I)V")
    unlinkToDeath = JavaMethod("(Landroid/os/IBinder$DeathRecipient;I)Z")

    class DeathRecipient(JavaInterface, metaclass=MetaJavaClass):
        __javaclass__ = "android/os/IBinder/DeathRecipient"
        binderDied = JavaMultipleMethod([("()V", False, False), ("(Landroid/os/IBinder;)V", False, False)])