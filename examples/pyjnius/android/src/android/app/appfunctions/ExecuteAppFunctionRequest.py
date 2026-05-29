from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ExecuteAppFunctionRequest"]

class ExecuteAppFunctionRequest(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/app/appfunctions/ExecuteAppFunctionRequest"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    getFunctionIdentifier = JavaMethod("()Ljava/lang/String;")
    getParameters = JavaMethod("()Landroid/app/appsearch/GenericDocument;")
    getExtras = JavaMethod("()Landroid/os/Bundle;")
    getTargetPackageName = JavaMethod("()Ljava/lang/String;")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/app/appfunctions/ExecuteAppFunctionRequest$Builder"
        __javaconstructor__ = [("(Ljava/lang/String;Ljava/lang/String;)V", False)]
        setParameters = JavaMethod("(Landroid/app/appsearch/GenericDocument;)Landroid/app/appfunctions/ExecuteAppFunctionRequest$Builder;")
        setExtras = JavaMethod("(Landroid/os/Bundle;)Landroid/app/appfunctions/ExecuteAppFunctionRequest$Builder;")
        build = JavaMethod("()Landroid/app/appfunctions/ExecuteAppFunctionRequest;")