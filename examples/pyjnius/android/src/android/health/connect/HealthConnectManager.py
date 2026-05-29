from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["HealthConnectManager"]

class HealthConnectManager(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/health/connect/HealthConnectManager"
    ACTION_MANAGE_HEALTH_PERMISSIONS = JavaStaticField("Ljava/lang/String;")
    ACTION_REQUEST_EXERCISE_ROUTE = JavaStaticField("Ljava/lang/String;")
    CATEGORY_HEALTH_PERMISSIONS = JavaStaticField("Ljava/lang/String;")
    EXTRA_EXERCISE_ROUTE = JavaStaticField("Ljava/lang/String;")
    EXTRA_SESSION_ID = JavaStaticField("Ljava/lang/String;")
    getChangeLogToken = JavaMethod("(Landroid/health/connect/changelog/ChangeLogTokenRequest;Ljava/util/concurrent/Executor;Landroid/os/OutcomeReceiver;)V")
    getChangeLogs = JavaMethod("(Landroid/health/connect/changelog/ChangeLogsRequest;Ljava/util/concurrent/Executor;Landroid/os/OutcomeReceiver;)V")
    aggregate = JavaMethod("(Landroid/health/connect/AggregateRecordsRequest;Ljava/util/concurrent/Executor;Landroid/os/OutcomeReceiver;)V")
    readRecords = JavaMethod("(Landroid/health/connect/ReadRecordsRequest;Ljava/util/concurrent/Executor;Landroid/os/OutcomeReceiver;)V")
    deleteRecords = JavaMultipleMethod([("(Ljava/lang/Class;Landroid/health/connect/TimeRangeFilter;Ljava/util/concurrent/Executor;Landroid/os/OutcomeReceiver;)V", False, False), ("(Ljava/util/List;Ljava/util/concurrent/Executor;Landroid/os/OutcomeReceiver;)V", False, False)])
    insertRecords = JavaMethod("(Ljava/util/List;Ljava/util/concurrent/Executor;Landroid/os/OutcomeReceiver;)V")
    updateRecords = JavaMethod("(Ljava/util/List;Ljava/util/concurrent/Executor;Landroid/os/OutcomeReceiver;)V")
    aggregateGroupByDuration = JavaMethod("(Landroid/health/connect/AggregateRecordsRequest;Ljava/time/Duration;Ljava/util/concurrent/Executor;Landroid/os/OutcomeReceiver;)V")
    aggregateGroupByPeriod = JavaMethod("(Landroid/health/connect/AggregateRecordsRequest;Ljava/time/Period;Ljava/util/concurrent/Executor;Landroid/os/OutcomeReceiver;)V")
    createMedicalDataSource = JavaMethod("(Landroid/health/connect/CreateMedicalDataSourceRequest;Ljava/util/concurrent/Executor;Landroid/os/OutcomeReceiver;)V")
    deleteMedicalDataSourceWithData = JavaMethod("(Ljava/lang/String;Ljava/util/concurrent/Executor;Landroid/os/OutcomeReceiver;)V")
    deleteMedicalResources = JavaMultipleMethod([("(Ljava/util/List;Ljava/util/concurrent/Executor;Landroid/os/OutcomeReceiver;)V", False, False), ("(Landroid/health/connect/DeleteMedicalResourcesRequest;Ljava/util/concurrent/Executor;Landroid/os/OutcomeReceiver;)V", False, False)])
    getMedicalDataSources = JavaMultipleMethod([("(Landroid/health/connect/GetMedicalDataSourcesRequest;Ljava/util/concurrent/Executor;Landroid/os/OutcomeReceiver;)V", False, False), ("(Ljava/util/List;Ljava/util/concurrent/Executor;Landroid/os/OutcomeReceiver;)V", False, False)])
    readMedicalResources = JavaMultipleMethod([("(Ljava/util/List;Ljava/util/concurrent/Executor;Landroid/os/OutcomeReceiver;)V", False, False), ("(Landroid/health/connect/ReadMedicalResourcesRequest;Ljava/util/concurrent/Executor;Landroid/os/OutcomeReceiver;)V", False, False)])
    upsertMedicalResources = JavaMethod("(Ljava/util/List;Ljava/util/concurrent/Executor;Landroid/os/OutcomeReceiver;)V")