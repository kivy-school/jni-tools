from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["GameState"]

class GameState(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/app/GameState"
    __javaconstructor__ = [("(ZI)V", False), ("(ZIII)V", False)]
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    MODE_CONTENT = JavaStaticField("I")
    MODE_GAMEPLAY_INTERRUPTIBLE = JavaStaticField("I")
    MODE_GAMEPLAY_UNINTERRUPTIBLE = JavaStaticField("I")
    MODE_NONE = JavaStaticField("I")
    MODE_UNKNOWN = JavaStaticField("I")
    isLoading = JavaMethod("()Z")
    getMode = JavaMethod("()I")
    getLabel = JavaMethod("()I")
    getQuality = JavaMethod("()I")
    describeContents = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")