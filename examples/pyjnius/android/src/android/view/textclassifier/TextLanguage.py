from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["TextLanguage"]

class TextLanguage(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/view/textclassifier/TextLanguage"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    getLocaleHypothesisCount = JavaMethod("()I")
    toString = JavaMethod("()Ljava/lang/String;")
    getId = JavaMethod("()Ljava/lang/String;")
    getLocale = JavaMethod("(I)Landroid/icu/util/ULocale;")
    getExtras = JavaMethod("()Landroid/os/Bundle;")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")
    getConfidenceScore = JavaMethod("(Landroid/icu/util/ULocale;)F")

    class Request(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/view/textclassifier/TextLanguage$Request"
        CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
        CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
        PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
        getCallingPackageName = JavaMethod("()Ljava/lang/String;")
        getExtras = JavaMethod("()Landroid/os/Bundle;")
        writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
        describeContents = JavaMethod("()I")
        getText = JavaMethod("()Ljava/lang/CharSequence;")

        class Builder(JavaClass, metaclass=MetaJavaClass):
            __javaclass__ = "android/view/textclassifier/TextLanguage$Request$Builder"
            __javaconstructor__ = [("(Ljava/lang/CharSequence;)V", False)]
            setExtras = JavaMethod("(Landroid/os/Bundle;)Landroid/view/textclassifier/TextLanguage$Request$Builder;")
            build = JavaMethod("()Landroid/view/textclassifier/TextLanguage$Request;")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/view/textclassifier/TextLanguage$Builder"
        __javaconstructor__ = [("()V", False)]
        putLocale = JavaMethod("(Landroid/icu/util/ULocale;F)Landroid/view/textclassifier/TextLanguage$Builder;")
        setId = JavaMethod("(Ljava/lang/String;)Landroid/view/textclassifier/TextLanguage$Builder;")
        setExtras = JavaMethod("(Landroid/os/Bundle;)Landroid/view/textclassifier/TextLanguage$Builder;")
        build = JavaMethod("()Landroid/view/textclassifier/TextLanguage;")