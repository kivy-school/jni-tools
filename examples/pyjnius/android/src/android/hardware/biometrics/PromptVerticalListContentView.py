from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["PromptVerticalListContentView"]

class PromptVerticalListContentView(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/hardware/biometrics/PromptVerticalListContentView"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    getListItems = JavaMethod("()Ljava/util/List;")
    getMaxItemCount = JavaStaticMethod("()I")
    getMaxEachItemCharacterNumber = JavaStaticMethod("()I")
    getDescription = JavaMethod("()Ljava/lang/String;")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/hardware/biometrics/PromptVerticalListContentView$Builder"
        __javaconstructor__ = [("()V", False)]
        setDescription = JavaMethod("(Ljava/lang/String;)Landroid/hardware/biometrics/PromptVerticalListContentView$Builder;")
        addListItem = JavaMultipleMethod([("(Landroid/hardware/biometrics/PromptContentItem;)Landroid/hardware/biometrics/PromptVerticalListContentView$Builder;", False, False), ("(Landroid/hardware/biometrics/PromptContentItem;I)Landroid/hardware/biometrics/PromptVerticalListContentView$Builder;", False, False)])
        build = JavaMethod("()Landroid/hardware/biometrics/PromptVerticalListContentView;")