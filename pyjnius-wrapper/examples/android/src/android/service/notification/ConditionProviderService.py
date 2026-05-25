from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ConditionProviderService"]

class ConditionProviderService(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/service/notification/ConditionProviderService"
    __javaconstructor__ = [("()V", False)]
    EXTRA_RULE_ID = JavaStaticField("Ljava/lang/String;")
    META_DATA_CONFIGURATION_ACTIVITY = JavaStaticField("Ljava/lang/String;")
    META_DATA_RULE_INSTANCE_LIMIT = JavaStaticField("Ljava/lang/String;")
    META_DATA_RULE_TYPE = JavaStaticField("Ljava/lang/String;")
    SERVICE_INTERFACE = JavaStaticField("Ljava/lang/String;")
    onConnected = JavaMethod("()V")
    onRequestConditions = JavaMethod("(I)V")
    onSubscribe = JavaMethod("(Landroid/net/Uri;)V")
    onUnsubscribe = JavaMethod("(Landroid/net/Uri;)V")
    requestRebind = JavaStaticMethod("(Landroid/content/ComponentName;)V")
    requestUnbind = JavaMethod("()V")
    notifyCondition = JavaMethod("(Landroid/service/notification/Condition;)V")
    notifyConditions = JavaMethod("([Landroid/service/notification/Condition;)V", varargs=True)
    onBind = JavaMethod("(Landroid/content/Intent;)Landroid/os/IBinder;")