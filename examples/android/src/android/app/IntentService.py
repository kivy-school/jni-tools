from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["IntentService"]

class IntentService(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/app/IntentService"
    __javaconstructor__ = [("(Ljava/lang/String;)V", False)]
    setIntentRedelivery = JavaMethod("(Z)V")
    onCreate = JavaMethod("()V")
    onStart = JavaMethod("(Landroid/content/Intent;I)V")
    onStartCommand = JavaMethod("(Landroid/content/Intent;II)I")
    onDestroy = JavaMethod("()V")
    onBind = JavaMethod("(Landroid/content/Intent;)Landroid/os/IBinder;")
    onHandleIntent = JavaMethod("(Landroid/content/Intent;)V")