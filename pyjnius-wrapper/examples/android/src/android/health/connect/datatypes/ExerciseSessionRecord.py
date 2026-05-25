from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ExerciseSessionRecord"]

class ExerciseSessionRecord(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/health/connect/datatypes/ExerciseSessionRecord"
    EXERCISE_DURATION_TOTAL = JavaStaticField("Landroid/health/connect/datatypes/AggregationType;")
    getExerciseType = JavaMethod("()I")
    getNotes = JavaMethod("()Ljava/lang/CharSequence;")
    getTitle = JavaMethod("()Ljava/lang/CharSequence;")
    getRoute = JavaMethod("()Landroid/health/connect/datatypes/ExerciseRoute;")
    getSegments = JavaMethod("()Ljava/util/List;")
    getLaps = JavaMethod("()Ljava/util/List;")
    hasRoute = JavaMethod("()Z")
    getPlannedExerciseSessionId = JavaMethod("()Ljava/lang/String;")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/health/connect/datatypes/ExerciseSessionRecord/Builder"
        __javaconstructor__ = [("(Landroid/health/connect/datatypes/Metadata;Ljava/time/Instant;Ljava/time/Instant;I)V", False)]
        setStartZoneOffset = JavaMethod("(Ljava/time/ZoneOffset;)Landroid/health/connect/datatypes/ExerciseSessionRecord$Builder;")
        setEndZoneOffset = JavaMethod("(Ljava/time/ZoneOffset;)Landroid/health/connect/datatypes/ExerciseSessionRecord$Builder;")
        clearStartZoneOffset = JavaMethod("()Landroid/health/connect/datatypes/ExerciseSessionRecord$Builder;")
        clearEndZoneOffset = JavaMethod("()Landroid/health/connect/datatypes/ExerciseSessionRecord$Builder;")
        setNotes = JavaMethod("(Ljava/lang/CharSequence;)Landroid/health/connect/datatypes/ExerciseSessionRecord$Builder;")
        setTitle = JavaMethod("(Ljava/lang/CharSequence;)Landroid/health/connect/datatypes/ExerciseSessionRecord$Builder;")
        setRoute = JavaMethod("(Landroid/health/connect/datatypes/ExerciseRoute;)Landroid/health/connect/datatypes/ExerciseSessionRecord$Builder;")
        setLaps = JavaMethod("(Ljava/util/List;)Landroid/health/connect/datatypes/ExerciseSessionRecord$Builder;")
        setSegments = JavaMethod("(Ljava/util/List;)Landroid/health/connect/datatypes/ExerciseSessionRecord$Builder;")
        setPlannedExerciseSessionId = JavaMethod("(Ljava/lang/String;)Landroid/health/connect/datatypes/ExerciseSessionRecord$Builder;")
        build = JavaMethod("()Landroid/health/connect/datatypes/ExerciseSessionRecord;")