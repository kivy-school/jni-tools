from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["TextSelection"]

class TextSelection(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/view/textclassifier/TextSelection"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    getSelectionStartIndex = JavaMethod("()I")
    getSelectionEndIndex = JavaMethod("()I")
    getEntityCount = JavaMethod("()I")
    getEntity = JavaMethod("(I)Ljava/lang/String;")
    getConfidenceScore = JavaMethod("(Ljava/lang/String;)F")
    getId = JavaMethod("()Ljava/lang/String;")
    getTextClassification = JavaMethod("()Landroid/view/textclassifier/TextClassification;")
    getExtras = JavaMethod("()Landroid/os/Bundle;")
    toString = JavaMethod("()Ljava/lang/String;")
    describeContents = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/view/textclassifier/TextSelection/Builder"
        __javaconstructor__ = [("(II)V", False)]
        setEntityType = JavaMethod("(Ljava/lang/String;F)Landroid/view/textclassifier/TextSelection$Builder;")
        setId = JavaMethod("(Ljava/lang/String;)Landroid/view/textclassifier/TextSelection$Builder;")
        setTextClassification = JavaMethod("(Landroid/view/textclassifier/TextClassification;)Landroid/view/textclassifier/TextSelection$Builder;")
        setExtras = JavaMethod("(Landroid/os/Bundle;)Landroid/view/textclassifier/TextSelection$Builder;")
        build = JavaMethod("()Landroid/view/textclassifier/TextSelection;")

    class Request(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/view/textclassifier/TextSelection/Request"
        CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
        getText = JavaMethod("()Ljava/lang/CharSequence;")
        getStartIndex = JavaMethod("()I")
        getEndIndex = JavaMethod("()I")
        getDefaultLocales = JavaMethod("()Landroid/os/LocaleList;")
        getCallingPackageName = JavaMethod("()Ljava/lang/String;")
        shouldIncludeTextClassification = JavaMethod("()Z")
        getExtras = JavaMethod("()Landroid/os/Bundle;")
        describeContents = JavaMethod("()I")
        writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")

        class Builder(JavaClass, metaclass=MetaJavaClass):
            __javaclass__ = "android/view/textclassifier/TextSelection/Request/Builder"
            __javaconstructor__ = [("(Ljava/lang/CharSequence;II)V", False)]
            setDefaultLocales = JavaMethod("(Landroid/os/LocaleList;)Landroid/view/textclassifier/TextSelection$Request$Builder;")
            setIncludeTextClassification = JavaMethod("(Z)Landroid/view/textclassifier/TextSelection$Request$Builder;")
            setExtras = JavaMethod("(Landroid/os/Bundle;)Landroid/view/textclassifier/TextSelection$Request$Builder;")
            build = JavaMethod("()Landroid/view/textclassifier/TextSelection$Request;")