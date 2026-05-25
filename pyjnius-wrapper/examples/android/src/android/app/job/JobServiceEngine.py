from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["JobServiceEngine"]

class JobServiceEngine(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/app/job/JobServiceEngine"
    __javaconstructor__ = [("(Landroid/app/Service;)V", False)]
    getBinder = JavaMethod("()Landroid/os/IBinder;")
    onStartJob = JavaMethod("(Landroid/app/job/JobParameters;)Z")
    onStopJob = JavaMethod("(Landroid/app/job/JobParameters;)Z")
    jobFinished = JavaMethod("(Landroid/app/job/JobParameters;Z)V")
    onNetworkChanged = JavaMethod("(Landroid/app/job/JobParameters;)V")
    updateTransferredNetworkBytes = JavaMethod("(Landroid/app/job/JobParameters;Landroid/app/job/JobWorkItem;JJ)V")
    updateEstimatedNetworkBytes = JavaMethod("(Landroid/app/job/JobParameters;Landroid/app/job/JobWorkItem;JJ)V")
    setNotification = JavaMethod("(Landroid/app/job/JobParameters;ILandroid/app/Notification;I)V")