from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["TaskInfo"]

class TaskInfo(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/app/TaskInfo"
    baseActivity = JavaField("Landroid/content/ComponentName;")
    baseIntent = JavaField("Landroid/content/Intent;")
    isRunning = JavaField("Z")
    numActivities = JavaField("I")
    origActivity = JavaField("Landroid/content/ComponentName;")
    taskDescription = JavaField("Landroid/app/ActivityManager$TaskDescription;")
    taskId = JavaField("I")
    topActivity = JavaField("Landroid/content/ComponentName;")
    isVisible = JavaMethod("()Z")
    toString = JavaMethod("()Ljava/lang/String;")