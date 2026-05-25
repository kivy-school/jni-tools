from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["TaskStackBuilder"]

class TaskStackBuilder(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/app/TaskStackBuilder"
    create = JavaStaticMethod("(Landroid/content/Context;)Landroid/app/TaskStackBuilder;")
    addNextIntent = JavaMethod("(Landroid/content/Intent;)Landroid/app/TaskStackBuilder;")
    addNextIntentWithParentStack = JavaMethod("(Landroid/content/Intent;)Landroid/app/TaskStackBuilder;")
    addParentStack = JavaMultipleMethod([("(Landroid/app/Activity;)Landroid/app/TaskStackBuilder;", False, False), ("(Ljava/lang/Class;)Landroid/app/TaskStackBuilder;", False, False), ("(Landroid/content/ComponentName;)Landroid/app/TaskStackBuilder;", False, False)])
    getIntentCount = JavaMethod("()I")
    editIntentAt = JavaMethod("(I)Landroid/content/Intent;")
    startActivities = JavaMultipleMethod([("()V", False, False), ("(Landroid/os/Bundle;)V", False, False)])
    getPendingIntent = JavaMultipleMethod([("(II)Landroid/app/PendingIntent;", False, False), ("(IILandroid/os/Bundle;)Landroid/app/PendingIntent;", False, False)])
    getIntents = JavaMethod("()[Landroid/content/Intent;")