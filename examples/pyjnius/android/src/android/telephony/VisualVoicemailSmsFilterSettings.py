from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["VisualVoicemailSmsFilterSettings"]

class VisualVoicemailSmsFilterSettings(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/telephony/VisualVoicemailSmsFilterSettings"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    DESTINATION_PORT_ANY = JavaStaticField("I")
    DESTINATION_PORT_DATA_SMS = JavaStaticField("I")
    clientPrefix = JavaField("Ljava/lang/String;")
    destinationPort = JavaField("I")
    originatingNumbers = JavaField("Ljava/util/List;")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    toString = JavaMethod("()Ljava/lang/String;")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/telephony/VisualVoicemailSmsFilterSettings$Builder"
        __javaconstructor__ = [("()V", False)]
        setDestinationPort = JavaMethod("(I)Landroid/telephony/VisualVoicemailSmsFilterSettings$Builder;")
        setClientPrefix = JavaMethod("(Ljava/lang/String;)Landroid/telephony/VisualVoicemailSmsFilterSettings$Builder;")
        setOriginatingNumbers = JavaMethod("(Ljava/util/List;)Landroid/telephony/VisualVoicemailSmsFilterSettings$Builder;")
        build = JavaMethod("()Landroid/telephony/VisualVoicemailSmsFilterSettings;")