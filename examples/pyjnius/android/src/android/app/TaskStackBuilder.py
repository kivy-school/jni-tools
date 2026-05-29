from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["TaskStackBuilder"]

class TaskStackBuilder(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/app/TaskStackBuilder"
    addParentStack = JavaMultipleMethod([("(Landroid/app/Activity;)Landroid/app/TaskStackBuilder;", False, False), ("(Ljava/lang/Class;)Landroid/app/TaskStackBuilder;", False, False), ("(Landroid/content/ComponentName;)Landroid/app/TaskStackBuilder;", False, False)])
    addNextIntentWithParentStack = JavaMethod("(Landroid/content/Intent;)Landroid/app/TaskStackBuilder;")
    addNextIntent = JavaMethod("(Landroid/content/Intent;)Landroid/app/TaskStackBuilder;")
    editIntentAt = JavaMethod("(I)Landroid/content/Intent;")
    getIntentCount = JavaMethod("()I")
    create = JavaStaticMethod("(Landroid/content/Context;)Landroid/app/TaskStackBuilder;")
    getIntents = JavaMethod("()[Landroid/content/Intent;")
    getPendingIntent = JavaMultipleMethod([("(IILandroid/os/Bundle;)Landroid/app/PendingIntent;", False, False), ("(II)Landroid/app/PendingIntent;", False, False)])
    startActivities = JavaMultipleMethod([("()V", False, False), ("(Landroid/os/Bundle;)V", False, False)])