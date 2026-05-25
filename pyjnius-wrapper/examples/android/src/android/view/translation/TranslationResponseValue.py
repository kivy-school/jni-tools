from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["TranslationResponseValue"]

class TranslationResponseValue(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/view/translation/TranslationResponseValue"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    EXTRA_DEFINITIONS = JavaStaticField("Ljava/lang/String;")
    STATUS_ERROR = JavaStaticField("I")
    STATUS_SUCCESS = JavaStaticField("I")
    forError = JavaStaticMethod("()Landroid/view/translation/TranslationResponseValue;")
    getStatusCode = JavaMethod("()I")
    getText = JavaMethod("()Ljava/lang/CharSequence;")
    getExtras = JavaMethod("()Landroid/os/Bundle;")
    getTransliteration = JavaMethod("()Ljava/lang/CharSequence;")
    toString = JavaMethod("()Ljava/lang/String;")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/view/translation/TranslationResponseValue/Builder"
        __javaconstructor__ = [("(I)V", False)]
        setText = JavaMethod("(Ljava/lang/CharSequence;)Landroid/view/translation/TranslationResponseValue$Builder;")
        setExtras = JavaMethod("(Landroid/os/Bundle;)Landroid/view/translation/TranslationResponseValue$Builder;")
        setTransliteration = JavaMethod("(Ljava/lang/CharSequence;)Landroid/view/translation/TranslationResponseValue$Builder;")
        build = JavaMethod("()Landroid/view/translation/TranslationResponseValue;")