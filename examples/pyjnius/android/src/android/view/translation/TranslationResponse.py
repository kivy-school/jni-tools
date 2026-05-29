from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["TranslationResponse"]

class TranslationResponse(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/view/translation/TranslationResponse"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    TRANSLATION_STATUS_CONTEXT_UNSUPPORTED = JavaStaticField("I")
    TRANSLATION_STATUS_SUCCESS = JavaStaticField("I")
    TRANSLATION_STATUS_UNKNOWN_ERROR = JavaStaticField("I")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    isFinalResponse = JavaMethod("()Z")
    getTranslationResponseValues = JavaMethod("()Landroid/util/SparseArray;")
    getTranslationStatus = JavaMethod("()I")
    getViewTranslationResponses = JavaMethod("()Landroid/util/SparseArray;")
    toString = JavaMethod("()Ljava/lang/String;")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/view/translation/TranslationResponse$Builder"
        __javaconstructor__ = [("(I)V", False)]
        setFinalResponse = JavaMethod("(Z)Landroid/view/translation/TranslationResponse$Builder;")
        setTranslationResponseValues = JavaMethod("(Landroid/util/SparseArray;)Landroid/view/translation/TranslationResponse$Builder;")
        setViewTranslationResponse = JavaMethod("(ILandroid/view/translation/ViewTranslationResponse;)Landroid/view/translation/TranslationResponse$Builder;")
        setTranslationResponseValue = JavaMethod("(ILandroid/view/translation/TranslationResponseValue;)Landroid/view/translation/TranslationResponse$Builder;")
        setViewTranslationResponses = JavaMethod("(Landroid/util/SparseArray;)Landroid/view/translation/TranslationResponse$Builder;")
        build = JavaMethod("()Landroid/view/translation/TranslationResponse;")