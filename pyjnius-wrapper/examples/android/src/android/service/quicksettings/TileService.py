from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["TileService"]

class TileService(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/service/quicksettings/TileService"
    __javaconstructor__ = [("()V", False)]
    ACTION_QS_TILE = JavaStaticField("Ljava/lang/String;")
    ACTION_QS_TILE_PREFERENCES = JavaStaticField("Ljava/lang/String;")
    META_DATA_ACTIVE_TILE = JavaStaticField("Ljava/lang/String;")
    META_DATA_TOGGLEABLE_TILE = JavaStaticField("Ljava/lang/String;")
    onDestroy = JavaMethod("()V")
    onTileAdded = JavaMethod("()V")
    onTileRemoved = JavaMethod("()V")
    onStartListening = JavaMethod("()V")
    onStopListening = JavaMethod("()V")
    onClick = JavaMethod("()V")
    showDialog = JavaMethod("(Landroid/app/Dialog;)V")
    unlockAndRun = JavaMethod("(Ljava/lang/Runnable;)V")
    isSecure = JavaMethod("()Z")
    isLocked = JavaMethod("()Z")
    startActivityAndCollapse = JavaMultipleMethod([("(Landroid/content/Intent;)V", False, False), ("(Landroid/app/PendingIntent;)V", False, False)])
    getQsTile = JavaMethod("()Landroid/service/quicksettings/Tile;")
    onBind = JavaMethod("(Landroid/content/Intent;)Landroid/os/IBinder;")
    requestListeningState = JavaStaticMethod("(Landroid/content/Context;Landroid/content/ComponentName;)V")