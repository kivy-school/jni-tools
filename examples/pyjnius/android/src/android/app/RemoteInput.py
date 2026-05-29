from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

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
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    getLabel = JavaMethod("()Ljava/lang/CharSequence;")
    getExtras = JavaMethod("()Landroid/os/Bundle;")
    addDataResultToIntent = JavaStaticMethod("(Landroid/app/RemoteInput;Landroid/content/Intent;Ljava/util/Map;)V")
    addResultsToIntent = JavaStaticMethod("([Landroid/app/RemoteInput;Landroid/content/Intent;Landroid/os/Bundle;)V")
    getAllowFreeFormInput = JavaMethod("()Z")
    getAllowedDataTypes = JavaMethod("()Ljava/util/Set;")
    getChoices = JavaMethod("()[Ljava/lang/CharSequence;")
    getDataResultsFromIntent = JavaStaticMethod("(Landroid/content/Intent;Ljava/lang/String;)Ljava/util/Map;")
    getEditChoicesBeforeSending = JavaMethod("()I")
    getResultKey = JavaMethod("()Ljava/lang/String;")
    getResultsFromIntent = JavaStaticMethod("(Landroid/content/Intent;)Landroid/os/Bundle;")
    getResultsSource = JavaStaticMethod("(Landroid/content/Intent;)I")
    isDataOnly = JavaMethod("()Z")
    setResultsSource = JavaStaticMethod("(Landroid/content/Intent;I)V")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/app/RemoteInput$Builder"
        __javaconstructor__ = [("(Ljava/lang/String;)V", False)]
        setChoices = JavaMethod("([Ljava/lang/CharSequence;)Landroid/app/RemoteInput$Builder;")
        setEditChoicesBeforeSending = JavaMethod("(I)Landroid/app/RemoteInput$Builder;")
        setAllowFreeFormInput = JavaMethod("(Z)Landroid/app/RemoteInput$Builder;")
        setAllowDataType = JavaMethod("(Ljava/lang/String;Z)Landroid/app/RemoteInput$Builder;")
        getExtras = JavaMethod("()Landroid/os/Bundle;")
        setLabel = JavaMethod("(Ljava/lang/CharSequence;)Landroid/app/RemoteInput$Builder;")
        build = JavaMethod("()Landroid/app/RemoteInput;")
        addExtras = JavaMethod("(Landroid/os/Bundle;)Landroid/app/RemoteInput$Builder;")