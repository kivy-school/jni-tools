from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["SliceProvider"]

class SliceProvider(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/app/slice/SliceProvider"
    __javaconstructor__ = [("([Ljava/lang/String;)V", True), ("()V", False)]
    SLICE_TYPE = JavaStaticField("Ljava/lang/String;")
    attachInfo = JavaMethod("(Landroid/content/Context;Landroid/content/pm/ProviderInfo;)V")
    onBindSlice = JavaMethod("(Landroid/net/Uri;Ljava/util/Set;)Landroid/app/slice/Slice;")
    onSlicePinned = JavaMethod("(Landroid/net/Uri;)V")
    onSliceUnpinned = JavaMethod("(Landroid/net/Uri;)V")
    onGetSliceDescendants = JavaMethod("(Landroid/net/Uri;)Ljava/util/Collection;")
    onMapIntentToUri = JavaMethod("(Landroid/content/Intent;)Landroid/net/Uri;")
    onCreatePermissionRequest = JavaMethod("(Landroid/net/Uri;)Landroid/app/PendingIntent;")
    update = JavaMethod("(Landroid/net/Uri;Landroid/content/ContentValues;Ljava/lang/String;[Ljava/lang/String;)I")
    delete = JavaMethod("(Landroid/net/Uri;Ljava/lang/String;[Ljava/lang/String;)I")
    query = JavaMultipleMethod([("(Landroid/net/Uri;[Ljava/lang/String;Ljava/lang/String;[Ljava/lang/String;Ljava/lang/String;)Landroid/database/Cursor;", False, False), ("(Landroid/net/Uri;[Ljava/lang/String;Ljava/lang/String;[Ljava/lang/String;Ljava/lang/String;Landroid/os/CancellationSignal;)Landroid/database/Cursor;", False, False), ("(Landroid/net/Uri;[Ljava/lang/String;Landroid/os/Bundle;Landroid/os/CancellationSignal;)Landroid/database/Cursor;", False, False)])
    insert = JavaMethod("(Landroid/net/Uri;Landroid/content/ContentValues;)Landroid/net/Uri;")
    getType = JavaMethod("(Landroid/net/Uri;)Ljava/lang/String;")
    call = JavaMethod("(Ljava/lang/String;Ljava/lang/String;Landroid/os/Bundle;)Landroid/os/Bundle;")