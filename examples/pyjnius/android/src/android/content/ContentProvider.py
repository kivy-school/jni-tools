from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ContentProvider"]

class ContentProvider(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/content/ContentProvider"
    __javaconstructor__ = [("()V", False)]
    getContext = JavaMethod("()Landroid/content/Context;")
    requireContext = JavaMethod("()Landroid/content/Context;")
    getCallingPackage = JavaMethod("()Ljava/lang/String;")
    getCallingAttributionSource = JavaMethod("()Landroid/content/AttributionSource;")
    getCallingAttributionTag = JavaMethod("()Ljava/lang/String;")
    getCallingPackageUnchecked = JavaMethod("()Ljava/lang/String;")
    onCallingPackageChanged = JavaMethod("()V")
    clearCallingIdentity = JavaMethod("()Landroid/content/ContentProvider$CallingIdentity;")
    restoreCallingIdentity = JavaMethod("(Landroid/content/ContentProvider$CallingIdentity;)V")
    setReadPermission = JavaMethod("(Ljava/lang/String;)V")
    getReadPermission = JavaMethod("()Ljava/lang/String;")
    setWritePermission = JavaMethod("(Ljava/lang/String;)V")
    getWritePermission = JavaMethod("()Ljava/lang/String;")
    setPathPermissions = JavaMethod("([Landroid/content/pm/PathPermission;)V")
    getPathPermissions = JavaMethod("()[Landroid/content/pm/PathPermission;")
    onCreate = JavaMethod("()Z")
    onConfigurationChanged = JavaMethod("(Landroid/content/res/Configuration;)V")
    onLowMemory = JavaMethod("()V")
    onTrimMemory = JavaMethod("(I)V")
    query = JavaMultipleMethod([("(Landroid/net/Uri;[Ljava/lang/String;Ljava/lang/String;[Ljava/lang/String;Ljava/lang/String;)Landroid/database/Cursor;", False, False), ("(Landroid/net/Uri;[Ljava/lang/String;Ljava/lang/String;[Ljava/lang/String;Ljava/lang/String;Landroid/os/CancellationSignal;)Landroid/database/Cursor;", False, False), ("(Landroid/net/Uri;[Ljava/lang/String;Landroid/os/Bundle;Landroid/os/CancellationSignal;)Landroid/database/Cursor;", False, False)])
    getType = JavaMethod("(Landroid/net/Uri;)Ljava/lang/String;")
    getTypeAnonymous = JavaMethod("(Landroid/net/Uri;)Ljava/lang/String;")
    canonicalize = JavaMethod("(Landroid/net/Uri;)Landroid/net/Uri;")
    uncanonicalize = JavaMethod("(Landroid/net/Uri;)Landroid/net/Uri;")
    refresh = JavaMethod("(Landroid/net/Uri;Landroid/os/Bundle;Landroid/os/CancellationSignal;)Z")
    insert = JavaMultipleMethod([("(Landroid/net/Uri;Landroid/content/ContentValues;)Landroid/net/Uri;", False, False), ("(Landroid/net/Uri;Landroid/content/ContentValues;Landroid/os/Bundle;)Landroid/net/Uri;", False, False)])
    bulkInsert = JavaMethod("(Landroid/net/Uri;[Landroid/content/ContentValues;)I")
    delete = JavaMultipleMethod([("(Landroid/net/Uri;Ljava/lang/String;[Ljava/lang/String;)I", False, False), ("(Landroid/net/Uri;Landroid/os/Bundle;)I", False, False)])
    update = JavaMultipleMethod([("(Landroid/net/Uri;Landroid/content/ContentValues;Ljava/lang/String;[Ljava/lang/String;)I", False, False), ("(Landroid/net/Uri;Landroid/content/ContentValues;Landroid/os/Bundle;)I", False, False)])
    openFile = JavaMultipleMethod([("(Landroid/net/Uri;Ljava/lang/String;)Landroid/os/ParcelFileDescriptor;", False, False), ("(Landroid/net/Uri;Ljava/lang/String;Landroid/os/CancellationSignal;)Landroid/os/ParcelFileDescriptor;", False, False)])
    openAssetFile = JavaMultipleMethod([("(Landroid/net/Uri;Ljava/lang/String;)Landroid/content/res/AssetFileDescriptor;", False, False), ("(Landroid/net/Uri;Ljava/lang/String;Landroid/os/CancellationSignal;)Landroid/content/res/AssetFileDescriptor;", False, False)])
    openFileHelper = JavaMethod("(Landroid/net/Uri;Ljava/lang/String;)Landroid/os/ParcelFileDescriptor;")
    getStreamTypes = JavaMethod("(Landroid/net/Uri;Ljava/lang/String;)[Ljava/lang/String;")
    openTypedAssetFile = JavaMultipleMethod([("(Landroid/net/Uri;Ljava/lang/String;Landroid/os/Bundle;)Landroid/content/res/AssetFileDescriptor;", False, False), ("(Landroid/net/Uri;Ljava/lang/String;Landroid/os/Bundle;Landroid/os/CancellationSignal;)Landroid/content/res/AssetFileDescriptor;", False, False)])
    openPipeHelper = JavaMethod("(Landroid/net/Uri;Ljava/lang/String;Landroid/os/Bundle;Ljava/lang/Object;Landroid/content/ContentProvider$PipeDataWriter;)Landroid/os/ParcelFileDescriptor;")
    isTemporary = JavaMethod("()Z")
    attachInfo = JavaMethod("(Landroid/content/Context;Landroid/content/pm/ProviderInfo;)V")
    applyBatch = JavaMultipleMethod([("(Ljava/lang/String;Ljava/util/ArrayList;)[Landroid/content/ContentProviderResult;", False, False), ("(Ljava/util/ArrayList;)[Landroid/content/ContentProviderResult;", False, False)])
    call = JavaMultipleMethod([("(Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;Landroid/os/Bundle;)Landroid/os/Bundle;", False, False), ("(Ljava/lang/String;Ljava/lang/String;Landroid/os/Bundle;)Landroid/os/Bundle;", False, False)])
    shutdown = JavaMethod("()V")
    dump = JavaMethod("(Ljava/io/FileDescriptor;Ljava/io/PrintWriter;[Ljava/lang/String;)V")

    class CallingIdentity(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/content/ContentProvider/CallingIdentity"

    class PipeDataWriter(JavaInterface, metaclass=MetaJavaClass):
        __javaclass__ = "android/content/ContentProvider/PipeDataWriter"
        writeDataToPipe = JavaMethod("(Landroid/os/ParcelFileDescriptor;Landroid/net/Uri;Ljava/lang/String;Landroid/os/Bundle;Ljava/lang/Object;)V")