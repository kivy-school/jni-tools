from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["AssistContent"]

class AssistContent(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/app/assist/AssistContent"
    __javaconstructor__ = [("()V", False)]
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    setIntent = JavaMethod("(Landroid/content/Intent;)V")
    getIntent = JavaMethod("()Landroid/content/Intent;")
    isAppProvidedIntent = JavaMethod("()Z")
    setClipData = JavaMethod("(Landroid/content/ClipData;)V")
    getClipData = JavaMethod("()Landroid/content/ClipData;")
    setStructuredData = JavaMethod("(Ljava/lang/String;)V")
    getStructuredData = JavaMethod("()Ljava/lang/String;")
    setWebUri = JavaMethod("(Landroid/net/Uri;)V")
    getWebUri = JavaMethod("()Landroid/net/Uri;")
    isAppProvidedWebUri = JavaMethod("()Z")
    getExtras = JavaMethod("()Landroid/os/Bundle;")
    describeContents = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")