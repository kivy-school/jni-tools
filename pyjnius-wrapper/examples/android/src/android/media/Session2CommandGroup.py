from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Session2CommandGroup"]

class Session2CommandGroup(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/media/Session2CommandGroup"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    hasCommand = JavaMultipleMethod([("(Landroid/media/Session2Command;)Z", False, False), ("(I)Z", False, False)])
    getCommands = JavaMethod("()Ljava/util/Set;")
    describeContents = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/media/Session2CommandGroup/Builder"
        __javaconstructor__ = [("()V", False), ("(Landroid/media/Session2CommandGroup;)V", False)]
        addCommand = JavaMethod("(Landroid/media/Session2Command;)Landroid/media/Session2CommandGroup$Builder;")
        removeCommand = JavaMethod("(Landroid/media/Session2Command;)Landroid/media/Session2CommandGroup$Builder;")
        build = JavaMethod("()Landroid/media/Session2CommandGroup;")