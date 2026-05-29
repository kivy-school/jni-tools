from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Parcelable"]

class Parcelable(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/os/Parcelable"
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")

    class Creator(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/os/Parcelable$Creator"
        newArray = JavaMethod("(I)[Ljava/lang/Object;")
        createFromParcel = JavaMethod("(Landroid/os/Parcel;)Ljava/lang/Object;")

    class ClassLoaderCreator(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/os/Parcelable$ClassLoaderCreator"
        createFromParcel = JavaMethod("(Landroid/os/Parcel;Ljava/lang/ClassLoader;)Ljava/lang/Object;")