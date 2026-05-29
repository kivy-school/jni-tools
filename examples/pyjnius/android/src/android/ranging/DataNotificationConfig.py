from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["DataNotificationConfig"]

class DataNotificationConfig(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/ranging/DataNotificationConfig"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    NOTIFICATION_CONFIG_DISABLE = JavaStaticField("I")
    NOTIFICATION_CONFIG_ENABLE = JavaStaticField("I")
    NOTIFICATION_CONFIG_PROXIMITY_EDGE = JavaStaticField("I")
    NOTIFICATION_CONFIG_PROXIMITY_LEVEL = JavaStaticField("I")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    toString = JavaMethod("()Ljava/lang/String;")
    hashCode = JavaMethod("()I")
    getNotificationConfigType = JavaMethod("()I")
    getProximityFarCm = JavaMethod("()I")
    getProximityNearCm = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/ranging/DataNotificationConfig$Builder"
        __javaconstructor__ = [("()V", False)]
        setProximityNearCm = JavaMethod("(I)Landroid/ranging/DataNotificationConfig$Builder;")
        setProximityFarCm = JavaMethod("(I)Landroid/ranging/DataNotificationConfig$Builder;")
        setNotificationConfigType = JavaMethod("(I)Landroid/ranging/DataNotificationConfig$Builder;")
        build = JavaMethod("()Landroid/ranging/DataNotificationConfig;")