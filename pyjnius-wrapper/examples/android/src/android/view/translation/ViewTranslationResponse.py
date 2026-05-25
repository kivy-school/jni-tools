from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ViewTranslationResponse"]

class ViewTranslationResponse(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/view/translation/ViewTranslationResponse"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    getValue = JavaMethod("(Ljava/lang/String;)Landroid/view/translation/TranslationResponseValue;")
    getKeys = JavaMethod("()Ljava/util/Set;")
    getAutofillId = JavaMethod("()Landroid/view/autofill/AutofillId;")
    toString = JavaMethod("()Ljava/lang/String;")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/view/translation/ViewTranslationResponse/Builder"
        __javaconstructor__ = [("(Landroid/view/autofill/AutofillId;)V", False)]
        build = JavaMethod("()Landroid/view/translation/ViewTranslationResponse;")
        setValue = JavaMethod("(Ljava/lang/String;Landroid/view/translation/TranslationResponseValue;)Landroid/view/translation/ViewTranslationResponse$Builder;")