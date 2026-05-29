from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["UsageEvents"]

class UsageEvents(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/app/usage/UsageEvents"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    hasNextEvent = JavaMethod("()Z")
    getNextEvent = JavaMethod("(Landroid/app/usage/UsageEvents$Event;)Z")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")

    class Event(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/app/usage/UsageEvents$Event"
        __javaconstructor__ = [("()V", False)]
        ACTIVITY_PAUSED = JavaStaticField("I")
        ACTIVITY_RESUMED = JavaStaticField("I")
        ACTIVITY_STOPPED = JavaStaticField("I")
        CONFIGURATION_CHANGE = JavaStaticField("I")
        DEVICE_SHUTDOWN = JavaStaticField("I")
        DEVICE_STARTUP = JavaStaticField("I")
        FOREGROUND_SERVICE_START = JavaStaticField("I")
        FOREGROUND_SERVICE_STOP = JavaStaticField("I")
        KEYGUARD_HIDDEN = JavaStaticField("I")
        KEYGUARD_SHOWN = JavaStaticField("I")
        MOVE_TO_BACKGROUND = JavaStaticField("I")
        MOVE_TO_FOREGROUND = JavaStaticField("I")
        NONE = JavaStaticField("I")
        SCREEN_INTERACTIVE = JavaStaticField("I")
        SCREEN_NON_INTERACTIVE = JavaStaticField("I")
        SHORTCUT_INVOCATION = JavaStaticField("I")
        STANDBY_BUCKET_CHANGED = JavaStaticField("I")
        USER_INTERACTION = JavaStaticField("I")
        getShortcutId = JavaMethod("()Ljava/lang/String;")
        getAppStandbyBucket = JavaMethod("()I")
        getTimeStamp = JavaMethod("()J")
        getPackageName = JavaMethod("()Ljava/lang/String;")
        getClassName = JavaMethod("()Ljava/lang/String;")
        getConfiguration = JavaMethod("()Landroid/content/res/Configuration;")
        getExtras = JavaMethod("()Landroid/os/PersistableBundle;")
        getEventType = JavaMethod("()I")