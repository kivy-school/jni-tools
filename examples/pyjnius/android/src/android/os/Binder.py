from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Binder"]

class Binder(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/os/Binder"
    __javaconstructor__ = [("()V", False), ("(Ljava/lang/String;)V", False)]
    DUMP_TRANSACTION = JavaStaticField("I")
    FIRST_CALL_TRANSACTION = JavaStaticField("I")
    FLAG_ONEWAY = JavaStaticField("I")
    INTERFACE_TRANSACTION = JavaStaticField("I")
    LAST_CALL_TRANSACTION = JavaStaticField("I")
    LIKE_TRANSACTION = JavaStaticField("I")
    PING_TRANSACTION = JavaStaticField("I")
    TWEET_TRANSACTION = JavaStaticField("I")
    attachInterface = JavaMethod("(Landroid/os/IInterface;Ljava/lang/String;)V")
    clearCallingWorkSource = JavaStaticMethod("()J")
    flushPendingCommands = JavaStaticMethod("()V")
    getCallingPid = JavaStaticMethod("()I")
    getCallingUidOrThrow = JavaStaticMethod("()I")
    getCallingUserHandle = JavaStaticMethod("()Landroid/os/UserHandle;")
    getCallingWorkSourceUid = JavaStaticMethod("()I")
    joinThreadPool = JavaStaticMethod("()V")
    restoreCallingWorkSource = JavaStaticMethod("(J)V")
    setCallingWorkSourceUid = JavaStaticMethod("(I)J")
    dump = JavaMethod("(Ljava/io/FileDescriptor;[Ljava/lang/String;)V")
    clearCallingIdentity = JavaStaticMethod("()J")
    restoreCallingIdentity = JavaStaticMethod("(J)V")
    dumpAsync = JavaMethod("(Ljava/io/FileDescriptor;[Ljava/lang/String;)V")
    pingBinder = JavaMethod("()Z")
    transact = JavaMethod("(ILandroid/os/Parcel;Landroid/os/Parcel;I)Z")
    isBinderAlive = JavaMethod("()Z")
    linkToDeath = JavaMethod("(Landroid/os/IBinder$DeathRecipient;I)V")
    unlinkToDeath = JavaMethod("(Landroid/os/IBinder$DeathRecipient;I)Z")
    getInterfaceDescriptor = JavaMethod("()Ljava/lang/String;")
    queryLocalInterface = JavaMethod("(Ljava/lang/String;)Landroid/os/IInterface;")
    getCallingUid = JavaStaticMethod("()I")