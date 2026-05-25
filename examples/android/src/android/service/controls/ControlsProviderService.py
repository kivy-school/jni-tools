from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ControlsProviderService"]

class ControlsProviderService(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/service/controls/ControlsProviderService"
    __javaconstructor__ = [("()V", False)]
    CONTROLS_SURFACE_ACTIVITY_PANEL = JavaStaticField("I")
    CONTROLS_SURFACE_DREAM = JavaStaticField("I")
    EXTRA_CONTROLS_SURFACE = JavaStaticField("Ljava/lang/String;")
    EXTRA_LOCKSCREEN_ALLOW_TRIVIAL_CONTROLS = JavaStaticField("Ljava/lang/String;")
    META_DATA_PANEL_ACTIVITY = JavaStaticField("Ljava/lang/String;")
    SERVICE_CONTROLS = JavaStaticField("Ljava/lang/String;")
    TAG = JavaStaticField("Ljava/lang/String;")
    createPublisherForAllAvailable = JavaMethod("()Ljava/util/concurrent/Flow$Publisher;")
    createPublisherForSuggested = JavaMethod("()Ljava/util/concurrent/Flow$Publisher;")
    createPublisherFor = JavaMethod("(Ljava/util/List;)Ljava/util/concurrent/Flow$Publisher;")
    performControlAction = JavaMethod("(Ljava/lang/String;Landroid/service/controls/actions/ControlAction;Ljava/util/function/Consumer;)V")
    onBind = JavaMethod("(Landroid/content/Intent;)Landroid/os/IBinder;")
    onUnbind = JavaMethod("(Landroid/content/Intent;)Z")
    requestAddControl = JavaStaticMethod("(Landroid/content/Context;Landroid/content/ComponentName;Landroid/service/controls/Control;)V")