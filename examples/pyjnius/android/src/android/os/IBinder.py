from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["IBinder"]

class IBinder(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/os/IBinder"
    DUMP_TRANSACTION = JavaStaticField("I")
    FIRST_CALL_TRANSACTION = JavaStaticField("I")
    FLAG_ONEWAY = JavaStaticField("I")
    INTERFACE_TRANSACTION = JavaStaticField("I")
    LAST_CALL_TRANSACTION = JavaStaticField("I")
    LIKE_TRANSACTION = JavaStaticField("I")
    PING_TRANSACTION = JavaStaticField("I")
    TWEET_TRANSACTION = JavaStaticField("I")
    dump = JavaMethod("(Ljava/io/FileDescriptor;[Ljava/lang/String;)V")
    dumpAsync = JavaMethod("(Ljava/io/FileDescriptor;[Ljava/lang/String;)V")
    pingBinder = JavaMethod("()Z")
    transact = JavaMethod("(ILandroid/os/Parcel;Landroid/os/Parcel;I)Z")
    isBinderAlive = JavaMethod("()Z")
    linkToDeath = JavaMethod("(Landroid/os/IBinder$DeathRecipient;I)V")
    unlinkToDeath = JavaMethod("(Landroid/os/IBinder$DeathRecipient;I)Z")
    addFrozenStateChangeCallback = JavaMethod("(Ljava/util/concurrent/Executor;Landroid/os/IBinder$FrozenStateChangeCallback;)V")
    getInterfaceDescriptor = JavaMethod("()Ljava/lang/String;")
    getSuggestedMaxIpcSizeBytes = JavaStaticMethod("()I")
    queryLocalInterface = JavaMethod("(Ljava/lang/String;)Landroid/os/IInterface;")
    removeFrozenStateChangeCallback = JavaMethod("(Landroid/os/IBinder$FrozenStateChangeCallback;)Z")

    class FrozenStateChangeCallback(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/os/IBinder$FrozenStateChangeCallback"
        STATE_FROZEN = JavaStaticField("I")
        STATE_UNFROZEN = JavaStaticField("I")
        onFrozenStateChanged = JavaMethod("(Landroid/os/IBinder;I)V")

    class DeathRecipient(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/os/IBinder$DeathRecipient"
        binderDied = JavaMultipleMethod([("()V", False, False), ("(Landroid/os/IBinder;)V", False, False)])