from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["SharedLibraryInfo"]

class SharedLibraryInfo(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/content/pm/SharedLibraryInfo"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    TYPE_BUILTIN = JavaStaticField("I")
    TYPE_DYNAMIC = JavaStaticField("I")
    TYPE_SDK_PACKAGE = JavaStaticField("I")
    TYPE_STATIC = JavaStaticField("I")
    VERSION_UNDEFINED = JavaStaticField("I")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    getLongVersion = JavaMethod("()J")
    getCertDigests = JavaMethod("()Ljava/util/List;")
    getDeclaringPackage = JavaMethod("()Landroid/content/pm/VersionedPackage;")
    getDependentPackages = JavaMethod("()Ljava/util/List;")
    getName = JavaMethod("()Ljava/lang/String;")
    toString = JavaMethod("()Ljava/lang/String;")
    getType = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")
    getVersion = JavaMethod("()I")