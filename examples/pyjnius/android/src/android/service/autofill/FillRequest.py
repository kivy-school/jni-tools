from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["FillRequest"]

class FillRequest(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/service/autofill/FillRequest"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    FLAG_COMPATIBILITY_MODE_REQUEST = JavaStaticField("I")
    FLAG_MANUAL_REQUEST = JavaStaticField("I")
    FLAG_SUPPORTS_FILL_DIALOG = JavaStaticField("I")
    getId = JavaMethod("()I")
    getFillContexts = JavaMethod("()Ljava/util/List;")
    getHints = JavaMethod("()Ljava/util/List;")
    getClientState = JavaMethod("()Landroid/os/Bundle;")
    getFlags = JavaMethod("()I")
    getInlineSuggestionsRequest = JavaMethod("()Landroid/view/inputmethod/InlineSuggestionsRequest;")
    getDelayedFillIntentSender = JavaMethod("()Landroid/content/IntentSender;")
    toString = JavaMethod("()Ljava/lang/String;")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")