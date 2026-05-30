from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

class AdServicesPermissions(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/adservices/common/AdServicesPermissions"
    ACCESS_ADSERVICES_AD_ID = JavaStaticField("Ljava/lang/String;")
    ACCESS_ADSERVICES_AD_SELECTION = JavaStaticField("Ljava/lang/String;")
    ACCESS_ADSERVICES_ATTRIBUTION = JavaStaticField("Ljava/lang/String;")
    ACCESS_ADSERVICES_CUSTOM_AUDIENCE = JavaStaticField("Ljava/lang/String;")
    ACCESS_ADSERVICES_PROTECTED_SIGNALS = JavaStaticField("Ljava/lang/String;")
    ACCESS_ADSERVICES_TOPICS = JavaStaticField("Ljava/lang/String;")

class AdTechIdentifier(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/adservices/common/AdTechIdentifier"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    toString = JavaMethod("()Ljava/lang/String;")
    hashCode = JavaMethod("()I")
    describeContents = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    fromString = JavaStaticMethod("(Ljava/lang/String;)Landroid/adservices/common/AdTechIdentifier;")

class AdSelectionSignals(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/adservices/common/AdSelectionSignals"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    EMPTY = JavaStaticField("Landroid/adservices/common/AdSelectionSignals;")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    toString = JavaMethod("()Ljava/lang/String;")
    hashCode = JavaMethod("()I")
    describeContents = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    fromString = JavaStaticMethod("(Ljava/lang/String;)Landroid/adservices/common/AdSelectionSignals;")

class KeyedFrequencyCap(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/adservices/common/KeyedFrequencyCap"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    getMaxCount = JavaMethod("()I")
    getAdCounterKey = JavaMethod("()I")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    toString = JavaMethod("()Ljava/lang/String;")
    hashCode = JavaMethod("()I")
    getInterval = JavaMethod("()Ljava/time/Duration;")
    describeContents = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/adservices/common/KeyedFrequencyCap$Builder"
        __javaconstructor__ = [("(IILjava/time/Duration;)V", False)]
        setInterval = JavaMethod("(Ljava/time/Duration;)Landroid/adservices/common/KeyedFrequencyCap$Builder;")
        setAdCounterKey = JavaMethod("(I)Landroid/adservices/common/KeyedFrequencyCap$Builder;")
        setMaxCount = JavaMethod("(I)Landroid/adservices/common/KeyedFrequencyCap$Builder;")
        build = JavaMethod("()Landroid/adservices/common/KeyedFrequencyCap;")

class ComponentAdData(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/adservices/common/ComponentAdData"
    __javaconstructor__ = [("(Landroid/net/Uri;Ljava/lang/String;)V", False)]
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    toString = JavaMethod("()Ljava/lang/String;")
    hashCode = JavaMethod("()I")
    describeContents = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    getAdRenderId = JavaMethod("()Ljava/lang/String;")
    getRenderUri = JavaMethod("()Landroid/net/Uri;")

class FrequencyCapFilters(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/adservices/common/FrequencyCapFilters"
    AD_EVENT_TYPE_CLICK = JavaStaticField("I")
    AD_EVENT_TYPE_IMPRESSION = JavaStaticField("I")
    AD_EVENT_TYPE_VIEW = JavaStaticField("I")
    AD_EVENT_TYPE_WIN = JavaStaticField("I")
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    toString = JavaMethod("()Ljava/lang/String;")
    hashCode = JavaMethod("()I")
    describeContents = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    getKeyedFrequencyCapsForClickEvents = JavaMethod("()Ljava/util/List;")
    getKeyedFrequencyCapsForImpressionEvents = JavaMethod("()Ljava/util/List;")
    getKeyedFrequencyCapsForViewEvents = JavaMethod("()Ljava/util/List;")
    getKeyedFrequencyCapsForWinEvents = JavaMethod("()Ljava/util/List;")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/adservices/common/FrequencyCapFilters$Builder"
        __javaconstructor__ = [("()V", False)]
        setKeyedFrequencyCapsForClickEvents = JavaMethod("(Ljava/util/List;)Landroid/adservices/common/FrequencyCapFilters$Builder;")
        setKeyedFrequencyCapsForImpressionEvents = JavaMethod("(Ljava/util/List;)Landroid/adservices/common/FrequencyCapFilters$Builder;")
        setKeyedFrequencyCapsForViewEvents = JavaMethod("(Ljava/util/List;)Landroid/adservices/common/FrequencyCapFilters$Builder;")
        setKeyedFrequencyCapsForWinEvents = JavaMethod("(Ljava/util/List;)Landroid/adservices/common/FrequencyCapFilters$Builder;")
        build = JavaMethod("()Landroid/adservices/common/FrequencyCapFilters;")

class AdServicesOutcomeReceiver(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/adservices/common/AdServicesOutcomeReceiver"
    onError = JavaMethod("(Ljava/lang/Throwable;)V")
    onResult = JavaMethod("(Ljava/lang/Object;)V")

class AdData(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/adservices/common/AdData"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    toString = JavaMethod("()Ljava/lang/String;")
    hashCode = JavaMethod("()I")
    describeContents = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    getMetadata = JavaMethod("()Ljava/lang/String;")
    getAdCounterKeys = JavaMethod("()Ljava/util/Set;")
    getAdFilters = JavaMethod("()Landroid/adservices/common/AdFilters;")
    getAdRenderId = JavaMethod("()Ljava/lang/String;")
    getRenderUri = JavaMethod("()Landroid/net/Uri;")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/adservices/common/AdData$Builder"
        __javaconstructor__ = [("()V", False)]
        setAdFilters = JavaMethod("(Landroid/adservices/common/AdFilters;)Landroid/adservices/common/AdData$Builder;")
        setAdRenderId = JavaMethod("(Ljava/lang/String;)Landroid/adservices/common/AdData$Builder;")
        setAdCounterKeys = JavaMethod("(Ljava/util/Set;)Landroid/adservices/common/AdData$Builder;")
        setMetadata = JavaMethod("(Ljava/lang/String;)Landroid/adservices/common/AdData$Builder;")
        setRenderUri = JavaMethod("(Landroid/net/Uri;)Landroid/adservices/common/AdData$Builder;")
        build = JavaMethod("()Landroid/adservices/common/AdData;")

class AppInstallFilters(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/adservices/common/AppInstallFilters"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    toString = JavaMethod("()Ljava/lang/String;")
    hashCode = JavaMethod("()I")
    describeContents = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    getPackageNames = JavaMethod("()Ljava/util/Set;")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/adservices/common/AppInstallFilters$Builder"
        __javaconstructor__ = [("()V", False)]
        setPackageNames = JavaMethod("(Ljava/util/Set;)Landroid/adservices/common/AppInstallFilters$Builder;")
        build = JavaMethod("()Landroid/adservices/common/AppInstallFilters;")

class AdFilters(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/adservices/common/AdFilters"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    toString = JavaMethod("()Ljava/lang/String;")
    hashCode = JavaMethod("()I")
    describeContents = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    getAppInstallFilters = JavaMethod("()Landroid/adservices/common/AppInstallFilters;")
    getFrequencyCapFilters = JavaMethod("()Landroid/adservices/common/FrequencyCapFilters;")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/adservices/common/AdFilters$Builder"
        __javaconstructor__ = [("()V", False)]
        setFrequencyCapFilters = JavaMethod("(Landroid/adservices/common/FrequencyCapFilters;)Landroid/adservices/common/AdFilters$Builder;")
        setAppInstallFilters = JavaMethod("(Landroid/adservices/common/AppInstallFilters;)Landroid/adservices/common/AdFilters$Builder;")
        build = JavaMethod("()Landroid/adservices/common/AdFilters;")