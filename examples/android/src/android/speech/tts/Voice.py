from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Voice"]

class Voice(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/speech/tts/Voice"
    __javaconstructor__ = [("(Ljava/lang/String;Ljava/util/Locale;IIZLjava/util/Set;)V", False)]
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    LATENCY_HIGH = JavaStaticField("I")
    LATENCY_LOW = JavaStaticField("I")
    LATENCY_NORMAL = JavaStaticField("I")
    LATENCY_VERY_HIGH = JavaStaticField("I")
    LATENCY_VERY_LOW = JavaStaticField("I")
    QUALITY_HIGH = JavaStaticField("I")
    QUALITY_LOW = JavaStaticField("I")
    QUALITY_NORMAL = JavaStaticField("I")
    QUALITY_VERY_HIGH = JavaStaticField("I")
    QUALITY_VERY_LOW = JavaStaticField("I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")
    getLocale = JavaMethod("()Ljava/util/Locale;")
    getQuality = JavaMethod("()I")
    getLatency = JavaMethod("()I")
    isNetworkConnectionRequired = JavaMethod("()Z")
    getName = JavaMethod("()Ljava/lang/String;")
    getFeatures = JavaMethod("()Ljava/util/Set;")
    toString = JavaMethod("()Ljava/lang/String;")
    hashCode = JavaMethod("()I")
    equals = JavaMethod("(Ljava/lang/Object;)Z")