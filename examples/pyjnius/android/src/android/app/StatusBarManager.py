from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["StatusBarManager"]

class StatusBarManager(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/app/StatusBarManager"
    TILE_ADD_REQUEST_ERROR_APP_NOT_IN_FOREGROUND = JavaStaticField("I")
    TILE_ADD_REQUEST_ERROR_BAD_COMPONENT = JavaStaticField("I")
    TILE_ADD_REQUEST_ERROR_MISMATCHED_PACKAGE = JavaStaticField("I")
    TILE_ADD_REQUEST_ERROR_NOT_CURRENT_USER = JavaStaticField("I")
    TILE_ADD_REQUEST_ERROR_NO_STATUS_BAR_SERVICE = JavaStaticField("I")
    TILE_ADD_REQUEST_ERROR_REQUEST_IN_PROGRESS = JavaStaticField("I")
    TILE_ADD_REQUEST_RESULT_TILE_ADDED = JavaStaticField("I")
    TILE_ADD_REQUEST_RESULT_TILE_ALREADY_ADDED = JavaStaticField("I")
    TILE_ADD_REQUEST_RESULT_TILE_NOT_ADDED = JavaStaticField("I")
    canLaunchCaptureContentActivityForNote = JavaMethod("(Landroid/app/Activity;)Z")
    requestAddTileService = JavaMethod("(Landroid/content/ComponentName;Ljava/lang/CharSequence;Landroid/graphics/drawable/Icon;Ljava/util/concurrent/Executor;Ljava/util/function/Consumer;)V")