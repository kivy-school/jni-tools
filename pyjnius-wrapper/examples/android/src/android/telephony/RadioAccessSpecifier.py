from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["RadioAccessSpecifier"]

class RadioAccessSpecifier(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/telephony/RadioAccessSpecifier"
    __javaconstructor__ = [("(I[I[I)V", False)]
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    getRadioAccessNetwork = JavaMethod("()I")
    getBands = JavaMethod("()[I")
    getChannels = JavaMethod("()[I")
    describeContents = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")
    toString = JavaMethod("()Ljava/lang/String;")