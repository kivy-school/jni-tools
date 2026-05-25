from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["SubscriptionPlan"]

class SubscriptionPlan(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/telephony/SubscriptionPlan"
    BYTES_UNKNOWN = JavaStaticField("J")
    BYTES_UNLIMITED = JavaStaticField("J")
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    LIMIT_BEHAVIOR_BILLED = JavaStaticField("I")
    LIMIT_BEHAVIOR_DISABLED = JavaStaticField("I")
    LIMIT_BEHAVIOR_THROTTLED = JavaStaticField("I")
    LIMIT_BEHAVIOR_UNKNOWN = JavaStaticField("I")
    TIME_UNKNOWN = JavaStaticField("J")
    describeContents = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    toString = JavaMethod("()Ljava/lang/String;")
    hashCode = JavaMethod("()I")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    getTitle = JavaMethod("()Ljava/lang/CharSequence;")
    getSummary = JavaMethod("()Ljava/lang/CharSequence;")
    getDataLimitBytes = JavaMethod("()J")
    getDataLimitBehavior = JavaMethod("()I")
    getDataUsageBytes = JavaMethod("()J")
    getDataUsageTime = JavaMethod("()J")
    getNetworkTypes = JavaMethod("()[I")
    cycleIterator = JavaMethod("()Ljava/util/Iterator;")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/telephony/SubscriptionPlan/Builder"
        createNonrecurring = JavaStaticMethod("(Ljava/time/ZonedDateTime;Ljava/time/ZonedDateTime;)Landroid/telephony/SubscriptionPlan$Builder;")
        createRecurring = JavaStaticMethod("(Ljava/time/ZonedDateTime;Ljava/time/Period;)Landroid/telephony/SubscriptionPlan$Builder;")
        build = JavaMethod("()Landroid/telephony/SubscriptionPlan;")
        setTitle = JavaMethod("(Ljava/lang/CharSequence;)Landroid/telephony/SubscriptionPlan$Builder;")
        setSummary = JavaMethod("(Ljava/lang/CharSequence;)Landroid/telephony/SubscriptionPlan$Builder;")
        setDataLimit = JavaMethod("(JI)Landroid/telephony/SubscriptionPlan$Builder;")
        setDataUsage = JavaMethod("(JJ)Landroid/telephony/SubscriptionPlan$Builder;")
        setNetworkTypes = JavaMethod("([I)Landroid/telephony/SubscriptionPlan$Builder;")
        resetNetworkTypes = JavaMethod("()Landroid/telephony/SubscriptionPlan$Builder;")