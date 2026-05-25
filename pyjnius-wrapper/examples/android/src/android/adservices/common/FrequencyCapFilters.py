from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["FrequencyCapFilters"]

class FrequencyCapFilters(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/adservices/common/FrequencyCapFilters"
    AD_EVENT_TYPE_CLICK = JavaStaticField("I")
    AD_EVENT_TYPE_IMPRESSION = JavaStaticField("I")
    AD_EVENT_TYPE_VIEW = JavaStaticField("I")
    AD_EVENT_TYPE_WIN = JavaStaticField("I")
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    getKeyedFrequencyCapsForWinEvents = JavaMethod("()Ljava/util/List;")
    getKeyedFrequencyCapsForImpressionEvents = JavaMethod("()Ljava/util/List;")
    getKeyedFrequencyCapsForViewEvents = JavaMethod("()Ljava/util/List;")
    getKeyedFrequencyCapsForClickEvents = JavaMethod("()Ljava/util/List;")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")
    toString = JavaMethod("()Ljava/lang/String;")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/adservices/common/FrequencyCapFilters/Builder"
        __javaconstructor__ = [("()V", False)]
        setKeyedFrequencyCapsForWinEvents = JavaMethod("(Ljava/util/List;)Landroid/adservices/common/FrequencyCapFilters$Builder;")
        setKeyedFrequencyCapsForImpressionEvents = JavaMethod("(Ljava/util/List;)Landroid/adservices/common/FrequencyCapFilters$Builder;")
        setKeyedFrequencyCapsForViewEvents = JavaMethod("(Ljava/util/List;)Landroid/adservices/common/FrequencyCapFilters$Builder;")
        setKeyedFrequencyCapsForClickEvents = JavaMethod("(Ljava/util/List;)Landroid/adservices/common/FrequencyCapFilters$Builder;")
        build = JavaMethod("()Landroid/adservices/common/FrequencyCapFilters;")