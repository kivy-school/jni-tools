from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Parcelable"]

class Parcelable(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "android/os/Parcelable"
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    describeContents = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")

    class ClassLoaderCreator(JavaInterface, metaclass=MetaJavaClass):
        __javaclass__ = "android/os/Parcelable/ClassLoaderCreator"
        createFromParcel = JavaMethod("(Landroid/os/Parcel;Ljava/lang/ClassLoader;)Ljava/lang/Object;")

    class Creator(JavaInterface, metaclass=MetaJavaClass):
        __javaclass__ = "android/os/Parcelable/Creator"
        createFromParcel = JavaMethod("(Landroid/os/Parcel;)Ljava/lang/Object;")
        newArray = JavaMethod("(I)[Ljava/lang/Object;")