from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["UwbComplexChannel"]

class UwbComplexChannel(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/ranging/uwb/UwbComplexChannel"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    UWB_CHANNEL_10 = JavaStaticField("I")
    UWB_CHANNEL_12 = JavaStaticField("I")
    UWB_CHANNEL_13 = JavaStaticField("I")
    UWB_CHANNEL_14 = JavaStaticField("I")
    UWB_CHANNEL_5 = JavaStaticField("I")
    UWB_CHANNEL_6 = JavaStaticField("I")
    UWB_CHANNEL_8 = JavaStaticField("I")
    UWB_CHANNEL_9 = JavaStaticField("I")
    UWB_PREAMBLE_CODE_INDEX_10 = JavaStaticField("I")
    UWB_PREAMBLE_CODE_INDEX_11 = JavaStaticField("I")
    UWB_PREAMBLE_CODE_INDEX_12 = JavaStaticField("I")
    UWB_PREAMBLE_CODE_INDEX_25 = JavaStaticField("I")
    UWB_PREAMBLE_CODE_INDEX_26 = JavaStaticField("I")
    UWB_PREAMBLE_CODE_INDEX_27 = JavaStaticField("I")
    UWB_PREAMBLE_CODE_INDEX_28 = JavaStaticField("I")
    UWB_PREAMBLE_CODE_INDEX_29 = JavaStaticField("I")
    UWB_PREAMBLE_CODE_INDEX_30 = JavaStaticField("I")
    UWB_PREAMBLE_CODE_INDEX_31 = JavaStaticField("I")
    UWB_PREAMBLE_CODE_INDEX_32 = JavaStaticField("I")
    UWB_PREAMBLE_CODE_INDEX_9 = JavaStaticField("I")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    toString = JavaMethod("()Ljava/lang/String;")
    hashCode = JavaMethod("()I")
    getPreambleIndex = JavaMethod("()I")
    getChannel = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/ranging/uwb/UwbComplexChannel$Builder"
        __javaconstructor__ = [("()V", False)]
        setChannel = JavaMethod("(I)Landroid/ranging/uwb/UwbComplexChannel$Builder;")
        setPreambleIndex = JavaMethod("(I)Landroid/ranging/uwb/UwbComplexChannel$Builder;")
        build = JavaMethod("()Landroid/ranging/uwb/UwbComplexChannel;")