from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ContentProviderClient"]

class ContentProviderClient(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/content/ContentProviderClient"
    query = JavaMultipleMethod([("(Landroid/net/Uri;[Ljava/lang/String;Ljava/lang/String;[Ljava/lang/String;Ljava/lang/String;)Landroid/database/Cursor;", False, False), ("(Landroid/net/Uri;[Ljava/lang/String;Ljava/lang/String;[Ljava/lang/String;Ljava/lang/String;Landroid/os/CancellationSignal;)Landroid/database/Cursor;", False, False), ("(Landroid/net/Uri;[Ljava/lang/String;Landroid/os/Bundle;Landroid/os/CancellationSignal;)Landroid/database/Cursor;", False, False)])
    getType = JavaMethod("(Landroid/net/Uri;)Ljava/lang/String;")
    getStreamTypes = JavaMethod("(Landroid/net/Uri;Ljava/lang/String;)[Ljava/lang/String;")
    canonicalize = JavaMethod("(Landroid/net/Uri;)Landroid/net/Uri;")
    uncanonicalize = JavaMethod("(Landroid/net/Uri;)Landroid/net/Uri;")
    refresh = JavaMethod("(Landroid/net/Uri;Landroid/os/Bundle;Landroid/os/CancellationSignal;)Z")
    insert = JavaMultipleMethod([("(Landroid/net/Uri;Landroid/content/ContentValues;)Landroid/net/Uri;", False, False), ("(Landroid/net/Uri;Landroid/content/ContentValues;Landroid/os/Bundle;)Landroid/net/Uri;", False, False)])
    bulkInsert = JavaMethod("(Landroid/net/Uri;[Landroid/content/ContentValues;)I")
    delete = JavaMultipleMethod([("(Landroid/net/Uri;Ljava/lang/String;[Ljava/lang/String;)I", False, False), ("(Landroid/net/Uri;Landroid/os/Bundle;)I", False, False)])
    update = JavaMultipleMethod([("(Landroid/net/Uri;Landroid/content/ContentValues;Ljava/lang/String;[Ljava/lang/String;)I", False, False), ("(Landroid/net/Uri;Landroid/content/ContentValues;Landroid/os/Bundle;)I", False, False)])
    openFile = JavaMultipleMethod([("(Landroid/net/Uri;Ljava/lang/String;)Landroid/os/ParcelFileDescriptor;", False, False), ("(Landroid/net/Uri;Ljava/lang/String;Landroid/os/CancellationSignal;)Landroid/os/ParcelFileDescriptor;", False, False)])
    openAssetFile = JavaMultipleMethod([("(Landroid/net/Uri;Ljava/lang/String;)Landroid/content/res/AssetFileDescriptor;", False, False), ("(Landroid/net/Uri;Ljava/lang/String;Landroid/os/CancellationSignal;)Landroid/content/res/AssetFileDescriptor;", False, False)])
    openTypedAssetFileDescriptor = JavaMultipleMethod([("(Landroid/net/Uri;Ljava/lang/String;Landroid/os/Bundle;)Landroid/content/res/AssetFileDescriptor;", False, False), ("(Landroid/net/Uri;Ljava/lang/String;Landroid/os/Bundle;Landroid/os/CancellationSignal;)Landroid/content/res/AssetFileDescriptor;", False, False)])
    openTypedAssetFile = JavaMethod("(Landroid/net/Uri;Ljava/lang/String;Landroid/os/Bundle;Landroid/os/CancellationSignal;)Landroid/content/res/AssetFileDescriptor;")
    applyBatch = JavaMultipleMethod([("(Ljava/util/ArrayList;)[Landroid/content/ContentProviderResult;", False, False), ("(Ljava/lang/String;Ljava/util/ArrayList;)[Landroid/content/ContentProviderResult;", False, False)])
    call = JavaMultipleMethod([("(Ljava/lang/String;Ljava/lang/String;Landroid/os/Bundle;)Landroid/os/Bundle;", False, False), ("(Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;Landroid/os/Bundle;)Landroid/os/Bundle;", False, False)])
    close = JavaMethod("()V")
    release = JavaMethod("()Z")
    finalize = JavaMethod("()V")
    getLocalContentProvider = JavaMethod("()Landroid/content/ContentProvider;")