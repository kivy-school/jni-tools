from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["StorageManager"]

class StorageManager(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/os/storage/StorageManager"
    ACTION_CLEAR_APP_CACHE = JavaStaticField("Ljava/lang/String;")
    ACTION_MANAGE_STORAGE = JavaStaticField("Ljava/lang/String;")
    EXTRA_REQUESTED_BYTES = JavaStaticField("Ljava/lang/String;")
    EXTRA_UUID = JavaStaticField("Ljava/lang/String;")
    UUID_DEFAULT = JavaStaticField("Ljava/util/UUID;")
    registerStorageVolumeCallback = JavaMethod("(Ljava/util/concurrent/Executor;Landroid/os/storage/StorageManager$StorageVolumeCallback;)V")
    unregisterStorageVolumeCallback = JavaMethod("(Landroid/os/storage/StorageManager$StorageVolumeCallback;)V")
    mountObb = JavaMethod("(Ljava/lang/String;Ljava/lang/String;Landroid/os/storage/OnObbStateChangeListener;)Z")
    getManageSpaceActivityIntent = JavaMethod("(Ljava/lang/String;I)Landroid/app/PendingIntent;")
    unmountObb = JavaMethod("(Ljava/lang/String;ZLandroid/os/storage/OnObbStateChangeListener;)Z")
    isObbMounted = JavaMethod("(Ljava/lang/String;)Z")
    getMountedObbPath = JavaMethod("(Ljava/lang/String;)Ljava/lang/String;")
    getUuidForPath = JavaMethod("(Ljava/io/File;)Ljava/util/UUID;")
    isAllocationSupported = JavaMethod("(Ljava/io/FileDescriptor;)Z")
    getStorageVolume = JavaMultipleMethod([("(Ljava/io/File;)Landroid/os/storage/StorageVolume;", False, False), ("(Landroid/net/Uri;)Landroid/os/storage/StorageVolume;", False, False)])
    getStorageVolumes = JavaMethod("()Ljava/util/List;")
    getStorageVolumesIncludingSharedProfiles = JavaMethod("()Ljava/util/List;")
    getRecentStorageVolumes = JavaMethod("()Ljava/util/List;")
    getPrimaryStorageVolume = JavaMethod("()Landroid/os/storage/StorageVolume;")
    isEncrypted = JavaMethod("(Ljava/io/File;)Z")
    openProxyFileDescriptor = JavaMethod("(ILandroid/os/ProxyFileDescriptorCallback;Landroid/os/Handler;)Landroid/os/ParcelFileDescriptor;")
    getCacheQuotaBytes = JavaMethod("(Ljava/util/UUID;)J")
    getCacheSizeBytes = JavaMethod("(Ljava/util/UUID;)J")
    getAllocatableBytes = JavaMethod("(Ljava/util/UUID;)J")
    allocateBytes = JavaMultipleMethod([("(Ljava/util/UUID;J)V", False, False), ("(Ljava/io/FileDescriptor;J)V", False, False)])
    setCacheBehaviorGroup = JavaMethod("(Ljava/io/File;Z)V")
    isCacheBehaviorGroup = JavaMethod("(Ljava/io/File;)Z")
    setCacheBehaviorTombstone = JavaMethod("(Ljava/io/File;Z)V")
    isCacheBehaviorTombstone = JavaMethod("(Ljava/io/File;)Z")
    isCheckpointSupported = JavaMethod("()Z")

    class StorageVolumeCallback(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/os/storage/StorageManager/StorageVolumeCallback"
        __javaconstructor__ = [("()V", False)]
        onStateChanged = JavaMethod("(Landroid/os/storage/StorageVolume;)V")