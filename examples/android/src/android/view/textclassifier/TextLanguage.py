from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["TextLanguage"]

class TextLanguage(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/view/textclassifier/TextLanguage"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    getId = JavaMethod("()Ljava/lang/String;")
    getLocaleHypothesisCount = JavaMethod("()I")
    getLocale = JavaMethod("(I)Landroid/icu/util/ULocale;")
    getConfidenceScore = JavaMethod("(Landroid/icu/util/ULocale;)F")
    getExtras = JavaMethod("()Landroid/os/Bundle;")
    toString = JavaMethod("()Ljava/lang/String;")
    describeContents = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/view/textclassifier/TextLanguage/Builder"
        __javaconstructor__ = [("()V", False)]
        putLocale = JavaMethod("(Landroid/icu/util/ULocale;F)Landroid/view/textclassifier/TextLanguage$Builder;")
        setId = JavaMethod("(Ljava/lang/String;)Landroid/view/textclassifier/TextLanguage$Builder;")
        setExtras = JavaMethod("(Landroid/os/Bundle;)Landroid/view/textclassifier/TextLanguage$Builder;")
        build = JavaMethod("()Landroid/view/textclassifier/TextLanguage;")

    class Request(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/view/textclassifier/TextLanguage/Request"
        CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
        getText = JavaMethod("()Ljava/lang/CharSequence;")
        getCallingPackageName = JavaMethod("()Ljava/lang/String;")
        getExtras = JavaMethod("()Landroid/os/Bundle;")
        describeContents = JavaMethod("()I")
        writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")

        class Builder(JavaClass, metaclass=MetaJavaClass):
            __javaclass__ = "android/view/textclassifier/TextLanguage/Request/Builder"
            __javaconstructor__ = [("(Ljava/lang/CharSequence;)V", False)]
            setExtras = JavaMethod("(Landroid/os/Bundle;)Landroid/view/textclassifier/TextLanguage$Request$Builder;")
            build = JavaMethod("()Landroid/view/textclassifier/TextLanguage$Request;")