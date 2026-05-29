from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["RecognitionSupport"]

class RecognitionSupport(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/speech/RecognitionSupport"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    toString = JavaMethod("()Ljava/lang/String;")
    hashCode = JavaMethod("()I")
    getOnlineLanguages = JavaMethod("()Ljava/util/List;")
    getPendingOnDeviceLanguages = JavaMethod("()Ljava/util/List;")
    getInstalledOnDeviceLanguages = JavaMethod("()Ljava/util/List;")
    getSupportedOnDeviceLanguages = JavaMethod("()Ljava/util/List;")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/speech/RecognitionSupport$Builder"
        __javaconstructor__ = [("()V", False)]
        setOnlineLanguages = JavaMethod("(Ljava/util/List;)Landroid/speech/RecognitionSupport$Builder;")
        addOnlineLanguage = JavaMethod("(Ljava/lang/String;)Landroid/speech/RecognitionSupport$Builder;")
        addInstalledOnDeviceLanguage = JavaMethod("(Ljava/lang/String;)Landroid/speech/RecognitionSupport$Builder;")
        addPendingOnDeviceLanguage = JavaMethod("(Ljava/lang/String;)Landroid/speech/RecognitionSupport$Builder;")
        addSupportedOnDeviceLanguage = JavaMethod("(Ljava/lang/String;)Landroid/speech/RecognitionSupport$Builder;")
        setInstalledOnDeviceLanguages = JavaMethod("(Ljava/util/List;)Landroid/speech/RecognitionSupport$Builder;")
        setPendingOnDeviceLanguages = JavaMethod("(Ljava/util/List;)Landroid/speech/RecognitionSupport$Builder;")
        setSupportedOnDeviceLanguages = JavaMethod("(Ljava/util/List;)Landroid/speech/RecognitionSupport$Builder;")
        build = JavaMethod("()Landroid/speech/RecognitionSupport;")