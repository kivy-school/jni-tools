from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["TranslationCapability"]

class TranslationCapability(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/view/translation/TranslationCapability"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    STATE_AVAILABLE_TO_DOWNLOAD = JavaStaticField("I")
    STATE_DOWNLOADING = JavaStaticField("I")
    STATE_NOT_AVAILABLE = JavaStaticField("I")
    STATE_ON_DEVICE = JavaStaticField("I")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    getSourceSpec = JavaMethod("()Landroid/view/translation/TranslationSpec;")
    getTargetSpec = JavaMethod("()Landroid/view/translation/TranslationSpec;")
    getSupportedTranslationFlags = JavaMethod("()I")
    isUiTranslationEnabled = JavaMethod("()Z")
    toString = JavaMethod("()Ljava/lang/String;")
    getState = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")