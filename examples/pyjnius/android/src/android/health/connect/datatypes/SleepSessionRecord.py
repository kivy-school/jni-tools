from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["SleepSessionRecord"]

class SleepSessionRecord(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/health/connect/datatypes/SleepSessionRecord"
    SLEEP_DURATION_TOTAL = JavaStaticField("Landroid/health/connect/datatypes/AggregationType;")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")
    getTitle = JavaMethod("()Ljava/lang/CharSequence;")
    getStages = JavaMethod("()Ljava/util/List;")
    getNotes = JavaMethod("()Ljava/lang/CharSequence;")

    class StageType(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/health/connect/datatypes/SleepSessionRecord$StageType"
        STAGE_TYPE_AWAKE = JavaStaticField("I")
        STAGE_TYPE_AWAKE_IN_BED = JavaStaticField("I")
        STAGE_TYPE_AWAKE_OUT_OF_BED = JavaStaticField("I")
        STAGE_TYPE_SLEEPING = JavaStaticField("I")
        STAGE_TYPE_SLEEPING_DEEP = JavaStaticField("I")
        STAGE_TYPE_SLEEPING_LIGHT = JavaStaticField("I")
        STAGE_TYPE_SLEEPING_REM = JavaStaticField("I")
        STAGE_TYPE_UNKNOWN = JavaStaticField("I")

    class Stage(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/health/connect/datatypes/SleepSessionRecord$Stage"
        __javaconstructor__ = [("(Ljava/time/Instant;Ljava/time/Instant;I)V", False)]
        equals = JavaMethod("(Ljava/lang/Object;)Z")
        hashCode = JavaMethod("()I")
        getType = JavaMethod("()I")
        getStartTime = JavaMethod("()Ljava/time/Instant;")
        getEndTime = JavaMethod("()Ljava/time/Instant;")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/health/connect/datatypes/SleepSessionRecord$Builder"
        __javaconstructor__ = [("(Landroid/health/connect/datatypes/Metadata;Ljava/time/Instant;Ljava/time/Instant;)V", False)]
        setTitle = JavaMethod("(Ljava/lang/CharSequence;)Landroid/health/connect/datatypes/SleepSessionRecord$Builder;")
        setStages = JavaMethod("(Ljava/util/List;)Landroid/health/connect/datatypes/SleepSessionRecord$Builder;")
        build = JavaMethod("()Landroid/health/connect/datatypes/SleepSessionRecord;")
        clearEndZoneOffset = JavaMethod("()Landroid/health/connect/datatypes/SleepSessionRecord$Builder;")
        clearStartZoneOffset = JavaMethod("()Landroid/health/connect/datatypes/SleepSessionRecord$Builder;")
        setEndZoneOffset = JavaMethod("(Ljava/time/ZoneOffset;)Landroid/health/connect/datatypes/SleepSessionRecord$Builder;")
        setNotes = JavaMethod("(Ljava/lang/CharSequence;)Landroid/health/connect/datatypes/SleepSessionRecord$Builder;")
        setStartZoneOffset = JavaMethod("(Ljava/time/ZoneOffset;)Landroid/health/connect/datatypes/SleepSessionRecord$Builder;")