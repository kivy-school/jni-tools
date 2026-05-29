from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["StorageManager"]

class StorageManager(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/os/storage/StorageManager"
    ACTION_CLEAR_APP_CACHE = JavaStaticField("Ljava/lang/String;")
    ACTION_MANAGE_STORAGE = JavaStaticField("Ljava/lang/String;")
    EXTRA_REQUESTED_BYTES = JavaStaticField("Ljava/lang/String;")
    EXTRA_UUID = JavaStaticField("Ljava/lang/String;")
    UUID_DEFAULT = JavaStaticField("Ljava/util/UUID;")
    getAllocatableBytes = JavaMethod("(Ljava/util/UUID;)J")
    getCacheQuotaBytes = JavaMethod("(Ljava/util/UUID;)J")
    getCacheSizeBytes = JavaMethod("(Ljava/util/UUID;)J")
    getManageSpaceActivityIntent = JavaMethod("(Ljava/lang/String;I)Landroid/app/PendingIntent;")
    getMountedObbPath = JavaMethod("(Ljava/lang/String;)Ljava/lang/String;")
    getPrimaryStorageVolume = JavaMethod("()Landroid/os/storage/StorageVolume;")
    getRecentStorageVolumes = JavaMethod("()Ljava/util/List;")
    getStorageVolume = JavaMultipleMethod([("(Landroid/net/Uri;)Landroid/os/storage/StorageVolume;", False, False), ("(Ljava/io/File;)Landroid/os/storage/StorageVolume;", False, False)])
    getStorageVolumes = JavaMethod("()Ljava/util/List;")
    getStorageVolumesIncludingSharedProfiles = JavaMethod("()Ljava/util/List;")
    getUuidForPath = JavaMethod("(Ljava/io/File;)Ljava/util/UUID;")
    allocateBytes = JavaMultipleMethod([("(Ljava/util/UUID;J)V", False, False), ("(Ljava/io/FileDescriptor;J)V", False, False)])
    isAllocationSupported = JavaMethod("(Ljava/io/FileDescriptor;)Z")
    isCacheBehaviorGroup = JavaMethod("(Ljava/io/File;)Z")
    isCacheBehaviorTombstone = JavaMethod("(Ljava/io/File;)Z")
    isCheckpointSupported = JavaMethod("()Z")
    isEncrypted = JavaMethod("(Ljava/io/File;)Z")
    isObbMounted = JavaMethod("(Ljava/lang/String;)Z")
    mountObb = JavaMethod("(Ljava/lang/String;Ljava/lang/String;Landroid/os/storage/OnObbStateChangeListener;)Z")
    openProxyFileDescriptor = JavaMethod("(ILandroid/os/ProxyFileDescriptorCallback;Landroid/os/Handler;)Landroid/os/ParcelFileDescriptor;")
    registerStorageVolumeCallback = JavaMethod("(Ljava/util/concurrent/Executor;Landroid/os/storage/StorageManager$StorageVolumeCallback;)V")
    setCacheBehaviorGroup = JavaMethod("(Ljava/io/File;Z)V")
    setCacheBehaviorTombstone = JavaMethod("(Ljava/io/File;Z)V")
    unmountObb = JavaMethod("(Ljava/lang/String;ZLandroid/os/storage/OnObbStateChangeListener;)Z")
    unregisterStorageVolumeCallback = JavaMethod("(Landroid/os/storage/StorageManager$StorageVolumeCallback;)V")

    class StorageVolumeCallback(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/os/storage/StorageManager$StorageVolumeCallback"
        __javaconstructor__ = [("()V", False)]
        onStateChanged = JavaMethod("(Landroid/os/storage/StorageVolume;)V")