from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ConversationActions"]

class ConversationActions(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/view/textclassifier/ConversationActions"
    __javaconstructor__ = [("(Ljava/util/List;Ljava/lang/String;)V", False)]
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    describeContents = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    getConversationActions = JavaMethod("()Ljava/util/List;")
    getId = JavaMethod("()Ljava/lang/String;")

    class Message(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/view/textclassifier/ConversationActions/Message"
        CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
        PERSON_USER_OTHERS = JavaStaticField("Landroid/app/Person;")
        PERSON_USER_SELF = JavaStaticField("Landroid/app/Person;")
        writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
        describeContents = JavaMethod("()I")
        getAuthor = JavaMethod("()Landroid/app/Person;")
        getReferenceTime = JavaMethod("()Ljava/time/ZonedDateTime;")
        getText = JavaMethod("()Ljava/lang/CharSequence;")
        getExtras = JavaMethod("()Landroid/os/Bundle;")

        class Builder(JavaClass, metaclass=MetaJavaClass):
            __javaclass__ = "android/view/textclassifier/ConversationActions/Message/Builder"
            __javaconstructor__ = [("(Landroid/app/Person;)V", False)]
            setText = JavaMethod("(Ljava/lang/CharSequence;)Landroid/view/textclassifier/ConversationActions$Message$Builder;")
            setReferenceTime = JavaMethod("(Ljava/time/ZonedDateTime;)Landroid/view/textclassifier/ConversationActions$Message$Builder;")
            setExtras = JavaMethod("(Landroid/os/Bundle;)Landroid/view/textclassifier/ConversationActions$Message$Builder;")
            build = JavaMethod("()Landroid/view/textclassifier/ConversationActions$Message;")

    class Request(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/view/textclassifier/ConversationActions/Request"
        CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
        HINT_FOR_IN_APP = JavaStaticField("Ljava/lang/String;")
        HINT_FOR_NOTIFICATION = JavaStaticField("Ljava/lang/String;")
        writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
        describeContents = JavaMethod("()I")
        getTypeConfig = JavaMethod("()Landroid/view/textclassifier/TextClassifier$EntityConfig;")
        getConversation = JavaMethod("()Ljava/util/List;")
        getMaxSuggestions = JavaMethod("()I")
        getHints = JavaMethod("()Ljava/util/List;")
        getCallingPackageName = JavaMethod("()Ljava/lang/String;")
        getExtras = JavaMethod("()Landroid/os/Bundle;")

        class Builder(JavaClass, metaclass=MetaJavaClass):
            __javaclass__ = "android/view/textclassifier/ConversationActions/Request/Builder"
            __javaconstructor__ = [("(Ljava/util/List;)V", False)]
            setHints = JavaMethod("(Ljava/util/List;)Landroid/view/textclassifier/ConversationActions$Request$Builder;")
            setTypeConfig = JavaMethod("(Landroid/view/textclassifier/TextClassifier$EntityConfig;)Landroid/view/textclassifier/ConversationActions$Request$Builder;")
            setMaxSuggestions = JavaMethod("(I)Landroid/view/textclassifier/ConversationActions$Request$Builder;")
            setExtras = JavaMethod("(Landroid/os/Bundle;)Landroid/view/textclassifier/ConversationActions$Request$Builder;")
            build = JavaMethod("()Landroid/view/textclassifier/ConversationActions$Request;")