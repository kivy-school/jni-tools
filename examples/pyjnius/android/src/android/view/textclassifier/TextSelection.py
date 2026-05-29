from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["TextSelection"]

class TextSelection(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/view/textclassifier/TextSelection"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    getEntityCount = JavaMethod("()I")
    getEntity = JavaMethod("(I)Ljava/lang/String;")
    getSelectionEndIndex = JavaMethod("()I")
    getSelectionStartIndex = JavaMethod("()I")
    getTextClassification = JavaMethod("()Landroid/view/textclassifier/TextClassification;")
    toString = JavaMethod("()Ljava/lang/String;")
    getId = JavaMethod("()Ljava/lang/String;")
    getExtras = JavaMethod("()Landroid/os/Bundle;")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")
    getConfidenceScore = JavaMethod("(Ljava/lang/String;)F")

    class Request(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/view/textclassifier/TextSelection$Request"
        CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
        CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
        PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
        getEndIndex = JavaMethod("()I")
        getStartIndex = JavaMethod("()I")
        shouldIncludeTextClassification = JavaMethod("()Z")
        getDefaultLocales = JavaMethod("()Landroid/os/LocaleList;")
        getCallingPackageName = JavaMethod("()Ljava/lang/String;")
        getExtras = JavaMethod("()Landroid/os/Bundle;")
        writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
        describeContents = JavaMethod("()I")
        getText = JavaMethod("()Ljava/lang/CharSequence;")

        class Builder(JavaClass, metaclass=MetaJavaClass):
            __javaclass__ = "android/view/textclassifier/TextSelection$Request$Builder"
            __javaconstructor__ = [("(Ljava/lang/CharSequence;II)V", False)]
            setIncludeTextClassification = JavaMethod("(Z)Landroid/view/textclassifier/TextSelection$Request$Builder;")
            setDefaultLocales = JavaMethod("(Landroid/os/LocaleList;)Landroid/view/textclassifier/TextSelection$Request$Builder;")
            setExtras = JavaMethod("(Landroid/os/Bundle;)Landroid/view/textclassifier/TextSelection$Request$Builder;")
            build = JavaMethod("()Landroid/view/textclassifier/TextSelection$Request;")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/view/textclassifier/TextSelection$Builder"
        __javaconstructor__ = [("(II)V", False)]
        setTextClassification = JavaMethod("(Landroid/view/textclassifier/TextClassification;)Landroid/view/textclassifier/TextSelection$Builder;")
        setEntityType = JavaMethod("(Ljava/lang/String;F)Landroid/view/textclassifier/TextSelection$Builder;")
        setId = JavaMethod("(Ljava/lang/String;)Landroid/view/textclassifier/TextSelection$Builder;")
        setExtras = JavaMethod("(Landroid/os/Bundle;)Landroid/view/textclassifier/TextSelection$Builder;")
        build = JavaMethod("()Landroid/view/textclassifier/TextSelection;")