from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["UsageStatsManager"]

class UsageStatsManager(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/app/usage/UsageStatsManager"
    EXTRA_EVENT_ACTION = JavaStaticField("Ljava/lang/String;")
    EXTRA_EVENT_CATEGORY = JavaStaticField("Ljava/lang/String;")
    INTERVAL_BEST = JavaStaticField("I")
    INTERVAL_DAILY = JavaStaticField("I")
    INTERVAL_MONTHLY = JavaStaticField("I")
    INTERVAL_WEEKLY = JavaStaticField("I")
    INTERVAL_YEARLY = JavaStaticField("I")
    STANDBY_BUCKET_ACTIVE = JavaStaticField("I")
    STANDBY_BUCKET_FREQUENT = JavaStaticField("I")
    STANDBY_BUCKET_RARE = JavaStaticField("I")
    STANDBY_BUCKET_RESTRICTED = JavaStaticField("I")
    STANDBY_BUCKET_WORKING_SET = JavaStaticField("I")
    queryUsageStats = JavaMethod("(IJJ)Ljava/util/List;")
    queryConfigurations = JavaMethod("(IJJ)Ljava/util/List;")
    queryEventStats = JavaMethod("(IJJ)Ljava/util/List;")
    queryEvents = JavaMultipleMethod([("(JJ)Landroid/app/usage/UsageEvents;", False, False), ("(Landroid/app/usage/UsageEventsQuery;)Landroid/app/usage/UsageEvents;", False, False)])
    queryEventsForSelf = JavaMethod("(JJ)Landroid/app/usage/UsageEvents;")
    queryAndAggregateUsageStats = JavaMethod("(JJ)Ljava/util/Map;")
    isAppInactive = JavaMethod("(Ljava/lang/String;)Z")
    getAppStandbyBucket = JavaMethod("()I")