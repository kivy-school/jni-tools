from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ContentProviderClient"]

class ContentProviderClient(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/content/ContentProviderClient"
    update = JavaMultipleMethod([("(Landroid/net/Uri;Landroid/content/ContentValues;Landroid/os/Bundle;)I", False, False), ("(Landroid/net/Uri;Landroid/content/ContentValues;Ljava/lang/String;[Ljava/lang/String;)I", False, False)])
    insert = JavaMultipleMethod([("(Landroid/net/Uri;Landroid/content/ContentValues;)Landroid/net/Uri;", False, False), ("(Landroid/net/Uri;Landroid/content/ContentValues;Landroid/os/Bundle;)Landroid/net/Uri;", False, False)])
    close = JavaMethod("()V")
    getType = JavaMethod("(Landroid/net/Uri;)Ljava/lang/String;")
    canonicalize = JavaMethod("(Landroid/net/Uri;)Landroid/net/Uri;")
    delete = JavaMultipleMethod([("(Landroid/net/Uri;Ljava/lang/String;[Ljava/lang/String;)I", False, False), ("(Landroid/net/Uri;Landroid/os/Bundle;)I", False, False)])
    query = JavaMultipleMethod([("(Landroid/net/Uri;[Ljava/lang/String;Ljava/lang/String;[Ljava/lang/String;Ljava/lang/String;Landroid/os/CancellationSignal;)Landroid/database/Cursor;", False, False), ("(Landroid/net/Uri;[Ljava/lang/String;Landroid/os/Bundle;Landroid/os/CancellationSignal;)Landroid/database/Cursor;", False, False), ("(Landroid/net/Uri;[Ljava/lang/String;Ljava/lang/String;[Ljava/lang/String;Ljava/lang/String;)Landroid/database/Cursor;", False, False)])
    call = JavaMultipleMethod([("(Ljava/lang/String;Ljava/lang/String;Landroid/os/Bundle;)Landroid/os/Bundle;", False, False), ("(Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;Landroid/os/Bundle;)Landroid/os/Bundle;", False, False)])
    release = JavaMethod("()Z")
    refresh = JavaMethod("(Landroid/net/Uri;Landroid/os/Bundle;Landroid/os/CancellationSignal;)Z")
    applyBatch = JavaMultipleMethod([("(Ljava/util/ArrayList;)[Landroid/content/ContentProviderResult;", False, False), ("(Ljava/lang/String;Ljava/util/ArrayList;)[Landroid/content/ContentProviderResult;", False, False)])
    getLocalContentProvider = JavaMethod("()Landroid/content/ContentProvider;")
    openTypedAssetFile = JavaMethod("(Landroid/net/Uri;Ljava/lang/String;Landroid/os/Bundle;Landroid/os/CancellationSignal;)Landroid/content/res/AssetFileDescriptor;")
    openTypedAssetFileDescriptor = JavaMultipleMethod([("(Landroid/net/Uri;Ljava/lang/String;Landroid/os/Bundle;)Landroid/content/res/AssetFileDescriptor;", False, False), ("(Landroid/net/Uri;Ljava/lang/String;Landroid/os/Bundle;Landroid/os/CancellationSignal;)Landroid/content/res/AssetFileDescriptor;", False, False)])
    bulkInsert = JavaMethod("(Landroid/net/Uri;[Landroid/content/ContentValues;)I")
    getStreamTypes = JavaMethod("(Landroid/net/Uri;Ljava/lang/String;)[Ljava/lang/String;")
    openAssetFile = JavaMultipleMethod([("(Landroid/net/Uri;Ljava/lang/String;)Landroid/content/res/AssetFileDescriptor;", False, False), ("(Landroid/net/Uri;Ljava/lang/String;Landroid/os/CancellationSignal;)Landroid/content/res/AssetFileDescriptor;", False, False)])
    openFile = JavaMultipleMethod([("(Landroid/net/Uri;Ljava/lang/String;)Landroid/os/ParcelFileDescriptor;", False, False), ("(Landroid/net/Uri;Ljava/lang/String;Landroid/os/CancellationSignal;)Landroid/os/ParcelFileDescriptor;", False, False)])
    uncanonicalize = JavaMethod("(Landroid/net/Uri;)Landroid/net/Uri;")