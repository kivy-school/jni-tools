from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Binder"]

class Binder(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/os/Binder"
    __javaconstructor__ = [("()V", False), ("(Ljava/lang/String;)V", False)]
    getCallingPid = JavaStaticMethod("()I")
    getCallingUid = JavaStaticMethod("()I")
    getCallingUidOrThrow = JavaStaticMethod("()I")
    getCallingUserHandle = JavaStaticMethod("()Landroid/os/UserHandle;")
    clearCallingIdentity = JavaStaticMethod("()J")
    restoreCallingIdentity = JavaStaticMethod("(J)V")
    setCallingWorkSourceUid = JavaStaticMethod("(I)J")
    getCallingWorkSourceUid = JavaStaticMethod("()I")
    clearCallingWorkSource = JavaStaticMethod("()J")
    restoreCallingWorkSource = JavaStaticMethod("(J)V")
    flushPendingCommands = JavaStaticMethod("()V")
    joinThreadPool = JavaStaticMethod("()V")
    attachInterface = JavaMethod("(Landroid/os/IInterface;Ljava/lang/String;)V")
    getInterfaceDescriptor = JavaMethod("()Ljava/lang/String;")
    pingBinder = JavaMethod("()Z")
    isBinderAlive = JavaMethod("()Z")
    queryLocalInterface = JavaMethod("(Ljava/lang/String;)Landroid/os/IInterface;")
    onTransact = JavaMethod("(ILandroid/os/Parcel;Landroid/os/Parcel;I)Z")
    dump = JavaMultipleMethod([("(Ljava/io/FileDescriptor;[Ljava/lang/String;)V", False, False), ("(Ljava/io/FileDescriptor;Ljava/io/PrintWriter;[Ljava/lang/String;)V", False, False)])
    dumpAsync = JavaMethod("(Ljava/io/FileDescriptor;[Ljava/lang/String;)V")
    transact = JavaMethod("(ILandroid/os/Parcel;Landroid/os/Parcel;I)Z")
    linkToDeath = JavaMethod("(Landroid/os/IBinder$DeathRecipient;I)V")
    unlinkToDeath = JavaMethod("(Landroid/os/IBinder$DeathRecipient;I)Z")