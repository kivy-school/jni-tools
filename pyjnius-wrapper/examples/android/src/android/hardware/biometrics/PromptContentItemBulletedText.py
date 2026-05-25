from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["PromptContentItemBulletedText"]

class PromptContentItemBulletedText(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/hardware/biometrics/PromptContentItemBulletedText"
    __javaconstructor__ = [("(Ljava/lang/String;)V", False)]
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    describeContents = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")