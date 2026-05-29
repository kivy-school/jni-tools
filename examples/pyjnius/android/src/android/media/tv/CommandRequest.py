from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["CommandRequest"]

class CommandRequest(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/media/tv/CommandRequest"
    __javaconstructor__ = [("(IILjava/lang/String;Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;)V", False)]
    ARGUMENT_TYPE_JSON = JavaStaticField("Ljava/lang/String;")
    ARGUMENT_TYPE_XML = JavaStaticField("Ljava/lang/String;")
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    REQUEST_OPTION_AUTO_UPDATE = JavaStaticField("I")
    REQUEST_OPTION_ONESHOT = JavaStaticField("I")
    REQUEST_OPTION_ONEWAY = JavaStaticField("I")
    REQUEST_OPTION_REPEAT = JavaStaticField("I")
    getArguments = JavaMethod("()Ljava/lang/String;")
    getArgumentType = JavaMethod("()Ljava/lang/String;")
    getName = JavaMethod("()Ljava/lang/String;")
    getNamespace = JavaMethod("()Ljava/lang/String;")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")