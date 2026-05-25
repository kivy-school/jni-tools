from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["StorageStatsManager"]

class StorageStatsManager(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/app/usage/StorageStatsManager"
    getTotalBytes = JavaMethod("(Ljava/util/UUID;)J")
    getFreeBytes = JavaMethod("(Ljava/util/UUID;)J")
    queryStatsForPackage = JavaMethod("(Ljava/util/UUID;Ljava/lang/String;Landroid/os/UserHandle;)Landroid/app/usage/StorageStats;")
    queryStatsForUid = JavaMethod("(Ljava/util/UUID;I)Landroid/app/usage/StorageStats;")
    queryStatsForUser = JavaMethod("(Ljava/util/UUID;Landroid/os/UserHandle;)Landroid/app/usage/StorageStats;")
    queryExternalStatsForUser = JavaMethod("(Ljava/util/UUID;Landroid/os/UserHandle;)Landroid/app/usage/ExternalStorageStats;")