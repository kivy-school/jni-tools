from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ConversationStatus"]

class ConversationStatus(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/app/people/ConversationStatus"
    ACTIVITY_ANNIVERSARY = JavaStaticField("I")
    ACTIVITY_AUDIO = JavaStaticField("I")
    ACTIVITY_BIRTHDAY = JavaStaticField("I")
    ACTIVITY_GAME = JavaStaticField("I")
    ACTIVITY_LOCATION = JavaStaticField("I")
    ACTIVITY_NEW_STORY = JavaStaticField("I")
    ACTIVITY_OTHER = JavaStaticField("I")
    ACTIVITY_UPCOMING_BIRTHDAY = JavaStaticField("I")
    ACTIVITY_VIDEO = JavaStaticField("I")
    AVAILABILITY_AVAILABLE = JavaStaticField("I")
    AVAILABILITY_BUSY = JavaStaticField("I")
    AVAILABILITY_OFFLINE = JavaStaticField("I")
    AVAILABILITY_UNKNOWN = JavaStaticField("I")
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    getId = JavaMethod("()Ljava/lang/String;")
    getActivity = JavaMethod("()I")
    getAvailability = JavaMethod("()I")
    getDescription = JavaMethod("()Ljava/lang/CharSequence;")
    getIcon = JavaMethod("()Landroid/graphics/drawable/Icon;")
    getStartTimeMillis = JavaMethod("()J")
    getEndTimeMillis = JavaMethod("()J")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")
    toString = JavaMethod("()Ljava/lang/String;")
    describeContents = JavaMethod("()I")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/app/people/ConversationStatus/Builder"
        __javaconstructor__ = [("(Ljava/lang/String;I)V", False)]
        setAvailability = JavaMethod("(I)Landroid/app/people/ConversationStatus$Builder;")
        setDescription = JavaMethod("(Ljava/lang/CharSequence;)Landroid/app/people/ConversationStatus$Builder;")
        setIcon = JavaMethod("(Landroid/graphics/drawable/Icon;)Landroid/app/people/ConversationStatus$Builder;")
        setStartTimeMillis = JavaMethod("(J)Landroid/app/people/ConversationStatus$Builder;")
        setEndTimeMillis = JavaMethod("(J)Landroid/app/people/ConversationStatus$Builder;")
        build = JavaMethod("()Landroid/app/people/ConversationStatus;")