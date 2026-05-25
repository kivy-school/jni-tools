from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["VisualVoicemailSmsFilterSettings"]

class VisualVoicemailSmsFilterSettings(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/telephony/VisualVoicemailSmsFilterSettings"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    DESTINATION_PORT_ANY = JavaStaticField("I")
    DESTINATION_PORT_DATA_SMS = JavaStaticField("I")
    clientPrefix = JavaField("Ljava/lang/String;")
    destinationPort = JavaField("I")
    originatingNumbers = JavaField("Ljava/util/List;")
    describeContents = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    toString = JavaMethod("()Ljava/lang/String;")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/telephony/VisualVoicemailSmsFilterSettings/Builder"
        __javaconstructor__ = [("()V", False)]
        build = JavaMethod("()Landroid/telephony/VisualVoicemailSmsFilterSettings;")
        setClientPrefix = JavaMethod("(Ljava/lang/String;)Landroid/telephony/VisualVoicemailSmsFilterSettings$Builder;")
        setOriginatingNumbers = JavaMethod("(Ljava/util/List;)Landroid/telephony/VisualVoicemailSmsFilterSettings$Builder;")
        setDestinationPort = JavaMethod("(I)Landroid/telephony/VisualVoicemailSmsFilterSettings$Builder;")