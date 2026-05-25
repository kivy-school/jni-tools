from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ConversationAction"]

class ConversationAction(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/view/textclassifier/ConversationAction"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    TYPE_CALL_PHONE = JavaStaticField("Ljava/lang/String;")
    TYPE_CREATE_REMINDER = JavaStaticField("Ljava/lang/String;")
    TYPE_OPEN_URL = JavaStaticField("Ljava/lang/String;")
    TYPE_SEND_EMAIL = JavaStaticField("Ljava/lang/String;")
    TYPE_SEND_SMS = JavaStaticField("Ljava/lang/String;")
    TYPE_SHARE_LOCATION = JavaStaticField("Ljava/lang/String;")
    TYPE_TEXT_REPLY = JavaStaticField("Ljava/lang/String;")
    TYPE_TRACK_FLIGHT = JavaStaticField("Ljava/lang/String;")
    TYPE_VIEW_CALENDAR = JavaStaticField("Ljava/lang/String;")
    TYPE_VIEW_MAP = JavaStaticField("Ljava/lang/String;")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")
    getType = JavaMethod("()Ljava/lang/String;")
    getAction = JavaMethod("()Landroid/app/RemoteAction;")
    getConfidenceScore = JavaMethod("()F")
    getTextReply = JavaMethod("()Ljava/lang/CharSequence;")
    getExtras = JavaMethod("()Landroid/os/Bundle;")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/view/textclassifier/ConversationAction/Builder"
        __javaconstructor__ = [("(Ljava/lang/String;)V", False)]
        setAction = JavaMethod("(Landroid/app/RemoteAction;)Landroid/view/textclassifier/ConversationAction$Builder;")
        setTextReply = JavaMethod("(Ljava/lang/CharSequence;)Landroid/view/textclassifier/ConversationAction$Builder;")
        setConfidenceScore = JavaMethod("(F)Landroid/view/textclassifier/ConversationAction$Builder;")
        setExtras = JavaMethod("(Landroid/os/Bundle;)Landroid/view/textclassifier/ConversationAction$Builder;")
        build = JavaMethod("()Landroid/view/textclassifier/ConversationAction;")