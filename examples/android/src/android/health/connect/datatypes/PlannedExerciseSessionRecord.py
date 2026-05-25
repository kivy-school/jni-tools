from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["PlannedExerciseSessionRecord"]

class PlannedExerciseSessionRecord(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/health/connect/datatypes/PlannedExerciseSessionRecord"
    getExerciseType = JavaMethod("()I")
    getNotes = JavaMethod("()Ljava/lang/CharSequence;")
    getTitle = JavaMethod("()Ljava/lang/CharSequence;")
    getStartDate = JavaMethod("()Ljava/time/LocalDate;")
    getDuration = JavaMethod("()Ljava/time/Duration;")
    hasExplicitTime = JavaMethod("()Z")
    getCompletedExerciseSessionId = JavaMethod("()Ljava/lang/String;")
    getBlocks = JavaMethod("()Ljava/util/List;")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/health/connect/datatypes/PlannedExerciseSessionRecord/Builder"
        __javaconstructor__ = [("(Landroid/health/connect/datatypes/Metadata;ILjava/time/Instant;Ljava/time/Instant;)V", False), ("(Landroid/health/connect/datatypes/Metadata;ILjava/time/LocalDate;Ljava/time/Duration;)V", False)]
        setMetadata = JavaMethod("(Landroid/health/connect/datatypes/Metadata;)Landroid/health/connect/datatypes/PlannedExerciseSessionRecord$Builder;")
        setExerciseType = JavaMethod("(I)Landroid/health/connect/datatypes/PlannedExerciseSessionRecord$Builder;")
        setStartTime = JavaMethod("(Ljava/time/Instant;)Landroid/health/connect/datatypes/PlannedExerciseSessionRecord$Builder;")
        setEndTime = JavaMethod("(Ljava/time/Instant;)Landroid/health/connect/datatypes/PlannedExerciseSessionRecord$Builder;")
        setStartZoneOffset = JavaMethod("(Ljava/time/ZoneOffset;)Landroid/health/connect/datatypes/PlannedExerciseSessionRecord$Builder;")
        setEndZoneOffset = JavaMethod("(Ljava/time/ZoneOffset;)Landroid/health/connect/datatypes/PlannedExerciseSessionRecord$Builder;")
        clearStartZoneOffset = JavaMethod("()Landroid/health/connect/datatypes/PlannedExerciseSessionRecord$Builder;")
        clearEndZoneOffset = JavaMethod("()Landroid/health/connect/datatypes/PlannedExerciseSessionRecord$Builder;")
        setNotes = JavaMethod("(Ljava/lang/CharSequence;)Landroid/health/connect/datatypes/PlannedExerciseSessionRecord$Builder;")
        setTitle = JavaMethod("(Ljava/lang/CharSequence;)Landroid/health/connect/datatypes/PlannedExerciseSessionRecord$Builder;")
        addBlock = JavaMethod("(Landroid/health/connect/datatypes/PlannedExerciseBlock;)Landroid/health/connect/datatypes/PlannedExerciseSessionRecord$Builder;")
        setBlocks = JavaMethod("(Ljava/util/List;)Landroid/health/connect/datatypes/PlannedExerciseSessionRecord$Builder;")
        clearBlocks = JavaMethod("()Landroid/health/connect/datatypes/PlannedExerciseSessionRecord$Builder;")
        build = JavaMethod("()Landroid/health/connect/datatypes/PlannedExerciseSessionRecord;")