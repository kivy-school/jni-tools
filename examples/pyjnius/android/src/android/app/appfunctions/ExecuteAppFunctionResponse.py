from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ExecuteAppFunctionResponse"]

class ExecuteAppFunctionResponse(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/app/appfunctions/ExecuteAppFunctionResponse"
    __javaconstructor__ = [("(Landroid/app/appsearch/GenericDocument;)V", False), ("(Landroid/app/appsearch/GenericDocument;Landroid/os/Bundle;)V", False)]
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    PROPERTY_RETURN_VALUE = JavaStaticField("Ljava/lang/String;")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    getExtras = JavaMethod("()Landroid/os/Bundle;")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")
    getResultDocument = JavaMethod("()Landroid/app/appsearch/GenericDocument;")