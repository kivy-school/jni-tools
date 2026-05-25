from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Service"]

class Service(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/app/Service"
    __javaconstructor__ = [("()V", False)]
    START_CONTINUATION_MASK = JavaStaticField("I")
    START_FLAG_REDELIVERY = JavaStaticField("I")
    START_FLAG_RETRY = JavaStaticField("I")
    START_NOT_STICKY = JavaStaticField("I")
    START_REDELIVER_INTENT = JavaStaticField("I")
    START_STICKY = JavaStaticField("I")
    START_STICKY_COMPATIBILITY = JavaStaticField("I")
    STOP_FOREGROUND_DETACH = JavaStaticField("I")
    STOP_FOREGROUND_LEGACY = JavaStaticField("I")
    STOP_FOREGROUND_REMOVE = JavaStaticField("I")
    getApplication = JavaMethod("()Landroid/app/Application;")
    onCreate = JavaMethod("()V")
    onStart = JavaMethod("(Landroid/content/Intent;I)V")
    onStartCommand = JavaMethod("(Landroid/content/Intent;II)I")
    onDestroy = JavaMethod("()V")
    onConfigurationChanged = JavaMethod("(Landroid/content/res/Configuration;)V")
    onLowMemory = JavaMethod("()V")
    onTrimMemory = JavaMethod("(I)V")
    onBind = JavaMethod("(Landroid/content/Intent;)Landroid/os/IBinder;")
    onUnbind = JavaMethod("(Landroid/content/Intent;)Z")
    onRebind = JavaMethod("(Landroid/content/Intent;)V")
    onTaskRemoved = JavaMethod("(Landroid/content/Intent;)V")
    stopSelf = JavaMultipleMethod([("()V", False, False), ("(I)V", False, False)])
    stopSelfResult = JavaMethod("(I)Z")
    startForeground = JavaMultipleMethod([("(ILandroid/app/Notification;)V", False, False), ("(ILandroid/app/Notification;I)V", False, False)])
    stopForeground = JavaMultipleMethod([("(Z)V", False, False), ("(I)V", False, False)])
    getForegroundServiceType = JavaMethod("()I")
    dump = JavaMethod("(Ljava/io/FileDescriptor;Ljava/io/PrintWriter;[Ljava/lang/String;)V")
    attachBaseContext = JavaMethod("(Landroid/content/Context;)V")
    onTimeout = JavaMultipleMethod([("(I)V", False, False), ("(II)V", False, False)])