from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["TvInputInfo"]

class TvInputInfo(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/media/tv/TvInputInfo"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    EXTRA_INPUT_ID = JavaStaticField("Ljava/lang/String;")
    TYPE_COMPONENT = JavaStaticField("I")
    TYPE_COMPOSITE = JavaStaticField("I")
    TYPE_DISPLAY_PORT = JavaStaticField("I")
    TYPE_DVI = JavaStaticField("I")
    TYPE_HDMI = JavaStaticField("I")
    TYPE_OTHER = JavaStaticField("I")
    TYPE_SCART = JavaStaticField("I")
    TYPE_SVIDEO = JavaStaticField("I")
    TYPE_TUNER = JavaStaticField("I")
    TYPE_VGA = JavaStaticField("I")
    getId = JavaMethod("()Ljava/lang/String;")
    getParentId = JavaMethod("()Ljava/lang/String;")
    getServiceInfo = JavaMethod("()Landroid/content/pm/ServiceInfo;")
    createSetupIntent = JavaMethod("()Landroid/content/Intent;")
    createSettingsIntent = JavaMethod("()Landroid/content/Intent;")
    getType = JavaMethod("()I")
    getTunerCount = JavaMethod("()I")
    canRecord = JavaMethod("()Z")
    canPauseRecording = JavaMethod("()Z")
    getExtras = JavaMethod("()Landroid/os/Bundle;")
    isPassthroughInput = JavaMethod("()Z")
    isHidden = JavaMethod("(Landroid/content/Context;)Z")
    loadLabel = JavaMethod("(Landroid/content/Context;)Ljava/lang/CharSequence;")
    loadCustomLabel = JavaMethod("(Landroid/content/Context;)Ljava/lang/CharSequence;")
    loadIcon = JavaMethod("(Landroid/content/Context;)Landroid/graphics/drawable/Drawable;")
    describeContents = JavaMethod("()I")
    hashCode = JavaMethod("()I")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    toString = JavaMethod("()Ljava/lang/String;")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/media/tv/TvInputInfo/Builder"
        __javaconstructor__ = [("(Landroid/content/Context;Landroid/content/ComponentName;)V", False)]
        setTunerCount = JavaMethod("(I)Landroid/media/tv/TvInputInfo$Builder;")
        setCanRecord = JavaMethod("(Z)Landroid/media/tv/TvInputInfo$Builder;")
        setCanPauseRecording = JavaMethod("(Z)Landroid/media/tv/TvInputInfo$Builder;")
        setExtras = JavaMethod("(Landroid/os/Bundle;)Landroid/media/tv/TvInputInfo$Builder;")
        build = JavaMethod("()Landroid/media/tv/TvInputInfo;")