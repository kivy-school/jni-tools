from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["AmbientBacklightSettings"]

class AmbientBacklightSettings(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/media/quality/AmbientBacklightSettings"
    __javaconstructor__ = [("(IIIIIZI)V", False)]
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    SOURCE_AUDIO = JavaStaticField("I")
    SOURCE_AUDIO_VIDEO = JavaStaticField("I")
    SOURCE_NONE = JavaStaticField("I")
    SOURCE_VIDEO = JavaStaticField("I")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    isLetterboxOmitted = JavaMethod("()Z")
    getColorFormat = JavaMethod("()I")
    getHorizontalZonesCount = JavaMethod("()I")
    getMaxFps = JavaMethod("()I")
    getVerticalZonesCount = JavaMethod("()I")
    toString = JavaMethod("()Ljava/lang/String;")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")
    getThreshold = JavaMethod("()I")
    getSource = JavaMethod("()I")