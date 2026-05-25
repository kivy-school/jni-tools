from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["OfflineNotificationPoster"]

class OfflineNotificationPoster(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/google/android/gms/ads/internal/offline/buffering/OfflineNotificationPoster"
    __javaconstructor__ = [("(Landroid/content/Context;Landroidx/work/WorkerParameters;)V", False)]
    doWork = JavaMethod("()Landroidx/work/ListenableWorker$Result;")