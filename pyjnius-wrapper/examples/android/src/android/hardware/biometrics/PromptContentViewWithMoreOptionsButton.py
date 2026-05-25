from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["PromptContentViewWithMoreOptionsButton"]

class PromptContentViewWithMoreOptionsButton(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/hardware/biometrics/PromptContentViewWithMoreOptionsButton"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    getDescription = JavaMethod("()Ljava/lang/String;")
    getMoreOptionsButtonListener = JavaMethod("()Landroid/content/DialogInterface$OnClickListener;")
    describeContents = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/hardware/biometrics/PromptContentViewWithMoreOptionsButton/Builder"
        __javaconstructor__ = [("()V", False)]
        setDescription = JavaMethod("(Ljava/lang/String;)Landroid/hardware/biometrics/PromptContentViewWithMoreOptionsButton$Builder;")
        setMoreOptionsButtonListener = JavaMethod("(Ljava/util/concurrent/Executor;Landroid/content/DialogInterface$OnClickListener;)Landroid/hardware/biometrics/PromptContentViewWithMoreOptionsButton$Builder;")
        build = JavaMethod("()Landroid/hardware/biometrics/PromptContentViewWithMoreOptionsButton;")