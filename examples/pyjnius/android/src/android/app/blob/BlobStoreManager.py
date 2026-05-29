from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["BlobStoreManager"]

class BlobStoreManager(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/app/blob/BlobStoreManager"
    getLeasedBlobs = JavaMethod("()Ljava/util/List;")
    openBlob = JavaMethod("(Landroid/app/blob/BlobHandle;)Landroid/os/ParcelFileDescriptor;")
    releaseLease = JavaMethod("(Landroid/app/blob/BlobHandle;)V")
    getRemainingLeaseQuotaBytes = JavaMethod("()J")
    acquireLease = JavaMultipleMethod([("(Landroid/app/blob/BlobHandle;Ljava/lang/CharSequence;)V", False, False), ("(Landroid/app/blob/BlobHandle;Ljava/lang/CharSequence;J)V", False, False), ("(Landroid/app/blob/BlobHandle;I)V", False, False), ("(Landroid/app/blob/BlobHandle;IJ)V", False, False)])
    openSession = JavaMethod("(J)Landroid/app/blob/BlobStoreManager$Session;")
    abandonSession = JavaMethod("(J)V")
    createSession = JavaMethod("(Landroid/app/blob/BlobHandle;)J")

    class Session(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/app/blob/BlobStoreManager$Session"
        abandon = JavaMethod("()V")
        openRead = JavaMethod("()Landroid/os/ParcelFileDescriptor;")
        openWrite = JavaMethod("(JJ)Landroid/os/ParcelFileDescriptor;")
        allowPackageAccess = JavaMethod("(Ljava/lang/String;[B)V")
        isPublicAccessAllowed = JavaMethod("()Z")
        isSameSignatureAccessAllowed = JavaMethod("()Z")
        allowPublicAccess = JavaMethod("()V")
        allowSameSignatureAccess = JavaMethod("()V")
        isPackageAccessAllowed = JavaMethod("(Ljava/lang/String;[B)Z")
        commit = JavaMethod("(Ljava/util/concurrent/Executor;Ljava/util/function/Consumer;)V")
        close = JavaMethod("()V")
        getSize = JavaMethod("()J")