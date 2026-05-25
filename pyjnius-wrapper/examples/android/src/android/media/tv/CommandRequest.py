from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["CommandRequest"]

class CommandRequest(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/media/tv/CommandRequest"
    __javaconstructor__ = [("(IILjava/lang/String;Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;)V", False)]
    ARGUMENT_TYPE_JSON = JavaStaticField("Ljava/lang/String;")
    ARGUMENT_TYPE_XML = JavaStaticField("Ljava/lang/String;")
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    getNamespace = JavaMethod("()Ljava/lang/String;")
    getName = JavaMethod("()Ljava/lang/String;")
    getArguments = JavaMethod("()Ljava/lang/String;")
    getArgumentType = JavaMethod("()Ljava/lang/String;")
    describeContents = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")