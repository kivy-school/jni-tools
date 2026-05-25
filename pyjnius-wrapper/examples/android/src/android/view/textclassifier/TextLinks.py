from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["TextLinks"]

class TextLinks(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/view/textclassifier/TextLinks"
    APPLY_STRATEGY_IGNORE = JavaStaticField("I")
    APPLY_STRATEGY_REPLACE = JavaStaticField("I")
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    STATUS_DIFFERENT_TEXT = JavaStaticField("I")
    STATUS_LINKS_APPLIED = JavaStaticField("I")
    STATUS_NO_LINKS_APPLIED = JavaStaticField("I")
    STATUS_NO_LINKS_FOUND = JavaStaticField("I")
    STATUS_UNSUPPORTED_CHARACTER = JavaStaticField("I")
    getText = JavaMethod("()Ljava/lang/CharSequence;")
    getLinks = JavaMethod("()Ljava/util/Collection;")
    getExtras = JavaMethod("()Landroid/os/Bundle;")
    apply = JavaMethod("(Landroid/text/Spannable;ILjava/util/function/Function;)I")
    toString = JavaMethod("()Ljava/lang/String;")
    describeContents = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/view/textclassifier/TextLinks/Builder"
        __javaconstructor__ = [("(Ljava/lang/String;)V", False)]
        addLink = JavaMultipleMethod([("(IILjava/util/Map;)Landroid/view/textclassifier/TextLinks$Builder;", False, False), ("(IILjava/util/Map;Landroid/os/Bundle;)Landroid/view/textclassifier/TextLinks$Builder;", False, False)])
        clearTextLinks = JavaMethod("()Landroid/view/textclassifier/TextLinks$Builder;")
        setExtras = JavaMethod("(Landroid/os/Bundle;)Landroid/view/textclassifier/TextLinks$Builder;")
        build = JavaMethod("()Landroid/view/textclassifier/TextLinks;")

    class Request(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/view/textclassifier/TextLinks/Request"
        CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
        getText = JavaMethod("()Ljava/lang/CharSequence;")
        getDefaultLocales = JavaMethod("()Landroid/os/LocaleList;")
        getEntityConfig = JavaMethod("()Landroid/view/textclassifier/TextClassifier$EntityConfig;")
        getReferenceTime = JavaMethod("()Ljava/time/ZonedDateTime;")
        getCallingPackageName = JavaMethod("()Ljava/lang/String;")
        getExtras = JavaMethod("()Landroid/os/Bundle;")
        describeContents = JavaMethod("()I")
        writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")

        class Builder(JavaClass, metaclass=MetaJavaClass):
            __javaclass__ = "android/view/textclassifier/TextLinks/Request/Builder"
            __javaconstructor__ = [("(Ljava/lang/CharSequence;)V", False)]
            setDefaultLocales = JavaMethod("(Landroid/os/LocaleList;)Landroid/view/textclassifier/TextLinks$Request$Builder;")
            setEntityConfig = JavaMethod("(Landroid/view/textclassifier/TextClassifier$EntityConfig;)Landroid/view/textclassifier/TextLinks$Request$Builder;")
            setExtras = JavaMethod("(Landroid/os/Bundle;)Landroid/view/textclassifier/TextLinks$Request$Builder;")
            setReferenceTime = JavaMethod("(Ljava/time/ZonedDateTime;)Landroid/view/textclassifier/TextLinks$Request$Builder;")
            build = JavaMethod("()Landroid/view/textclassifier/TextLinks$Request;")

    class TextLink(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/view/textclassifier/TextLinks/TextLink"
        CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
        getStart = JavaMethod("()I")
        getEnd = JavaMethod("()I")
        getEntityCount = JavaMethod("()I")
        getEntity = JavaMethod("(I)Ljava/lang/String;")
        getConfidenceScore = JavaMethod("(Ljava/lang/String;)F")
        getExtras = JavaMethod("()Landroid/os/Bundle;")
        toString = JavaMethod("()Ljava/lang/String;")
        describeContents = JavaMethod("()I")
        writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")

    class TextLinkSpan(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/view/textclassifier/TextLinks/TextLinkSpan"
        __javaconstructor__ = [("(Landroid/view/textclassifier/TextLinks$TextLink;)V", False)]
        onClick = JavaMethod("(Landroid/view/View;)V")
        getTextLink = JavaMethod("()Landroid/view/textclassifier/TextLinks$TextLink;")