from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["RemoteInput"]

class RemoteInput(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/app/RemoteInput"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    EDIT_CHOICES_BEFORE_SENDING_AUTO = JavaStaticField("I")
    EDIT_CHOICES_BEFORE_SENDING_DISABLED = JavaStaticField("I")
    EDIT_CHOICES_BEFORE_SENDING_ENABLED = JavaStaticField("I")
    EXTRA_RESULTS_DATA = JavaStaticField("Ljava/lang/String;")
    RESULTS_CLIP_LABEL = JavaStaticField("Ljava/lang/String;")
    SOURCE_CHOICE = JavaStaticField("I")
    SOURCE_FREE_FORM_INPUT = JavaStaticField("I")
    getResultKey = JavaMethod("()Ljava/lang/String;")
    getLabel = JavaMethod("()Ljava/lang/CharSequence;")
    getChoices = JavaMethod("()[Ljava/lang/CharSequence;")
    getAllowedDataTypes = JavaMethod("()Ljava/util/Set;")
    isDataOnly = JavaMethod("()Z")
    getAllowFreeFormInput = JavaMethod("()Z")
    getEditChoicesBeforeSending = JavaMethod("()I")
    getExtras = JavaMethod("()Landroid/os/Bundle;")
    getDataResultsFromIntent = JavaStaticMethod("(Landroid/content/Intent;Ljava/lang/String;)Ljava/util/Map;")
    getResultsFromIntent = JavaStaticMethod("(Landroid/content/Intent;)Landroid/os/Bundle;")
    addResultsToIntent = JavaStaticMethod("([Landroid/app/RemoteInput;Landroid/content/Intent;Landroid/os/Bundle;)V")
    addDataResultToIntent = JavaStaticMethod("(Landroid/app/RemoteInput;Landroid/content/Intent;Ljava/util/Map;)V")
    setResultsSource = JavaStaticMethod("(Landroid/content/Intent;I)V")
    getResultsSource = JavaStaticMethod("(Landroid/content/Intent;)I")
    describeContents = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/app/RemoteInput/Builder"
        __javaconstructor__ = [("(Ljava/lang/String;)V", False)]
        setLabel = JavaMethod("(Ljava/lang/CharSequence;)Landroid/app/RemoteInput$Builder;")
        setChoices = JavaMethod("([Ljava/lang/CharSequence;)Landroid/app/RemoteInput$Builder;")
        setAllowDataType = JavaMethod("(Ljava/lang/String;Z)Landroid/app/RemoteInput$Builder;")
        setAllowFreeFormInput = JavaMethod("(Z)Landroid/app/RemoteInput$Builder;")
        setEditChoicesBeforeSending = JavaMethod("(I)Landroid/app/RemoteInput$Builder;")
        addExtras = JavaMethod("(Landroid/os/Bundle;)Landroid/app/RemoteInput$Builder;")
        getExtras = JavaMethod("()Landroid/os/Bundle;")
        build = JavaMethod("()Landroid/app/RemoteInput;")