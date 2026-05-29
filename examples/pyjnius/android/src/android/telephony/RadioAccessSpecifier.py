from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["RadioAccessSpecifier"]

class RadioAccessSpecifier(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/telephony/RadioAccessSpecifier"
    __javaconstructor__ = [("(I[I[I)V", False)]
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    getChannels = JavaMethod("()[I")
    getRadioAccessNetwork = JavaMethod("()I")
    getBands = JavaMethod("()[I")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    toString = JavaMethod("()Ljava/lang/String;")
    hashCode = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")