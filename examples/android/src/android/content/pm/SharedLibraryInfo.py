from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["SharedLibraryInfo"]

class SharedLibraryInfo(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/content/pm/SharedLibraryInfo"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    TYPE_BUILTIN = JavaStaticField("I")
    TYPE_DYNAMIC = JavaStaticField("I")
    TYPE_SDK_PACKAGE = JavaStaticField("I")
    TYPE_STATIC = JavaStaticField("I")
    VERSION_UNDEFINED = JavaStaticField("I")
    getType = JavaMethod("()I")
    getName = JavaMethod("()Ljava/lang/String;")
    getVersion = JavaMethod("()I")
    getLongVersion = JavaMethod("()J")
    getDeclaringPackage = JavaMethod("()Landroid/content/pm/VersionedPackage;")
    getDependentPackages = JavaMethod("()Ljava/util/List;")
    describeContents = JavaMethod("()I")
    toString = JavaMethod("()Ljava/lang/String;")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")