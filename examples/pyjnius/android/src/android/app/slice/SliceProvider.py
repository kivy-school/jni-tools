from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["SliceProvider"]

class SliceProvider(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/app/slice/SliceProvider"
    __javaconstructor__ = [("()V", False), ("([Ljava/lang/String;)V", True)]
    SLICE_TYPE = JavaStaticField("Ljava/lang/String;")
    TRIM_MEMORY_BACKGROUND = JavaStaticField("I")
    TRIM_MEMORY_COMPLETE = JavaStaticField("I")
    TRIM_MEMORY_MODERATE = JavaStaticField("I")
    TRIM_MEMORY_RUNNING_CRITICAL = JavaStaticField("I")
    TRIM_MEMORY_RUNNING_LOW = JavaStaticField("I")
    TRIM_MEMORY_RUNNING_MODERATE = JavaStaticField("I")
    TRIM_MEMORY_UI_HIDDEN = JavaStaticField("I")
    onCreatePermissionRequest = JavaMethod("(Landroid/net/Uri;)Landroid/app/PendingIntent;")
    onMapIntentToUri = JavaMethod("(Landroid/content/Intent;)Landroid/net/Uri;")
    onBindSlice = JavaMethod("(Landroid/net/Uri;Ljava/util/Set;)Landroid/app/slice/Slice;")
    onGetSliceDescendants = JavaMethod("(Landroid/net/Uri;)Ljava/util/Collection;")
    onSlicePinned = JavaMethod("(Landroid/net/Uri;)V")
    onSliceUnpinned = JavaMethod("(Landroid/net/Uri;)V")
    update = JavaMethod("(Landroid/net/Uri;Landroid/content/ContentValues;Ljava/lang/String;[Ljava/lang/String;)I")
    insert = JavaMethod("(Landroid/net/Uri;Landroid/content/ContentValues;)Landroid/net/Uri;")
    getType = JavaMethod("(Landroid/net/Uri;)Ljava/lang/String;")
    delete = JavaMethod("(Landroid/net/Uri;Ljava/lang/String;[Ljava/lang/String;)I")
    query = JavaMultipleMethod([("(Landroid/net/Uri;[Ljava/lang/String;Ljava/lang/String;[Ljava/lang/String;Ljava/lang/String;Landroid/os/CancellationSignal;)Landroid/database/Cursor;", False, False), ("(Landroid/net/Uri;[Ljava/lang/String;Landroid/os/Bundle;Landroid/os/CancellationSignal;)Landroid/database/Cursor;", False, False), ("(Landroid/net/Uri;[Ljava/lang/String;Ljava/lang/String;[Ljava/lang/String;Ljava/lang/String;)Landroid/database/Cursor;", False, False)])
    call = JavaMethod("(Ljava/lang/String;Ljava/lang/String;Landroid/os/Bundle;)Landroid/os/Bundle;")
    attachInfo = JavaMethod("(Landroid/content/Context;Landroid/content/pm/ProviderInfo;)V")