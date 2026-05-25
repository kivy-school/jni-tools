from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ServiceInfo"]

class ServiceInfo(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/content/pm/ServiceInfo"
    __javaconstructor__ = [("()V", False), ("(Landroid/content/pm/ServiceInfo;)V", False)]
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    FLAG_ALLOW_SHARED_ISOLATED_PROCESS = JavaStaticField("I")
    FLAG_EXTERNAL_SERVICE = JavaStaticField("I")
    FLAG_ISOLATED_PROCESS = JavaStaticField("I")
    FLAG_SINGLE_USER = JavaStaticField("I")
    FLAG_STOP_WITH_TASK = JavaStaticField("I")
    FLAG_USE_APP_ZYGOTE = JavaStaticField("I")
    FOREGROUND_SERVICE_TYPE_CAMERA = JavaStaticField("I")
    FOREGROUND_SERVICE_TYPE_CONNECTED_DEVICE = JavaStaticField("I")
    FOREGROUND_SERVICE_TYPE_DATA_SYNC = JavaStaticField("I")
    FOREGROUND_SERVICE_TYPE_HEALTH = JavaStaticField("I")
    FOREGROUND_SERVICE_TYPE_LOCATION = JavaStaticField("I")
    FOREGROUND_SERVICE_TYPE_MANIFEST = JavaStaticField("I")
    FOREGROUND_SERVICE_TYPE_MEDIA_PLAYBACK = JavaStaticField("I")
    FOREGROUND_SERVICE_TYPE_MEDIA_PROCESSING = JavaStaticField("I")
    FOREGROUND_SERVICE_TYPE_MEDIA_PROJECTION = JavaStaticField("I")
    FOREGROUND_SERVICE_TYPE_MICROPHONE = JavaStaticField("I")
    FOREGROUND_SERVICE_TYPE_NONE = JavaStaticField("I")
    FOREGROUND_SERVICE_TYPE_PHONE_CALL = JavaStaticField("I")
    FOREGROUND_SERVICE_TYPE_REMOTE_MESSAGING = JavaStaticField("I")
    FOREGROUND_SERVICE_TYPE_SHORT_SERVICE = JavaStaticField("I")
    FOREGROUND_SERVICE_TYPE_SPECIAL_USE = JavaStaticField("I")
    FOREGROUND_SERVICE_TYPE_SYSTEM_EXEMPTED = JavaStaticField("I")
    flags = JavaField("I")
    permission = JavaField("Ljava/lang/String;")
    getForegroundServiceType = JavaMethod("()I")
    dump = JavaMethod("(Landroid/util/Printer;Ljava/lang/String;)V")
    toString = JavaMethod("()Ljava/lang/String;")
    describeContents = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")