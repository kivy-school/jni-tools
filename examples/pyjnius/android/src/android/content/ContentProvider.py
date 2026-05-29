from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ContentProvider"]

class ContentProvider(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/content/ContentProvider"
    __javaconstructor__ = [("()V", False)]
    TRIM_MEMORY_BACKGROUND = JavaStaticField("I")
    TRIM_MEMORY_COMPLETE = JavaStaticField("I")
    TRIM_MEMORY_MODERATE = JavaStaticField("I")
    TRIM_MEMORY_RUNNING_CRITICAL = JavaStaticField("I")
    TRIM_MEMORY_RUNNING_LOW = JavaStaticField("I")
    TRIM_MEMORY_RUNNING_MODERATE = JavaStaticField("I")
    TRIM_MEMORY_UI_HIDDEN = JavaStaticField("I")
    shutdown = JavaMethod("()V")
    update = JavaMultipleMethod([("(Landroid/net/Uri;Landroid/content/ContentValues;Landroid/os/Bundle;)I", False, False), ("(Landroid/net/Uri;Landroid/content/ContentValues;Ljava/lang/String;[Ljava/lang/String;)I", False, False)])
    insert = JavaMultipleMethod([("(Landroid/net/Uri;Landroid/content/ContentValues;Landroid/os/Bundle;)Landroid/net/Uri;", False, False), ("(Landroid/net/Uri;Landroid/content/ContentValues;)Landroid/net/Uri;", False, False)])
    getType = JavaMethod("(Landroid/net/Uri;)Ljava/lang/String;")
    dump = JavaMethod("(Ljava/io/FileDescriptor;Ljava/io/PrintWriter;[Ljava/lang/String;)V")
    canonicalize = JavaMethod("(Landroid/net/Uri;)Landroid/net/Uri;")
    delete = JavaMultipleMethod([("(Landroid/net/Uri;Ljava/lang/String;[Ljava/lang/String;)I", False, False), ("(Landroid/net/Uri;Landroid/os/Bundle;)I", False, False)])
    query = JavaMultipleMethod([("(Landroid/net/Uri;[Ljava/lang/String;Landroid/os/Bundle;Landroid/os/CancellationSignal;)Landroid/database/Cursor;", False, False), ("(Landroid/net/Uri;[Ljava/lang/String;Ljava/lang/String;[Ljava/lang/String;Ljava/lang/String;Landroid/os/CancellationSignal;)Landroid/database/Cursor;", False, False), ("(Landroid/net/Uri;[Ljava/lang/String;Ljava/lang/String;[Ljava/lang/String;Ljava/lang/String;)Landroid/database/Cursor;", False, False)])
    call = JavaMultipleMethod([("(Ljava/lang/String;Ljava/lang/String;Landroid/os/Bundle;)Landroid/os/Bundle;", False, False), ("(Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;Landroid/os/Bundle;)Landroid/os/Bundle;", False, False)])
    getContext = JavaMethod("()Landroid/content/Context;")
    attachInfo = JavaMethod("(Landroid/content/Context;Landroid/content/pm/ProviderInfo;)V")
    clearCallingIdentity = JavaMethod("()Landroid/content/ContentProvider$CallingIdentity;")
    getCallingAttributionTag = JavaMethod("()Ljava/lang/String;")
    getCallingPackage = JavaMethod("()Ljava/lang/String;")
    getCallingPackageUnchecked = JavaMethod("()Ljava/lang/String;")
    getPathPermissions = JavaMethod("()[Landroid/content/pm/PathPermission;")
    getReadPermission = JavaMethod("()Ljava/lang/String;")
    getTypeAnonymous = JavaMethod("(Landroid/net/Uri;)Ljava/lang/String;")
    getWritePermission = JavaMethod("()Ljava/lang/String;")
    onCallingPackageChanged = JavaMethod("()V")
    openPipeHelper = JavaMethod("(Landroid/net/Uri;Ljava/lang/String;Landroid/os/Bundle;Ljava/lang/Object;Landroid/content/ContentProvider$PipeDataWriter;)Landroid/os/ParcelFileDescriptor;")
    requireContext = JavaMethod("()Landroid/content/Context;")
    restoreCallingIdentity = JavaMethod("(Landroid/content/ContentProvider$CallingIdentity;)V")
    refresh = JavaMethod("(Landroid/net/Uri;Landroid/os/Bundle;Landroid/os/CancellationSignal;)Z")
    applyBatch = JavaMultipleMethod([("(Ljava/lang/String;Ljava/util/ArrayList;)[Landroid/content/ContentProviderResult;", False, False), ("(Ljava/util/ArrayList;)[Landroid/content/ContentProviderResult;", False, False)])
    openTypedAssetFile = JavaMultipleMethod([("(Landroid/net/Uri;Ljava/lang/String;Landroid/os/Bundle;Landroid/os/CancellationSignal;)Landroid/content/res/AssetFileDescriptor;", False, False), ("(Landroid/net/Uri;Ljava/lang/String;Landroid/os/Bundle;)Landroid/content/res/AssetFileDescriptor;", False, False)])
    bulkInsert = JavaMethod("(Landroid/net/Uri;[Landroid/content/ContentValues;)I")
    getStreamTypes = JavaMethod("(Landroid/net/Uri;Ljava/lang/String;)[Ljava/lang/String;")
    openAssetFile = JavaMultipleMethod([("(Landroid/net/Uri;Ljava/lang/String;)Landroid/content/res/AssetFileDescriptor;", False, False), ("(Landroid/net/Uri;Ljava/lang/String;Landroid/os/CancellationSignal;)Landroid/content/res/AssetFileDescriptor;", False, False)])
    openFile = JavaMultipleMethod([("(Landroid/net/Uri;Ljava/lang/String;Landroid/os/CancellationSignal;)Landroid/os/ParcelFileDescriptor;", False, False), ("(Landroid/net/Uri;Ljava/lang/String;)Landroid/os/ParcelFileDescriptor;", False, False)])
    uncanonicalize = JavaMethod("(Landroid/net/Uri;)Landroid/net/Uri;")
    onCreate = JavaMethod("()Z")
    onTrimMemory = JavaMethod("(I)V")
    onLowMemory = JavaMethod("()V")
    onConfigurationChanged = JavaMethod("(Landroid/content/res/Configuration;)V")
    getCallingAttributionSource = JavaMethod("()Landroid/content/AttributionSource;")

    class PipeDataWriter(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/content/ContentProvider$PipeDataWriter"
        writeDataToPipe = JavaMethod("(Landroid/os/ParcelFileDescriptor;Landroid/net/Uri;Ljava/lang/String;Landroid/os/Bundle;Ljava/lang/Object;)V")

    class CallingIdentity(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/content/ContentProvider$CallingIdentity"