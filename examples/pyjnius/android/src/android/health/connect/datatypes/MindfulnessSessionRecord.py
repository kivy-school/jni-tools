from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["MindfulnessSessionRecord"]

class MindfulnessSessionRecord(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/health/connect/datatypes/MindfulnessSessionRecord"
    MINDFULNESS_DURATION_TOTAL = JavaStaticField("Landroid/health/connect/datatypes/AggregationType;")
    MINDFULNESS_SESSION_TYPE_BREATHING = JavaStaticField("I")
    MINDFULNESS_SESSION_TYPE_MEDITATION = JavaStaticField("I")
    MINDFULNESS_SESSION_TYPE_MOVEMENT = JavaStaticField("I")
    MINDFULNESS_SESSION_TYPE_MUSIC = JavaStaticField("I")
    MINDFULNESS_SESSION_TYPE_OTHER = JavaStaticField("I")
    MINDFULNESS_SESSION_TYPE_UNGUIDED = JavaStaticField("I")
    MINDFULNESS_SESSION_TYPE_UNKNOWN = JavaStaticField("I")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")
    getTitle = JavaMethod("()Ljava/lang/CharSequence;")
    getNotes = JavaMethod("()Ljava/lang/CharSequence;")
    getMindfulnessSessionType = JavaMethod("()I")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/health/connect/datatypes/MindfulnessSessionRecord$Builder"
        __javaconstructor__ = [("(Landroid/health/connect/datatypes/Metadata;Ljava/time/Instant;Ljava/time/Instant;I)V", False)]
        setTitle = JavaMethod("(Ljava/lang/CharSequence;)Landroid/health/connect/datatypes/MindfulnessSessionRecord$Builder;")
        build = JavaMethod("()Landroid/health/connect/datatypes/MindfulnessSessionRecord;")
        setEndZoneOffset = JavaMethod("(Ljava/time/ZoneOffset;)Landroid/health/connect/datatypes/MindfulnessSessionRecord$Builder;")
        setNotes = JavaMethod("(Ljava/lang/CharSequence;)Landroid/health/connect/datatypes/MindfulnessSessionRecord$Builder;")
        setStartZoneOffset = JavaMethod("(Ljava/time/ZoneOffset;)Landroid/health/connect/datatypes/MindfulnessSessionRecord$Builder;")