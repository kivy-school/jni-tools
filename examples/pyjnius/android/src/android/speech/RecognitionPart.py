from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

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
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    toString = JavaMethod("()Ljava/lang/String;")
    hashCode = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")
    getTimestampMillis = JavaMethod("()J")
    getRawText = JavaMethod("()Ljava/lang/String;")
    getFormattedText = JavaMethod("()Ljava/lang/String;")
    getConfidenceLevel = JavaMethod("()I")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/speech/RecognitionPart$Builder"
        __javaconstructor__ = [("(Ljava/lang/String;)V", False)]
        setRawText = JavaMethod("(Ljava/lang/String;)Landroid/speech/RecognitionPart$Builder;")
        setTimestampMillis = JavaMethod("(J)Landroid/speech/RecognitionPart$Builder;")
        setFormattedText = JavaMethod("(Ljava/lang/String;)Landroid/speech/RecognitionPart$Builder;")
        setConfidenceLevel = JavaMethod("(I)Landroid/speech/RecognitionPart$Builder;")
        build = JavaMethod("()Landroid/speech/RecognitionPart;")