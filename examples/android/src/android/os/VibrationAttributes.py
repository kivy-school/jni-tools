from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["VibrationAttributes"]

class VibrationAttributes(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/os/VibrationAttributes"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    FLAG_BYPASS_INTERRUPTION_POLICY = JavaStaticField("I")
    USAGE_ACCESSIBILITY = JavaStaticField("I")
    USAGE_ALARM = JavaStaticField("I")
    USAGE_CLASS_ALARM = JavaStaticField("I")
    USAGE_CLASS_FEEDBACK = JavaStaticField("I")
    USAGE_CLASS_MASK = JavaStaticField("I")
    USAGE_CLASS_MEDIA = JavaStaticField("I")
    USAGE_CLASS_UNKNOWN = JavaStaticField("I")
    USAGE_COMMUNICATION_REQUEST = JavaStaticField("I")
    USAGE_HARDWARE_FEEDBACK = JavaStaticField("I")
    USAGE_MEDIA = JavaStaticField("I")
    USAGE_NOTIFICATION = JavaStaticField("I")
    USAGE_PHYSICAL_EMULATION = JavaStaticField("I")
    USAGE_RINGTONE = JavaStaticField("I")
    USAGE_TOUCH = JavaStaticField("I")
    USAGE_UNKNOWN = JavaStaticField("I")
    createForUsage = JavaStaticMethod("(I)Landroid/os/VibrationAttributes;")
    getUsageClass = JavaMethod("()I")
    getUsage = JavaMethod("()I")
    getFlags = JavaMethod("()I")
    isFlagSet = JavaMethod("(I)Z")
    describeContents = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")
    toString = JavaMethod("()Ljava/lang/String;")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/os/VibrationAttributes/Builder"
        __javaconstructor__ = [("()V", False), ("(Landroid/os/VibrationAttributes;)V", False), ("(Landroid/media/AudioAttributes;)V", False)]
        build = JavaMethod("()Landroid/os/VibrationAttributes;")
        setUsage = JavaMethod("(I)Landroid/os/VibrationAttributes$Builder;")
        setFlags = JavaMethod("(II)Landroid/os/VibrationAttributes$Builder;")