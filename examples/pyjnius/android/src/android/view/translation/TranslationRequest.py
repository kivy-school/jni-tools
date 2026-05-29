from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["TranslationRequest"]

class TranslationRequest(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/view/translation/TranslationRequest"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    FLAG_DICTIONARY_RESULT = JavaStaticField("I")
    FLAG_PARTIAL_RESPONSES = JavaStaticField("I")
    FLAG_TRANSLATION_RESULT = JavaStaticField("I")
    FLAG_TRANSLITERATION_RESULT = JavaStaticField("I")
    getFlags = JavaMethod("()I")
    getTranslationRequestValues = JavaMethod("()Ljava/util/List;")
    getViewTranslationRequests = JavaMethod("()Ljava/util/List;")
    toString = JavaMethod("()Ljava/lang/String;")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/view/translation/TranslationRequest/Builder"
        __javaconstructor__ = [("()V", False)]
        setFlags = JavaMethod("(I)Landroid/view/translation/TranslationRequest$Builder;")
        setTranslationRequestValues = JavaMethod("(Ljava/util/List;)Landroid/view/translation/TranslationRequest$Builder;")
        setViewTranslationRequests = JavaMethod("(Ljava/util/List;)Landroid/view/translation/TranslationRequest$Builder;")
        build = JavaMethod("()Landroid/view/translation/TranslationRequest;")