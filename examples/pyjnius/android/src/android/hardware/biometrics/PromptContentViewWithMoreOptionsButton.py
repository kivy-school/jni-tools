from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["PromptContentViewWithMoreOptionsButton"]

class PromptContentViewWithMoreOptionsButton(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/hardware/biometrics/PromptContentViewWithMoreOptionsButton"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    getMoreOptionsButtonListener = JavaMethod("()Landroid/content/DialogInterface$OnClickListener;")
    getDescription = JavaMethod("()Ljava/lang/String;")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/hardware/biometrics/PromptContentViewWithMoreOptionsButton$Builder"
        __javaconstructor__ = [("()V", False)]
        setMoreOptionsButtonListener = JavaMethod("(Ljava/util/concurrent/Executor;Landroid/content/DialogInterface$OnClickListener;)Landroid/hardware/biometrics/PromptContentViewWithMoreOptionsButton$Builder;")
        setDescription = JavaMethod("(Ljava/lang/String;)Landroid/hardware/biometrics/PromptContentViewWithMoreOptionsButton$Builder;")
        build = JavaMethod("()Landroid/hardware/biometrics/PromptContentViewWithMoreOptionsButton;")