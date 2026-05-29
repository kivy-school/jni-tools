from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ScheduleCustomAudienceUpdateRequest"]

class ScheduleCustomAudienceUpdateRequest(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/adservices/customaudience/ScheduleCustomAudienceUpdateRequest"
    getUpdateUri = JavaMethod("()Landroid/net/Uri;")
    getPartialCustomAudienceList = JavaMethod("()Ljava/util/List;")
    shouldReplacePendingUpdates = JavaMethod("()Z")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    toString = JavaMethod("()Ljava/lang/String;")
    hashCode = JavaMethod("()I")
    getMinDelay = JavaMethod("()Ljava/time/Duration;")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/adservices/customaudience/ScheduleCustomAudienceUpdateRequest$Builder"
        __javaconstructor__ = [("(Landroid/net/Uri;Ljava/time/Duration;Ljava/util/List;)V", False), ("(Landroid/net/Uri;Ljava/time/Duration;)V", False)]
        setMinDelay = JavaMethod("(Ljava/time/Duration;)Landroid/adservices/customaudience/ScheduleCustomAudienceUpdateRequest$Builder;")
        setShouldReplacePendingUpdates = JavaMethod("(Z)Landroid/adservices/customaudience/ScheduleCustomAudienceUpdateRequest$Builder;")
        setPartialCustomAudienceList = JavaMethod("(Ljava/util/List;)Landroid/adservices/customaudience/ScheduleCustomAudienceUpdateRequest$Builder;")
        setUpdateUri = JavaMethod("(Landroid/net/Uri;)Landroid/adservices/customaudience/ScheduleCustomAudienceUpdateRequest$Builder;")
        build = JavaMethod("()Landroid/adservices/customaudience/ScheduleCustomAudienceUpdateRequest;")