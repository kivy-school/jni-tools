from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["JobService"]

class JobService(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/app/job/JobService"
    __javaconstructor__ = [("()V", False)]
    JOB_END_NOTIFICATION_POLICY_DETACH = JavaStaticField("I")
    JOB_END_NOTIFICATION_POLICY_REMOVE = JavaStaticField("I")
    PERMISSION_BIND = JavaStaticField("Ljava/lang/String;")
    onBind = JavaMethod("(Landroid/content/Intent;)Landroid/os/IBinder;")
    jobFinished = JavaMethod("(Landroid/app/job/JobParameters;Z)V")
    onStartJob = JavaMethod("(Landroid/app/job/JobParameters;)Z")
    onStopJob = JavaMethod("(Landroid/app/job/JobParameters;)Z")
    onNetworkChanged = JavaMethod("(Landroid/app/job/JobParameters;)V")
    updateEstimatedNetworkBytes = JavaMultipleMethod([("(Landroid/app/job/JobParameters;JJ)V", False, False), ("(Landroid/app/job/JobParameters;Landroid/app/job/JobWorkItem;JJ)V", False, False)])
    updateTransferredNetworkBytes = JavaMultipleMethod([("(Landroid/app/job/JobParameters;JJ)V", False, False), ("(Landroid/app/job/JobParameters;Landroid/app/job/JobWorkItem;JJ)V", False, False)])
    setNotification = JavaMethod("(Landroid/app/job/JobParameters;ILandroid/app/Notification;I)V")