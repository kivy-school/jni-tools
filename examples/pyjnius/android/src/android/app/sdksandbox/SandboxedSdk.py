from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["SandboxedSdk"]

class SandboxedSdk(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/app/sdksandbox/SandboxedSdk"
    __javaconstructor__ = [("(Landroid/os/IBinder;)V", False)]
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    getSharedLibraryInfo = JavaMethod("()Landroid/content/pm/SharedLibraryInfo;")
    getInterface = JavaMethod("()Landroid/os/IBinder;")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")