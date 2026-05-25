from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["BlobStoreManager"]

class BlobStoreManager(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/app/blob/BlobStoreManager"
    createSession = JavaMethod("(Landroid/app/blob/BlobHandle;)J")
    openSession = JavaMethod("(J)Landroid/app/blob/BlobStoreManager$Session;")
    abandonSession = JavaMethod("(J)V")
    openBlob = JavaMethod("(Landroid/app/blob/BlobHandle;)Landroid/os/ParcelFileDescriptor;")
    acquireLease = JavaMultipleMethod([("(Landroid/app/blob/BlobHandle;IJ)V", False, False), ("(Landroid/app/blob/BlobHandle;Ljava/lang/CharSequence;J)V", False, False), ("(Landroid/app/blob/BlobHandle;I)V", False, False), ("(Landroid/app/blob/BlobHandle;Ljava/lang/CharSequence;)V", False, False)])
    releaseLease = JavaMethod("(Landroid/app/blob/BlobHandle;)V")
    getRemainingLeaseQuotaBytes = JavaMethod("()J")
    getLeasedBlobs = JavaMethod("()Ljava/util/List;")

    class Session(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/app/blob/BlobStoreManager/Session"
        openWrite = JavaMethod("(JJ)Landroid/os/ParcelFileDescriptor;")
        openRead = JavaMethod("()Landroid/os/ParcelFileDescriptor;")
        getSize = JavaMethod("()J")
        close = JavaMethod("()V")
        abandon = JavaMethod("()V")
        allowPackageAccess = JavaMethod("(Ljava/lang/String;[B)V")
        isPackageAccessAllowed = JavaMethod("(Ljava/lang/String;[B)Z")
        allowSameSignatureAccess = JavaMethod("()V")
        isSameSignatureAccessAllowed = JavaMethod("()Z")
        allowPublicAccess = JavaMethod("()V")
        isPublicAccessAllowed = JavaMethod("()Z")
        commit = JavaMethod("(Ljava/util/concurrent/Executor;Ljava/util/function/Consumer;)V")