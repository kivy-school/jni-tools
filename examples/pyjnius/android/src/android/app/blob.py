from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

class BlobHandle(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/app/blob/BlobHandle"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    createWithSha256 = JavaStaticMethod("([BLjava/lang/CharSequence;JLjava/lang/String;)Landroid/app/blob/BlobHandle;")
    getSha256Digest = JavaMethod("()[B")
    getExpiryTimeMillis = JavaMethod("()J")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    toString = JavaMethod("()Ljava/lang/String;")
    hashCode = JavaMethod("()I")
    getTag = JavaMethod("()Ljava/lang/String;")
    getLabel = JavaMethod("()Ljava/lang/CharSequence;")
    describeContents = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")

class BlobStoreManager(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/app/blob/BlobStoreManager"
    getRemainingLeaseQuotaBytes = JavaMethod("()J")
    acquireLease = JavaMultipleMethod([("(Landroid/app/blob/BlobHandle;Ljava/lang/CharSequence;J)V", False, False), ("(Landroid/app/blob/BlobHandle;IJ)V", False, False), ("(Landroid/app/blob/BlobHandle;I)V", False, False), ("(Landroid/app/blob/BlobHandle;Ljava/lang/CharSequence;)V", False, False)])
    getLeasedBlobs = JavaMethod("()Ljava/util/List;")
    openBlob = JavaMethod("(Landroid/app/blob/BlobHandle;)Landroid/os/ParcelFileDescriptor;")
    releaseLease = JavaMethod("(Landroid/app/blob/BlobHandle;)V")
    openSession = JavaMethod("(J)Landroid/app/blob/BlobStoreManager$Session;")
    abandonSession = JavaMethod("(J)V")
    createSession = JavaMethod("(Landroid/app/blob/BlobHandle;)J")

    class Session(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/app/blob/BlobStoreManager$Session"
        allowPackageAccess = JavaMethod("(Ljava/lang/String;[B)V")
        allowSameSignatureAccess = JavaMethod("()V")
        allowPublicAccess = JavaMethod("()V")
        isPackageAccessAllowed = JavaMethod("(Ljava/lang/String;[B)Z")
        isPublicAccessAllowed = JavaMethod("()Z")
        isSameSignatureAccessAllowed = JavaMethod("()Z")
        commit = JavaMethod("(Ljava/util/concurrent/Executor;Ljava/util/function/Consumer;)V")
        close = JavaMethod("()V")
        abandon = JavaMethod("()V")
        openRead = JavaMethod("()Landroid/os/ParcelFileDescriptor;")
        openWrite = JavaMethod("(JJ)Landroid/os/ParcelFileDescriptor;")
        getSize = JavaMethod("()J")