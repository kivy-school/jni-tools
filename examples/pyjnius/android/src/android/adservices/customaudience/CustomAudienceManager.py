from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["CustomAudienceManager"]

class CustomAudienceManager(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/adservices/customaudience/CustomAudienceManager"
    joinCustomAudience = JavaMethod("(Landroid/adservices/customaudience/JoinCustomAudienceRequest;Ljava/util/concurrent/Executor;Landroid/os/OutcomeReceiver;)V")
    fetchAndJoinCustomAudience = JavaMethod("(Landroid/adservices/customaudience/FetchAndJoinCustomAudienceRequest;Ljava/util/concurrent/Executor;Landroid/os/OutcomeReceiver;)V")
    getTestCustomAudienceManager = JavaMethod("()Landroid/adservices/customaudience/TestCustomAudienceManager;")
    leaveCustomAudience = JavaMethod("(Landroid/adservices/customaudience/LeaveCustomAudienceRequest;Ljava/util/concurrent/Executor;Landroid/os/OutcomeReceiver;)V")
    get = JavaStaticMethod("(Landroid/content/Context;)Landroid/adservices/customaudience/CustomAudienceManager;")
    scheduleCustomAudienceUpdate = JavaMethod("(Landroid/adservices/customaudience/ScheduleCustomAudienceUpdateRequest;Ljava/util/concurrent/Executor;Landroid/adservices/common/AdServicesOutcomeReceiver;)V")