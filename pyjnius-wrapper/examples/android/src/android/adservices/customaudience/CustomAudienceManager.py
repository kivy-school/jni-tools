from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["CustomAudienceManager"]

class CustomAudienceManager(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/adservices/customaudience/CustomAudienceManager"
    get = JavaStaticMethod("(Landroid/content/Context;)Landroid/adservices/customaudience/CustomAudienceManager;")
    getTestCustomAudienceManager = JavaMethod("()Landroid/adservices/customaudience/TestCustomAudienceManager;")
    joinCustomAudience = JavaMethod("(Landroid/adservices/customaudience/JoinCustomAudienceRequest;Ljava/util/concurrent/Executor;Landroid/os/OutcomeReceiver;)V")
    fetchAndJoinCustomAudience = JavaMethod("(Landroid/adservices/customaudience/FetchAndJoinCustomAudienceRequest;Ljava/util/concurrent/Executor;Landroid/os/OutcomeReceiver;)V")
    leaveCustomAudience = JavaMethod("(Landroid/adservices/customaudience/LeaveCustomAudienceRequest;Ljava/util/concurrent/Executor;Landroid/os/OutcomeReceiver;)V")
    scheduleCustomAudienceUpdate = JavaMethod("(Landroid/adservices/customaudience/ScheduleCustomAudienceUpdateRequest;Ljava/util/concurrent/Executor;Landroid/adservices/common/AdServicesOutcomeReceiver;)V")