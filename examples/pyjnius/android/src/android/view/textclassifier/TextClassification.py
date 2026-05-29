from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["TextClassification"]

class TextClassification(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/view/textclassifier/TextClassification"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    getEntityCount = JavaMethod("()I")
    getEntity = JavaMethod("(I)Ljava/lang/String;")
    toString = JavaMethod("()Ljava/lang/String;")
    getId = JavaMethod("()Ljava/lang/String;")
    getLabel = JavaMethod("()Ljava/lang/CharSequence;")
    getActions = JavaMethod("()Ljava/util/List;")
    getOnClickListener = JavaMethod("()Landroid/view/View$OnClickListener;")
    getIntent = JavaMethod("()Landroid/content/Intent;")
    getExtras = JavaMethod("()Landroid/os/Bundle;")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")
    getIcon = JavaMethod("()Landroid/graphics/drawable/Drawable;")
    getText = JavaMethod("()Ljava/lang/String;")
    getConfidenceScore = JavaMethod("(Ljava/lang/String;)F")

    class Request(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/view/textclassifier/TextClassification$Request"
        CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
        CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
        PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
        getEndIndex = JavaMethod("()I")
        getStartIndex = JavaMethod("()I")
        getDefaultLocales = JavaMethod("()Landroid/os/LocaleList;")
        getCallingPackageName = JavaMethod("()Ljava/lang/String;")
        getReferenceTime = JavaMethod("()Ljava/time/ZonedDateTime;")
        getExtras = JavaMethod("()Landroid/os/Bundle;")
        writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
        describeContents = JavaMethod("()I")
        getText = JavaMethod("()Ljava/lang/CharSequence;")

        class Builder(JavaClass, metaclass=MetaJavaClass):
            __javaclass__ = "android/view/textclassifier/TextClassification$Request$Builder"
            __javaconstructor__ = [("(Ljava/lang/CharSequence;II)V", False)]
            setReferenceTime = JavaMethod("(Ljava/time/ZonedDateTime;)Landroid/view/textclassifier/TextClassification$Request$Builder;")
            setDefaultLocales = JavaMethod("(Landroid/os/LocaleList;)Landroid/view/textclassifier/TextClassification$Request$Builder;")
            setExtras = JavaMethod("(Landroid/os/Bundle;)Landroid/view/textclassifier/TextClassification$Request$Builder;")
            build = JavaMethod("()Landroid/view/textclassifier/TextClassification$Request;")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/view/textclassifier/TextClassification$Builder"
        __javaconstructor__ = [("()V", False)]
        setEntityType = JavaMethod("(Ljava/lang/String;F)Landroid/view/textclassifier/TextClassification$Builder;")
        setId = JavaMethod("(Ljava/lang/String;)Landroid/view/textclassifier/TextClassification$Builder;")
        setOnClickListener = JavaMethod("(Landroid/view/View$OnClickListener;)Landroid/view/textclassifier/TextClassification$Builder;")
        setIcon = JavaMethod("(Landroid/graphics/drawable/Drawable;)Landroid/view/textclassifier/TextClassification$Builder;")
        setIntent = JavaMethod("(Landroid/content/Intent;)Landroid/view/textclassifier/TextClassification$Builder;")
        setExtras = JavaMethod("(Landroid/os/Bundle;)Landroid/view/textclassifier/TextClassification$Builder;")
        addAction = JavaMethod("(Landroid/app/RemoteAction;)Landroid/view/textclassifier/TextClassification$Builder;")
        setLabel = JavaMethod("(Ljava/lang/String;)Landroid/view/textclassifier/TextClassification$Builder;")
        build = JavaMethod("()Landroid/view/textclassifier/TextClassification;")
        setText = JavaMethod("(Ljava/lang/String;)Landroid/view/textclassifier/TextClassification$Builder;")