from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["MicrophoneDirection"]

class MicrophoneDirection(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "android/media/MicrophoneDirection"
    MIC_DIRECTION_AWAY_FROM_USER = JavaStaticField("I")
    MIC_DIRECTION_EXTERNAL = JavaStaticField("I")
    MIC_DIRECTION_TOWARDS_USER = JavaStaticField("I")
    MIC_DIRECTION_UNSPECIFIED = JavaStaticField("I")
    setPreferredMicrophoneDirection = JavaMethod("(I)Z")
    setPreferredMicrophoneFieldDimension = JavaMethod("(F)Z")