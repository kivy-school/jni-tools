from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ScheduleCustomAudienceUpdateRequest"]

class ScheduleCustomAudienceUpdateRequest(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/adservices/customaudience/ScheduleCustomAudienceUpdateRequest"
    getUpdateUri = JavaMethod("()Landroid/net/Uri;")
    getMinDelay = JavaMethod("()Ljava/time/Duration;")
    getPartialCustomAudienceList = JavaMethod("()Ljava/util/List;")
    hashCode = JavaMethod("()I")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    toString = JavaMethod("()Ljava/lang/String;")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/adservices/customaudience/ScheduleCustomAudienceUpdateRequest/Builder"
        __javaconstructor__ = [("(Landroid/net/Uri;Ljava/time/Duration;Ljava/util/List;)V", False)]
        setUpdateUri = JavaMethod("(Landroid/net/Uri;)Landroid/adservices/customaudience/ScheduleCustomAudienceUpdateRequest$Builder;")
        setMinDelay = JavaMethod("(Ljava/time/Duration;)Landroid/adservices/customaudience/ScheduleCustomAudienceUpdateRequest$Builder;")
        setPartialCustomAudienceList = JavaMethod("(Ljava/util/List;)Landroid/adservices/customaudience/ScheduleCustomAudienceUpdateRequest$Builder;")
        build = JavaMethod("()Landroid/adservices/customaudience/ScheduleCustomAudienceUpdateRequest;")