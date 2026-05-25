from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["TextClassification"]

class TextClassification(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/view/textclassifier/TextClassification"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    getText = JavaMethod("()Ljava/lang/String;")
    getEntityCount = JavaMethod("()I")
    getEntity = JavaMethod("(I)Ljava/lang/String;")
    getConfidenceScore = JavaMethod("(Ljava/lang/String;)F")
    getActions = JavaMethod("()Ljava/util/List;")
    getIcon = JavaMethod("()Landroid/graphics/drawable/Drawable;")
    getLabel = JavaMethod("()Ljava/lang/CharSequence;")
    getIntent = JavaMethod("()Landroid/content/Intent;")
    getOnClickListener = JavaMethod("()Landroid/view/View$OnClickListener;")
    getId = JavaMethod("()Ljava/lang/String;")
    getExtras = JavaMethod("()Landroid/os/Bundle;")
    toString = JavaMethod("()Ljava/lang/String;")
    describeContents = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/view/textclassifier/TextClassification/Builder"
        __javaconstructor__ = [("()V", False)]
        setText = JavaMethod("(Ljava/lang/String;)Landroid/view/textclassifier/TextClassification$Builder;")
        setEntityType = JavaMethod("(Ljava/lang/String;F)Landroid/view/textclassifier/TextClassification$Builder;")
        addAction = JavaMethod("(Landroid/app/RemoteAction;)Landroid/view/textclassifier/TextClassification$Builder;")
        setIcon = JavaMethod("(Landroid/graphics/drawable/Drawable;)Landroid/view/textclassifier/TextClassification$Builder;")
        setLabel = JavaMethod("(Ljava/lang/String;)Landroid/view/textclassifier/TextClassification$Builder;")
        setIntent = JavaMethod("(Landroid/content/Intent;)Landroid/view/textclassifier/TextClassification$Builder;")
        setOnClickListener = JavaMethod("(Landroid/view/View$OnClickListener;)Landroid/view/textclassifier/TextClassification$Builder;")
        setId = JavaMethod("(Ljava/lang/String;)Landroid/view/textclassifier/TextClassification$Builder;")
        setExtras = JavaMethod("(Landroid/os/Bundle;)Landroid/view/textclassifier/TextClassification$Builder;")
        build = JavaMethod("()Landroid/view/textclassifier/TextClassification;")

    class Request(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/view/textclassifier/TextClassification/Request"
        CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
        getText = JavaMethod("()Ljava/lang/CharSequence;")
        getStartIndex = JavaMethod("()I")
        getEndIndex = JavaMethod("()I")
        getDefaultLocales = JavaMethod("()Landroid/os/LocaleList;")
        getReferenceTime = JavaMethod("()Ljava/time/ZonedDateTime;")
        getCallingPackageName = JavaMethod("()Ljava/lang/String;")
        getExtras = JavaMethod("()Landroid/os/Bundle;")
        describeContents = JavaMethod("()I")
        writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")

        class Builder(JavaClass, metaclass=MetaJavaClass):
            __javaclass__ = "android/view/textclassifier/TextClassification/Request/Builder"
            __javaconstructor__ = [("(Ljava/lang/CharSequence;II)V", False)]
            setDefaultLocales = JavaMethod("(Landroid/os/LocaleList;)Landroid/view/textclassifier/TextClassification$Request$Builder;")
            setReferenceTime = JavaMethod("(Ljava/time/ZonedDateTime;)Landroid/view/textclassifier/TextClassification$Request$Builder;")
            setExtras = JavaMethod("(Landroid/os/Bundle;)Landroid/view/textclassifier/TextClassification$Request$Builder;")
            build = JavaMethod("()Landroid/view/textclassifier/TextClassification$Request;")