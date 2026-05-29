from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Session2CommandGroup"]

class Session2CommandGroup(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/media/Session2CommandGroup"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    hasCommand = JavaMultipleMethod([("(Landroid/media/Session2Command;)Z", False, False), ("(I)Z", False, False)])
    getCommands = JavaMethod("()Ljava/util/Set;")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/media/Session2CommandGroup$Builder"
        __javaconstructor__ = [("(Landroid/media/Session2CommandGroup;)V", False), ("()V", False)]
        addCommand = JavaMethod("(Landroid/media/Session2Command;)Landroid/media/Session2CommandGroup$Builder;")
        removeCommand = JavaMethod("(Landroid/media/Session2Command;)Landroid/media/Session2CommandGroup$Builder;")
        build = JavaMethod("()Landroid/media/Session2CommandGroup;")