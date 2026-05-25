from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["RecognitionPart"]

class RecognitionPart(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/speech/RecognitionPart"
    CONFIDENCE_LEVEL_HIGH = JavaStaticField("I")
    CONFIDENCE_LEVEL_LOW = JavaStaticField("I")
    CONFIDENCE_LEVEL_MEDIUM = JavaStaticField("I")
    CONFIDENCE_LEVEL_MEDIUM_HIGH = JavaStaticField("I")
    CONFIDENCE_LEVEL_MEDIUM_LOW = JavaStaticField("I")
    CONFIDENCE_LEVEL_UNKNOWN = JavaStaticField("I")
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    getRawText = JavaMethod("()Ljava/lang/String;")
    getFormattedText = JavaMethod("()Ljava/lang/String;")
    getTimestampMillis = JavaMethod("()J")
    getConfidenceLevel = JavaMethod("()I")
    toString = JavaMethod("()Ljava/lang/String;")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/speech/RecognitionPart/Builder"
        __javaconstructor__ = [("(Ljava/lang/String;)V", False)]
        setRawText = JavaMethod("(Ljava/lang/String;)Landroid/speech/RecognitionPart$Builder;")
        setTimestampMillis = JavaMethod("(J)Landroid/speech/RecognitionPart$Builder;")
        setConfidenceLevel = JavaMethod("(I)Landroid/speech/RecognitionPart$Builder;")
        build = JavaMethod("()Landroid/speech/RecognitionPart;")
        setFormattedText = JavaMethod("(Ljava/lang/String;)Landroid/speech/RecognitionPart$Builder;")