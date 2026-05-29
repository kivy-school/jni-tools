from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["NetworkStatsManager"]

class NetworkStatsManager(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/app/usage/NetworkStatsManager"
    queryDetailsForUid = JavaMethod("(ILjava/lang/String;JJI)Landroid/app/usage/NetworkStats;")
    queryDetails = JavaMethod("(ILjava/lang/String;JJ)Landroid/app/usage/NetworkStats;")
    querySummary = JavaMethod("(ILjava/lang/String;JJ)Landroid/app/usage/NetworkStats;")
    registerUsageCallback = JavaMultipleMethod([("(ILjava/lang/String;JLandroid/app/usage/NetworkStatsManager$UsageCallback;)V", False, False), ("(ILjava/lang/String;JLandroid/app/usage/NetworkStatsManager$UsageCallback;Landroid/os/Handler;)V", False, False)])
    unregisterUsageCallback = JavaMethod("(Landroid/app/usage/NetworkStatsManager$UsageCallback;)V")
    queryDetailsForUidTag = JavaMethod("(ILjava/lang/String;JJII)Landroid/app/usage/NetworkStats;")
    querySummaryForDevice = JavaMethod("(ILjava/lang/String;JJ)Landroid/app/usage/NetworkStats$Bucket;")
    querySummaryForUser = JavaMethod("(ILjava/lang/String;JJ)Landroid/app/usage/NetworkStats$Bucket;")
    queryDetailsForUidTagState = JavaMethod("(ILjava/lang/String;JJIII)Landroid/app/usage/NetworkStats;")

    class UsageCallback(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/app/usage/NetworkStatsManager$UsageCallback"
        __javaconstructor__ = [("()V", False)]
        onThresholdReached = JavaMethod("(ILjava/lang/String;)V")