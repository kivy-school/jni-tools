from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["PlannedExerciseSessionRecord"]

class PlannedExerciseSessionRecord(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/health/connect/datatypes/PlannedExerciseSessionRecord"
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")
    getTitle = JavaMethod("()Ljava/lang/CharSequence;")
    getDuration = JavaMethod("()Ljava/time/Duration;")
    getStartDate = JavaMethod("()Ljava/time/LocalDate;")
    hasExplicitTime = JavaMethod("()Z")
    getNotes = JavaMethod("()Ljava/lang/CharSequence;")
    getBlocks = JavaMethod("()Ljava/util/List;")
    getCompletedExerciseSessionId = JavaMethod("()Ljava/lang/String;")
    getExerciseType = JavaMethod("()I")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/health/connect/datatypes/PlannedExerciseSessionRecord$Builder"
        __javaconstructor__ = [("(Landroid/health/connect/datatypes/Metadata;ILjava/time/Instant;Ljava/time/Instant;)V", False), ("(Landroid/health/connect/datatypes/Metadata;ILjava/time/LocalDate;Ljava/time/Duration;)V", False)]
        setStartTime = JavaMethod("(Ljava/time/Instant;)Landroid/health/connect/datatypes/PlannedExerciseSessionRecord$Builder;")
        setTitle = JavaMethod("(Ljava/lang/CharSequence;)Landroid/health/connect/datatypes/PlannedExerciseSessionRecord$Builder;")
        build = JavaMethod("()Landroid/health/connect/datatypes/PlannedExerciseSessionRecord;")
        addBlock = JavaMethod("(Landroid/health/connect/datatypes/PlannedExerciseBlock;)Landroid/health/connect/datatypes/PlannedExerciseSessionRecord$Builder;")
        clearBlocks = JavaMethod("()Landroid/health/connect/datatypes/PlannedExerciseSessionRecord$Builder;")
        clearEndZoneOffset = JavaMethod("()Landroid/health/connect/datatypes/PlannedExerciseSessionRecord$Builder;")
        clearStartZoneOffset = JavaMethod("()Landroid/health/connect/datatypes/PlannedExerciseSessionRecord$Builder;")
        setBlocks = JavaMethod("(Ljava/util/List;)Landroid/health/connect/datatypes/PlannedExerciseSessionRecord$Builder;")
        setEndTime = JavaMethod("(Ljava/time/Instant;)Landroid/health/connect/datatypes/PlannedExerciseSessionRecord$Builder;")
        setEndZoneOffset = JavaMethod("(Ljava/time/ZoneOffset;)Landroid/health/connect/datatypes/PlannedExerciseSessionRecord$Builder;")
        setExerciseType = JavaMethod("(I)Landroid/health/connect/datatypes/PlannedExerciseSessionRecord$Builder;")
        setMetadata = JavaMethod("(Landroid/health/connect/datatypes/Metadata;)Landroid/health/connect/datatypes/PlannedExerciseSessionRecord$Builder;")
        setNotes = JavaMethod("(Ljava/lang/CharSequence;)Landroid/health/connect/datatypes/PlannedExerciseSessionRecord$Builder;")
        setStartZoneOffset = JavaMethod("(Ljava/time/ZoneOffset;)Landroid/health/connect/datatypes/PlannedExerciseSessionRecord$Builder;")