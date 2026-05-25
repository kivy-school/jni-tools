from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["TvInteractiveAppServiceInfo"]

class TvInteractiveAppServiceInfo(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/media/tv/interactive/TvInteractiveAppServiceInfo"
    __javaconstructor__ = [("(Landroid/content/Context;Landroid/content/ComponentName;)V", False)]
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    INTERACTIVE_APP_TYPE_ATSC = JavaStaticField("I")
    INTERACTIVE_APP_TYPE_GINGA = JavaStaticField("I")
    INTERACTIVE_APP_TYPE_HBBTV = JavaStaticField("I")
    INTERACTIVE_APP_TYPE_OTHER = JavaStaticField("I")
    INTERACTIVE_APP_TYPE_TARGETED_AD = JavaStaticField("I")
    describeContents = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    getId = JavaMethod("()Ljava/lang/String;")
    getServiceInfo = JavaMethod("()Landroid/content/pm/ServiceInfo;")
    getSupportedTypes = JavaMethod("()I")
    getCustomSupportedTypes = JavaMethod("()Ljava/util/List;")