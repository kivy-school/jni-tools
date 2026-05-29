from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["BloodGlucoseRecord"]

class BloodGlucoseRecord(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/health/connect/datatypes/BloodGlucoseRecord"
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")
    getMealType = JavaMethod("()I")
    getLevel = JavaMethod("()Landroid/health/connect/datatypes/units/BloodGlucose;")
    getSpecimenSource = JavaMethod("()I")
    getRelationToMeal = JavaMethod("()I")

    class SpecimenSource(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/health/connect/datatypes/BloodGlucoseRecord$SpecimenSource"
        SPECIMEN_SOURCE_CAPILLARY_BLOOD = JavaStaticField("I")
        SPECIMEN_SOURCE_INTERSTITIAL_FLUID = JavaStaticField("I")
        SPECIMEN_SOURCE_PLASMA = JavaStaticField("I")
        SPECIMEN_SOURCE_SERUM = JavaStaticField("I")
        SPECIMEN_SOURCE_TEARS = JavaStaticField("I")
        SPECIMEN_SOURCE_UNKNOWN = JavaStaticField("I")
        SPECIMEN_SOURCE_WHOLE_BLOOD = JavaStaticField("I")

    class RelationToMealType(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/health/connect/datatypes/BloodGlucoseRecord$RelationToMealType"
        RELATION_TO_MEAL_AFTER_MEAL = JavaStaticField("I")
        RELATION_TO_MEAL_BEFORE_MEAL = JavaStaticField("I")
        RELATION_TO_MEAL_FASTING = JavaStaticField("I")
        RELATION_TO_MEAL_GENERAL = JavaStaticField("I")
        RELATION_TO_MEAL_UNKNOWN = JavaStaticField("I")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/health/connect/datatypes/BloodGlucoseRecord$Builder"
        __javaconstructor__ = [("(Landroid/health/connect/datatypes/Metadata;Ljava/time/Instant;ILandroid/health/connect/datatypes/units/BloodGlucose;II)V", False)]
        build = JavaMethod("()Landroid/health/connect/datatypes/BloodGlucoseRecord;")
        clearZoneOffset = JavaMethod("()Landroid/health/connect/datatypes/BloodGlucoseRecord$Builder;")
        setZoneOffset = JavaMethod("(Ljava/time/ZoneOffset;)Landroid/health/connect/datatypes/BloodGlucoseRecord$Builder;")