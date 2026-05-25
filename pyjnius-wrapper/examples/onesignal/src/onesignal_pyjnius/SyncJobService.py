from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["SyncJobService"]

class SyncJobService(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/SyncJobService"
    __javaconstructor__ = [("()V", False)]
    onStartJob = JavaMethod("(Landroid/app/job/JobParameters;)Z")
    onStopJob = JavaMethod("(Landroid/app/job/JobParameters;)Z")