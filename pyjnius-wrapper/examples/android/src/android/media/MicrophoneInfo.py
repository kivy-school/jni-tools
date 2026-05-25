from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["MicrophoneInfo"]

class MicrophoneInfo(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/media/MicrophoneInfo"
    CHANNEL_MAPPING_DIRECT = JavaStaticField("I")
    CHANNEL_MAPPING_PROCESSED = JavaStaticField("I")
    DIRECTIONALITY_BI_DIRECTIONAL = JavaStaticField("I")
    DIRECTIONALITY_CARDIOID = JavaStaticField("I")
    DIRECTIONALITY_HYPER_CARDIOID = JavaStaticField("I")
    DIRECTIONALITY_OMNI = JavaStaticField("I")
    DIRECTIONALITY_SUPER_CARDIOID = JavaStaticField("I")
    DIRECTIONALITY_UNKNOWN = JavaStaticField("I")
    GROUP_UNKNOWN = JavaStaticField("I")
    INDEX_IN_THE_GROUP_UNKNOWN = JavaStaticField("I")
    LOCATION_MAINBODY = JavaStaticField("I")
    LOCATION_MAINBODY_MOVABLE = JavaStaticField("I")
    LOCATION_PERIPHERAL = JavaStaticField("I")
    LOCATION_UNKNOWN = JavaStaticField("I")
    ORIENTATION_UNKNOWN = JavaStaticField("Landroid/media/MicrophoneInfo$Coordinate3F;")
    POSITION_UNKNOWN = JavaStaticField("Landroid/media/MicrophoneInfo$Coordinate3F;")
    SENSITIVITY_UNKNOWN = JavaStaticField("F")
    SPL_UNKNOWN = JavaStaticField("F")
    getDescription = JavaMethod("()Ljava/lang/String;")
    getId = JavaMethod("()I")
    getType = JavaMethod("()I")
    getAddress = JavaMethod("()Ljava/lang/String;")
    getLocation = JavaMethod("()I")
    getGroup = JavaMethod("()I")
    getIndexInTheGroup = JavaMethod("()I")
    getPosition = JavaMethod("()Landroid/media/MicrophoneInfo$Coordinate3F;")
    getOrientation = JavaMethod("()Landroid/media/MicrophoneInfo$Coordinate3F;")
    getFrequencyResponse = JavaMethod("()Ljava/util/List;")
    getChannelMapping = JavaMethod("()Ljava/util/List;")
    getSensitivity = JavaMethod("()F")
    getMaxSpl = JavaMethod("()F")
    getMinSpl = JavaMethod("()F")
    getDirectionality = JavaMethod("()I")

    class Coordinate3F(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/media/MicrophoneInfo/Coordinate3F"
        x = JavaField("F")
        y = JavaField("F")
        z = JavaField("F")
        equals = JavaMethod("(Ljava/lang/Object;)Z")