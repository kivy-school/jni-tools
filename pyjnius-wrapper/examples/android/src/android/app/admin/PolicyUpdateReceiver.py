from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["PolicyUpdateReceiver"]

class PolicyUpdateReceiver(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/app/admin/PolicyUpdateReceiver"
    __javaconstructor__ = [("()V", False)]
    ACTION_DEVICE_POLICY_CHANGED = JavaStaticField("Ljava/lang/String;")
    ACTION_DEVICE_POLICY_SET_RESULT = JavaStaticField("Ljava/lang/String;")
    EXTRA_ACCOUNT_TYPE = JavaStaticField("Ljava/lang/String;")
    EXTRA_INTENT_FILTER = JavaStaticField("Ljava/lang/String;")
    EXTRA_PACKAGE_NAME = JavaStaticField("Ljava/lang/String;")
    EXTRA_PERMISSION_NAME = JavaStaticField("Ljava/lang/String;")
    onReceive = JavaMethod("(Landroid/content/Context;Landroid/content/Intent;)V")
    onPolicySetResult = JavaMethod("(Landroid/content/Context;Ljava/lang/String;Landroid/os/Bundle;Landroid/app/admin/TargetUser;Landroid/app/admin/PolicyUpdateResult;)V")
    onPolicyChanged = JavaMethod("(Landroid/content/Context;Ljava/lang/String;Landroid/os/Bundle;Landroid/app/admin/TargetUser;Landroid/app/admin/PolicyUpdateResult;)V")