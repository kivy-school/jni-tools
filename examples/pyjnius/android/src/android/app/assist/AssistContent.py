from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["AssistContent"]

class AssistContent(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/app/assist/AssistContent"
    __javaconstructor__ = [("()V", False)]
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    EXTRA_APP_FUNCTION_DATA = JavaStaticField("Ljava/lang/String;")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    setStructuredData = JavaMethod("(Ljava/lang/String;)V")
    getWebUri = JavaMethod("()Landroid/net/Uri;")
    getStructuredData = JavaMethod("()Ljava/lang/String;")
    getSessionTransferUri = JavaMethod("()Landroid/net/Uri;")
    isAppProvidedIntent = JavaMethod("()Z")
    isAppProvidedWebUri = JavaMethod("()Z")
    setSessionTransferUri = JavaMethod("(Landroid/net/Uri;)V")
    setWebUri = JavaMethod("(Landroid/net/Uri;)V")
    setIntent = JavaMethod("(Landroid/content/Intent;)V")
    setClipData = JavaMethod("(Landroid/content/ClipData;)V")
    getClipData = JavaMethod("()Landroid/content/ClipData;")
    getIntent = JavaMethod("()Landroid/content/Intent;")
    getExtras = JavaMethod("()Landroid/os/Bundle;")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")