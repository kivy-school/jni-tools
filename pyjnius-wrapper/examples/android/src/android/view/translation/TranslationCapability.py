from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["TranslationCapability"]

class TranslationCapability(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/view/translation/TranslationCapability"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    STATE_AVAILABLE_TO_DOWNLOAD = JavaStaticField("I")
    STATE_DOWNLOADING = JavaStaticField("I")
    STATE_NOT_AVAILABLE = JavaStaticField("I")
    STATE_ON_DEVICE = JavaStaticField("I")
    getState = JavaMethod("()I")
    getSourceSpec = JavaMethod("()Landroid/view/translation/TranslationSpec;")
    getTargetSpec = JavaMethod("()Landroid/view/translation/TranslationSpec;")
    isUiTranslationEnabled = JavaMethod("()Z")
    getSupportedTranslationFlags = JavaMethod("()I")
    toString = JavaMethod("()Ljava/lang/String;")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")