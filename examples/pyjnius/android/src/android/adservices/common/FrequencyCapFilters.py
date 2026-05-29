from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["FrequencyCapFilters"]

class FrequencyCapFilters(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/adservices/common/FrequencyCapFilters"
    AD_EVENT_TYPE_CLICK = JavaStaticField("I")
    AD_EVENT_TYPE_IMPRESSION = JavaStaticField("I")
    AD_EVENT_TYPE_VIEW = JavaStaticField("I")
    AD_EVENT_TYPE_WIN = JavaStaticField("I")
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    getKeyedFrequencyCapsForClickEvents = JavaMethod("()Ljava/util/List;")
    getKeyedFrequencyCapsForViewEvents = JavaMethod("()Ljava/util/List;")
    getKeyedFrequencyCapsForImpressionEvents = JavaMethod("()Ljava/util/List;")
    getKeyedFrequencyCapsForWinEvents = JavaMethod("()Ljava/util/List;")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    toString = JavaMethod("()Ljava/lang/String;")
    hashCode = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/adservices/common/FrequencyCapFilters$Builder"
        __javaconstructor__ = [("()V", False)]
        setKeyedFrequencyCapsForImpressionEvents = JavaMethod("(Ljava/util/List;)Landroid/adservices/common/FrequencyCapFilters$Builder;")
        setKeyedFrequencyCapsForWinEvents = JavaMethod("(Ljava/util/List;)Landroid/adservices/common/FrequencyCapFilters$Builder;")
        setKeyedFrequencyCapsForViewEvents = JavaMethod("(Ljava/util/List;)Landroid/adservices/common/FrequencyCapFilters$Builder;")
        setKeyedFrequencyCapsForClickEvents = JavaMethod("(Ljava/util/List;)Landroid/adservices/common/FrequencyCapFilters$Builder;")
        build = JavaMethod("()Landroid/adservices/common/FrequencyCapFilters;")