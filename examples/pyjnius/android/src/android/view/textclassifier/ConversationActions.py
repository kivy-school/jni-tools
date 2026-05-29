from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ConversationActions"]

class ConversationActions(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/view/textclassifier/ConversationActions"
    __javaconstructor__ = [("(Ljava/util/List;Ljava/lang/String;)V", False)]
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    getConversationActions = JavaMethod("()Ljava/util/List;")
    getId = JavaMethod("()Ljava/lang/String;")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")

    class Request(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/view/textclassifier/ConversationActions$Request"
        CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
        HINT_FOR_IN_APP = JavaStaticField("Ljava/lang/String;")
        HINT_FOR_NOTIFICATION = JavaStaticField("Ljava/lang/String;")
        CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
        PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
        getHints = JavaMethod("()Ljava/util/List;")
        getMaxSuggestions = JavaMethod("()I")
        getConversation = JavaMethod("()Ljava/util/List;")
        getTypeConfig = JavaMethod("()Landroid/view/textclassifier/TextClassifier$EntityConfig;")
        getCallingPackageName = JavaMethod("()Ljava/lang/String;")
        getExtras = JavaMethod("()Landroid/os/Bundle;")
        writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
        describeContents = JavaMethod("()I")

        class Builder(JavaClass, metaclass=MetaJavaClass):
            __javaclass__ = "android/view/textclassifier/ConversationActions$Request$Builder"
            __javaconstructor__ = [("(Ljava/util/List;)V", False)]
            setMaxSuggestions = JavaMethod("(I)Landroid/view/textclassifier/ConversationActions$Request$Builder;")
            setTypeConfig = JavaMethod("(Landroid/view/textclassifier/TextClassifier$EntityConfig;)Landroid/view/textclassifier/ConversationActions$Request$Builder;")
            setHints = JavaMethod("(Ljava/util/List;)Landroid/view/textclassifier/ConversationActions$Request$Builder;")
            setExtras = JavaMethod("(Landroid/os/Bundle;)Landroid/view/textclassifier/ConversationActions$Request$Builder;")
            build = JavaMethod("()Landroid/view/textclassifier/ConversationActions$Request;")

    class Message(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/view/textclassifier/ConversationActions$Message"
        CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
        PERSON_USER_OTHERS = JavaStaticField("Landroid/app/Person;")
        PERSON_USER_SELF = JavaStaticField("Landroid/app/Person;")
        CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
        PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
        getReferenceTime = JavaMethod("()Ljava/time/ZonedDateTime;")
        getAuthor = JavaMethod("()Landroid/app/Person;")
        getExtras = JavaMethod("()Landroid/os/Bundle;")
        writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
        describeContents = JavaMethod("()I")
        getText = JavaMethod("()Ljava/lang/CharSequence;")

        class Builder(JavaClass, metaclass=MetaJavaClass):
            __javaclass__ = "android/view/textclassifier/ConversationActions$Message$Builder"
            __javaconstructor__ = [("(Landroid/app/Person;)V", False)]
            setReferenceTime = JavaMethod("(Ljava/time/ZonedDateTime;)Landroid/view/textclassifier/ConversationActions$Message$Builder;")
            setExtras = JavaMethod("(Landroid/os/Bundle;)Landroid/view/textclassifier/ConversationActions$Message$Builder;")
            build = JavaMethod("()Landroid/view/textclassifier/ConversationActions$Message;")
            setText = JavaMethod("(Ljava/lang/CharSequence;)Landroid/view/textclassifier/ConversationActions$Message$Builder;")