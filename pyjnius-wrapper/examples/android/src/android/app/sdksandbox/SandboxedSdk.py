from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["SandboxedSdk"]

class SandboxedSdk(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/app/sdksandbox/SandboxedSdk"
    __javaconstructor__ = [("(Landroid/os/IBinder;)V", False)]
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    getInterface = JavaMethod("()Landroid/os/IBinder;")
    getSharedLibraryInfo = JavaMethod("()Landroid/content/pm/SharedLibraryInfo;")
    describeContents = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")