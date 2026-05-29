from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["JobServiceEngine"]

class JobServiceEngine(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/app/job/JobServiceEngine"
    __javaconstructor__ = [("(Landroid/app/Service;)V", False)]
    jobFinished = JavaMethod("(Landroid/app/job/JobParameters;Z)V")
    setNotification = JavaMethod("(Landroid/app/job/JobParameters;ILandroid/app/Notification;I)V")
    updateEstimatedNetworkBytes = JavaMethod("(Landroid/app/job/JobParameters;Landroid/app/job/JobWorkItem;JJ)V")
    updateTransferredNetworkBytes = JavaMethod("(Landroid/app/job/JobParameters;Landroid/app/job/JobWorkItem;JJ)V")
    onStartJob = JavaMethod("(Landroid/app/job/JobParameters;)Z")
    onStopJob = JavaMethod("(Landroid/app/job/JobParameters;)Z")
    onNetworkChanged = JavaMethod("(Landroid/app/job/JobParameters;)V")
    getBinder = JavaMethod("()Landroid/os/IBinder;")